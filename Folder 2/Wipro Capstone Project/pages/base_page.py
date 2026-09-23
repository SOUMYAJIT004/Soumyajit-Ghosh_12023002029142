from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )
    
    def click_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator, text, time=10):
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)
        
    def get_text(self, locator, time=10):
        return self.find_element(locator, time).text
