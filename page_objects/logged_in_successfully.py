from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __text_locator = (By.TAG_NAME, "h1")
    __log_out_btn = (By.LINK_TEXT, "Log out")

    def __init__(self,driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def header(self) -> str:
        return super()._get_text(self.__text_locator)
        # return self._driver.find_element(self.__text_locator).text

    def is_log_out_btn(self) -> bool:
        return super()._is_displayed(self.__log_out_btn)
        # assert self._driver.find_element(self.__log_out_btn).is_displayed()