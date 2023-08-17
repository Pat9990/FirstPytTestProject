import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username,password,expected_error_message", [("incorrectUser", "Password123", "Your "
                                                                                                           "username is"
                                                                                                           " invalid!"),
                                                                          ("student", "Password12345",
                                                                           "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.get_error_message() == expected_error_message, "Error message is not expected"

        # driver.get("https://practicetestautomation.com/practice-test-login/")
        # time.sleep(2)
        # username_locator = driver.find_element(By.ID, "username")
        # username_locator.send_keys(username)
        #
        # password_locator = driver.find_element(By.ID, "password")
        # password_locator.send_keys(password)
        #
        # submit_btn = driver.find_element(By.XPATH, "//button[@id='submit']")
        # submit_btn.click()

        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be"
        error_message = error_message_locator.text
        assert error_message == expected_error_message, "Error message is not expected"

    # @pytest.mark.login
    # @pytest.mark.negative
    # def test_negative_username(self, driver):
    #
    #     # driver = webdriver.Chrome()
    #     driver.get("https://practicetestautomation.com/practice-test-login/")
    #     time.sleep(2)
    #     username_locator = driver.find_element(By.ID, "username")
    #     username_locator.send_keys("incorrectUser")
    #
    #     password_locator = driver.find_element(By.ID, "password")
    #     password_locator.send_keys("Password123")
    #
    #     submit_btn = driver.find_element(By.XPATH, "//button[@id='submit']")
    #     submit_btn.click()
    #     time.sleep(2)
    #     error_message_locator = driver.find_element(By.ID, "error")
    #     assert error_message_locator._is_displayed(), "Error message is not displayed, but it should be"
    #     error_message = error_message_locator.text
    #     assert error_message == "Your username is invalid!", "Error message is not expected"
    #
    # @pytest.mark.login
    # @pytest.mark.negative
    # def test_negative_password(self, driver):
    #     # driver = webdriver.Chrome()
    #     driver.get("https://practicetestautomation.com/practice-test-login/")
    #     time.sleep(2)
    #     username_locator = driver.find_element(By.ID, "username")
    #     username_locator.send_keys("student")
    #
    #     password_locator = driver.find_element(By.ID, "password")
    #     password_locator.send_keys("Password12345")
    #
    #     submit_btn = driver.find_element(By.XPATH, "//button[@id='submit']")
    #     submit_btn.click()
    #     time.sleep(2)
    #     error_message_locator = driver.find_element(By.ID, "error")
    #     assert error_message_locator._is_displayed(), "Error message is not displayed, but it should be"
    #     error_message = error_message_locator.text
    #     assert error_message == "Your password is invalid!", "Error message is not expected"
