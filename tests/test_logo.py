from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.logo_locators import LogoLocators
from url import *

class TestLogo:

    def test_scooter_logo(self, driver):
        driver.get(order_page)
        driver.find_element(*LogoLocators.logo_scooter).click()

        assert driver.current_url == main_site

    def test_ya_logo(self, driver):
        driver.get(order_page)
        driver.find_element(*LogoLocators.ya_logo).click()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(EC.url_contains(dzen))

        assert driver.current_url == dzen