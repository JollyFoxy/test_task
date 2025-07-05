from elements.base_element import BaseElement
from selenium.webdriver.chrome.webdriver import WebDriver


class Img(BaseElement):
    def __init__(self, xpath: str, driver: WebDriver):
        super().__init__(xpath, driver)

    def get_width(self):
        width = self._element.get_attribute('width')
        return width

    def get_height(self):
        height = self._element.get_attribute('height')
        return height