import allure
from url import *
from pages.logo_page import LogoPage

class TestLogo():

    @allure.title('Проверка перехода на главную страницу по клику на логотип самоката')
    def test_scooter_logo(self, driver):
        logo_page = LogoPage(driver)
        logo_page.open_page(order_page)
        logo_page.click_logo_scooter()

        current_url = logo_page.get_current_url()
        assert current_url == main_site

    @allure.title('Проверка открытия нового окна с сайтом Дзен по клику на логотип Яндекса')
    def test_ya_logo(self, driver):
        logo_page = LogoPage(driver)
        logo_page.open_page(order_page)
        logo_page.click_logo_ya()
        logo_page.switch_to_dzen()
        current_url = logo_page.get_current_url()

        assert "dzen.ru" in current_url