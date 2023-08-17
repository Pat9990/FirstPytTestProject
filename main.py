import time

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdrivermanager import ChromeDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#open broweser
driver = webdriver.Chrome()

#go to website
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

password_locator = driver.find_element(By.ID, "password")
password_locator.send_keys("Password123")

submit_btn = driver.find_element(By.XPATH,"//button[@id='submit']")
submit_btn.click()
time.sleep(2)

actual_url = driver.current_url
assert  actual_url == "https://practicetestautomation.com/logged-in-successfully/"

text = driver.find_element(By.TAG_NAME,"h1")
actual_text = text.text
assert actual_text == "Logged In Successfully"

log_out_btn = driver.find_element(By.LINK_TEXT,"Log out")
assert log_out_btn.is_displayed()



