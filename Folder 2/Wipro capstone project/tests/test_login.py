import unittest
import pytest
import time
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class TestLogin(unittest.TestCase):
    
    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        # Ensure we are starting from the home page
        self.driver.get("https://tutorialsninja.com/demo/")
        login_page.navigate_to_login()
        
        # Use dynamic email to avoid website rate-limiting block
        dynamic_email = f"invalid_user_{int(time.time())}@test.com"
        login_page.login(dynamic_email, "wrongpassword")
        
        error_msg = login_page.get_error_message()
        self.assertIn("Warning: No match for E-Mail Address and/or Password.", error_msg)

    def test_failing_login_for_screenshot(self):
        """This test is intentionally failed to verify the screenshot functionality"""
        login_page = LoginPage(self.driver)
        # Ensure we are starting from the home page
        self.driver.get("https://tutorialsninja.com/demo/")
        login_page.navigate_to_login()
        
        # Try logging in with valid format but invalid credentials
        dynamic_email = f"test_fail_{int(time.time())}@test.com"
        login_page.login(dynamic_email, "test")
        
        # Asserting login is successful, but it will fail and take screenshot
        self.assertTrue(login_page.is_login_successful(), "Intentional failure to generate screenshot")
