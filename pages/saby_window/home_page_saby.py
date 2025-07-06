import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from elements.div import Div
from elements.a import A

class HomePageSaby:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Открытие страницы')
    def open(self):
        self.driver.get("https://saby.ru/")

    @allure.step('Открытие подменю "Контакты"')
    def click_on_contacts(self):
        contacts = Div(xpath='//div[@class="sbisru-Header__menu-link sbis_ru-Header__menu-link sbisru-Header__menu-link--hover"]',
                       driver= self.driver)
        contacts.click_div()

    @allure.step('Переход на страницу с контактами в регионе')
    def click_on_contacts_regions(self):
        contacts = A(xpath='//a[@href="/contacts"]', driver= self.driver)
        contacts.click_to_a()




