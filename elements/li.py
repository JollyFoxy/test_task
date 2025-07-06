from selenium.webdriver.chrome.webdriver import WebDriver

from elements.base_element import BaseElement


class Li(BaseElement):
    def __init__(self, xpath: str, driver: WebDriver):
        super().__init__(xpath, driver)

    def click_to_li(self):
        self._element.click()
