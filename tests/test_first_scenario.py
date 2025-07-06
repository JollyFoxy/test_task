from pages.saby_window.home_page_saby import HomePageSaby
from pages.saby_window.contacts_page_saby import ContactsPageSaby
from pages.tensor_window.home_page_tesor import HomePageTensor
from pages.tensor_window.about_page_tensor import AboutPageTensor
import allure


@allure.title("Первый сценарий")
def test_first_scenario(driver):
    home_page_saby = HomePageSaby(driver)
    contacts_page_say = ContactsPageSaby(driver)
    home_page_tesor = HomePageTensor(driver)
    about_page_tensor = AboutPageTensor(driver)

    home_page_saby.open()
    home_page_saby.click_on_contacts()
    home_page_saby.click_on_contacts_regions()
    contacts_page_say.click_on_tensor_logo()
    home_page_tesor.switch_to_window()
    home_page_tesor.check_box()
    home_page_tesor.click_about_company()
    about_page_tensor.move_to_block()
    about_page_tensor.check_img()

