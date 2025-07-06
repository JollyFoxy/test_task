from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ActionChains
from elements.div import Div
from elements.img import Img
import allure



class AboutPageTensor:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Прокуртка до блока "Работаем"')
    def move_to_block(self):
        block = Div( xpath='//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]', driver=self.driver)
        ActionChains(self.driver).scroll_to_element(block.get_element()).perform()

    @allure.step('Проверка одинаков ли размер изображений')
    def check_img(self):
        img1 = Img(xpath='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img', driver=self.driver)
        img2 = Img(xpath='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img', driver=self.driver)
        img3 = Img(xpath='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img', driver=self.driver)
        img4 = Img(xpath='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img', driver=self.driver)
        size = [[img1.get_width(),img1.get_height()],
                [img2.get_width(),img2.get_height()],
                [img3.get_width(),img3.get_height()],
                [img4.get_width(),img4.get_height()]]
        for i in range(len(size)):
            cp = size[0]
            assert cp == size[i]
