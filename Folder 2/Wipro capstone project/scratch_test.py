from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")

wait = WebDriverWait(driver, 10)
# Click My Account
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='My Account']"))).click()
# Click Login
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

# Enter email
wait.until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys("invalid_user_12345@test.com")
# Enter password
driver.find_element(By.ID, "input-password").send_keys("wrongpassword")
# Click Login button
driver.find_element(By.XPATH, "//input[@value='Login']").click()

# Check error alert
error = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert-danger")))
print("ERROR MSG:", error.text)

driver.quit()
