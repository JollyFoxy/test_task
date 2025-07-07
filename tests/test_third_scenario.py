from pages.saby_window.home_page_saby import HomePageSaby
from pages.saby_window.download_page_saby import DownloadPageSaby


def test_third_scenario(driver):
    home_page_sabay = HomePageSaby(driver)
    download_page_saby = DownloadPageSaby(driver)

    home_page_sabay.open()
    home_page_sabay.click_on_download()
    download_page_saby.download_file()
    download_page_saby.check_file()