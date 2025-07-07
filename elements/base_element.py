from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BaseElement:
    def __init__(self, xpath: str, driver: WebDriver):
        self._driver = driver
        self._element = driver.find_element(By.XPATH, xpath)
        self._actions = ActionChains(self._driver)

    def get_text(self):
        value = self._element.text
        return value

    def get_value(self):
        value = self._element.get_attribute('value')
        return value

    def get_attribute(self, attributee: str):
        value = self._element.get_attribute(attributee)
        return value

    def is_visible(self) -> bool:
        if self._element.is_displayed():
            return True
        else:
            return False

    def is_enabled(self):
        self._element.is_enabled()

    def get_element(self):
        return self._element
