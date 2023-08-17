import time

import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdrivermanager import ChromeDriverManager

from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_posistive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"
        assert logged_in_page.header == "Logged In Successfully", "Header is no expected"
        assert logged_in_page.is_log_out_btn(), "Logout btn should be visisble"


        # driver.get("https://practicetestautomation.com/practice-test-login/")
        # time.sleep(2)
        # username_locator = driver.find_element(By.ID, "username")
        # username_locator.send_keys("student")
        #
        # password_locator = driver.find_element(By.ID, "password")
        # password_locator.send_keys("Password123")
        #
        # submit_btn = driver.find_element(By.XPATH, "//button[@id='submit']")
        # submit_btn.click()
        # time.sleep(2)
        #
        # actual_url = driver.current_url
        # assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
        #
        # text = driver.find_element(By.TAG_NAME, "h1")
        # actual_text = text.text
        # assert actual_text == "Logged In Successfully"
        #
        # log_out_btn = driver.find_element(By.LINK_TEXT, "Log out")
        # assert log_out_btn._is_displayed()
