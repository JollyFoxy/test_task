from selenium.webdriver.chrome.webdriver import WebDriver

from elements.base_element import BaseElement


class A(BaseElement):
    def __init__(self, xpath: str, driver: WebDriver):
        super().__init__(xpath, driver)

    def hover_to_a(self):
        self._actions.move_to_element(self._element).perform()

    def click_to_a(self):
        self._element.click()
