import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



def download_file(driver: webdriver.Chrome,
                  download_link_xpath:  str,
                  download_directory: str,
                  expected_filename: str) -> None:


    download_link = driver.find_element(By.XPATH ,download_link_xpath)
    download_link.click()

    file_path = os.path.join(f'{download_directory}/{expected_filename}')

    for i in range(20):
        if os.path.exists(file_path):
            print(f"Файл {expected_filename} успешно скачан.")
            return
        time.sleep(1)

    raise FileNotFoundError(f"Файл {expected_filename} не был скачан в течение 20 ctreyl.")
