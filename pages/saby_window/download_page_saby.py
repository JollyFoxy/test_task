import os

from selenium.webdriver.chrome.webdriver import WebDriver
from elements.helper.download import download_file
import allure



class DownloadPageSaby:
    def __init__(self, driver: WebDriver):
         self.driver = driver

    @allure.step('Загрузка файла')
    def download_file(self):
        """Скачиваю и проверяю другой файл т.к. нужная вкладка с файлом отсутствовала"""
        download_file(driver= self.driver,
                      download_link_xpath= '//a[@href="https://update.saby.ru/SabyDesktop/master/win32/saby-setup-web.exe"]',
                      download_directory= '/Users/pavel.mizirev/PycharmProjects/test_task/d_dir',
                      expected_filename= 'saby-setup-web.exe')

    @allure.step('Проверка скаченого файла')
    def check_file(self):
        assert os.path.getsize('/Users/pavel.mizirev/PycharmProjects/test_task/d_dir/saby-setup-web.exe') == 11062976
