from pages.saby_window.home_page_saby import HomePageSaby
from pages.saby_window.contacts_page_saby import ContactsPageSaby
import allure


@allure.title("Второй сценарий")
def test_second_scenario(driver):
    home_page_saby = HomePageSaby(driver)
    contacts_page_saby = ContactsPageSaby(driver)

    home_page_saby.open()
    home_page_saby.click_on_contacts()
    home_page_saby.click_on_contacts_regions()
    contacts_page_saby.check_region('Костромская обл.')
    contacts_page_saby.check_partners_city('Кострома')
    contacts_page_saby.change_region()
    contacts_page_saby.check_url('https://saby.ru/contacts/41-kamchatskij-kraj?tab=clients')
    contacts_page_saby.check_title('Saby Контакты — Камчатский край')
    contacts_page_saby.check_region('Камчатский край')
    contacts_page_saby.check_partners_city('Петропавловск-Камчатский')
