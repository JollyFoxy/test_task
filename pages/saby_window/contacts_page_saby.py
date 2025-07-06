import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from elements.a import A
from elements.span import Span
from elements.div import Div
from elements.li import Li


class ContactsPageSaby:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Нажатие на логотип "Тензор"')
    def click_on_tensor_logo(self):
        tensor_logo = A(xpath='//a[@class="sbisru-Contacts__logo-tensor mb-12"]', driver=self.driver)
        tensor_logo.click_to_a()

    @allure.step('Проверка региона страници')
    def check_region(self, region):
        reg = Span(xpath='//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span',
                      driver=self.driver)
        assert reg.wait_get_text() == region

    @allure.step('Проверка города партнеров')
    def check_partners_city(self, city):
        partners = Div(xpath='//div[@id="city-id-2"]',driver=self.driver)
        assert partners.get_text() == city

    @allure.step('Изменение региона')
    def change_region(self):
        #region = Div(xpath="//span[@class='sbis_ru-Region-Chooser ml-16 ml-xm-0']/div",driver=self.driver)
        kamchatka = Li(xpath='//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]',
                       driver=self.driver)
        #region.click()
        kamchatka.click_to_li()

    @allure.step('Проверка заголовка страници')
    def check_title(self, title):
        assert self.driver.title == title

    @allure.step('Проверка URL страници')
    def check_url(self, url):
        assert self.driver.current_url == url