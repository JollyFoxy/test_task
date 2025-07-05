from selenium.webdriver.chrome.webdriver import WebDriver

from elements.base_element import BaseElement


class P(BaseElement):
    def __init__(self, xpath: str, driver: WebDriver):

        super().__init__(xpath, driver)

    def check_text_p(self, text):
        assert self._element.text == text
