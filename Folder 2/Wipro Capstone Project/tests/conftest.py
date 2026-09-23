import pytest
import os
from selenium import webdriver
from utils.config_reader import get_config

@pytest.fixture(scope="function")
def setup_teardown(request):
    config = get_config()
    browser = config['DEFAULT'].get('browser', 'chrome').lower()
    
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless') # Uncomment to run headless
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Browser {browser} not supported")

    driver.maximize_window()
    driver.implicitly_wait(int(config['DEFAULT'].get('implicit_wait', 10)))
    driver.get(config['DEFAULT'].get('url'))
    
    request.cls.driver = driver
    yield driver
    
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    
    if report.when == "call" and report.failed:
        if hasattr(item.cls, "driver"):
            driver = item.cls.driver
            screenshot_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots')
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_name = f"{item.name}.png"
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)
            driver.save_screenshot(screenshot_path)
            
            # Embed screenshot in pytest-html report
            from pytest_html import extras
            # Use relative path for HTML report compatibility if possible, or absolute path
            extra.append(extras.image(screenshot_path))
            
    report.extra = extra

def pytest_configure(config):
    # Register custom extras if pytest-html is used
    if not hasattr(config, '_metadata'):
        config._metadata = {}
