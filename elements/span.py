from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ActionChains
from elements.base_element import BaseElement


class Span(BaseElement):
    def __init__(self, xpath: str, driver: WebDriver):
        super().__init__(xpath, driver)

    def click(self):
        ActionChains(self._driver).move_to_element(self._element).click().perform()

    def wait_get_text(self):
        return self._driver.execute_script("return arguments[0].textContent;", self._element)