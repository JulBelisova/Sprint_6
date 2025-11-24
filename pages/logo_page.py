import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.logo_locators import LogoLocators
from .base_page import BasePage

class LogoPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликнуть на логотип самоката')
    def click_logo_scooter(self):
        self.click_element(LogoLocators.logo_scooter)
    
    @allure.step('Кликнуть на логотип Яндекса')
    def click_logo_ya(self):
        self.click_element(LogoLocators.ya_logo)

    @allure.step('Переключиться на окно Дзена')
    def switch_to_dzen(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(EC.url_contains("dzen.ru"))

    