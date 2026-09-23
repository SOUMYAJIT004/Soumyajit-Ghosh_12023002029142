from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    SEARCH_BOX = (By.NAME, "search")
    SEARCH_BTN = (By.CSS_SELECTOR, "div#search button")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div.product-layout")
    NO_RESULTS_MSG = (By.XPATH, "//p[contains(text(), 'There is no product that matches the search criteria.')]")

    def search_product(self, product_name):
        self.enter_text(self.SEARCH_BOX, product_name)
        self.click_element(self.SEARCH_BTN)

    def has_results(self):
        try:
            results = self.driver.find_elements(*self.SEARCH_RESULTS)
            return len(results) > 0
        except:
            return False
            
    def get_no_results_message(self):
        return self.get_text(self.NO_RESULTS_MSG)
