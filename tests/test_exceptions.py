import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.exceptions_page import ExceptionsPage


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exceptions(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_first_row()
        assert exceptions_page.is_row2_displayed(),"Row 2 input should be displayed"



        # driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # add_btn = driver.find_element(By.ID, "add_btn")
        # add_btn.click()
        #
        # wait = WebDriverWait(driver, 10)
        # row2_field = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']//input")))
        # assert row2_field._is_displayed(), "row is not displayed"

