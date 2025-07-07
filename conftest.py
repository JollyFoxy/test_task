import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    download_dir = "/Users/pavel.mizirev/PycharmProjects/test_task/d_dir"

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    chrome_driver = webdriver.Chrome(options = chrome_options)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    yield chrome_driver

