from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    MY_ACCOUNT_MENU = (By.XPATH, "//span[text()='My Account']")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BTN = (By.XPATH, "//input[@value='Login']")
    ERROR_ALERT = (By.CSS_SELECTOR, "div.alert-danger")
    MY_ACCOUNT_HEADER = (By.XPATH, "//h2[text()='My Account']")

    def navigate_to_login(self):
        self.click_element(self.MY_ACCOUNT_MENU)
        self.click_element(self.LOGIN_LINK)

    def login(self, email, password):
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BTN)

    def is_login_successful(self):
        try:
            return self.find_element(self.MY_ACCOUNT_HEADER, time=5).is_displayed()
        except:
            return False

    def get_error_message(self):
        return self.get_text(self.ERROR_ALERT)
