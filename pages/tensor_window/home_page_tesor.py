from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ActionChains
from elements.div import Div
from elements.a import A



class HomePageTensor:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def switch_to_window (self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == 'https://tensor.ru/'

    def check_box(self):
        box = Div(xpath='//div[@class="tensor_ru-Index__block4-content tensor_ru-Index__card"]', driver=self.driver)
        ActionChains(self.driver).scroll_to_element(box.get_element()).perform()
        assert box.is_visible() is True

    def click_about_company(self):
        link = A(xpath='/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a'
                 ,driver=self.driver)
        link.click_to_a()
        assert self.driver.current_url == 'https://tensor.ru/about'




