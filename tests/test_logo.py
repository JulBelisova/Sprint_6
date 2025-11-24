import allure
from url import *
from pages.logo_page import LogoPage

class TestLogo():

    @allure.title('Проверка перехода на главную страницу по клику на логотип самоката')
    def test_scooter_logo(self, driver):
        logo_page = LogoPage(driver)
        driver.get(order_page)
        logo_page.click_logo_scooter()

        assert driver.current_url == main_site

    @allure.title('Проверка открытия нового окна с сайтом Дзен по клику на логотип Яндекса')
    def test_ya_logo(self, driver):
        logo_page = LogoPage(driver)
        driver.get(order_page)
        logo_page.click_logo_ya()
        logo_page.switch_to_dzen()

        assert "dzen.ru" in driver.current_url