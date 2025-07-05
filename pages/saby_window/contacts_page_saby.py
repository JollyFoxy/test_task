import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from elements.a import A


class ContactsPageSaby:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_on_logo(self):
        tensor_logo = A(xpath='//a[@class="sbisru-Contacts__logo-tensor mb-12"]', driver=self.driver)
        tensor_logo.click_to_a()