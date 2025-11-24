import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.questions_locators import QuestionLocatorsPage
from locators.order_locators import OrderLocators
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Принять куки')
    def accept_cookies(self):
        self.click_element(QuestionLocatorsPage.accept_cookies)

    @allure.step('Кликнуть на кнопку Заказать в верхнем меню')
    def click_up_order(self):
        self.click_element(OrderLocators.order_up_button)  

    @allure.step('Кликнуть на кнопку Заказать внизу страницы')
    def click_down_order(self):
        self.click_element(OrderLocators.order_down_button)

    @allure.step('Заполнить всю информацию о клиенте')
    def fill_order_form(self, data):
        self.send_keys(OrderLocators.name, data["name"])
        self.send_keys(OrderLocators.surname, data["surname"])
        self.send_keys(OrderLocators.address, data["address"])
        self.send_keys(OrderLocators.subway_station, data["subway"])
        self.click_element(OrderLocators.subway_station_by_name(data['subway']))
        self.send_keys(OrderLocators.phone, data["phone"])

    @allure.step('Кликнуть Далее')
    def click_next(self):
        self.click_element(OrderLocators.next)

    @allure.step('Заполнить информацию об аренде')
    def fill_info_about_order(self, data):
        self.send_keys(OrderLocators.when_to_deliver, data["when"])
        self.send_keys(OrderLocators.when_to_deliver, Keys.ESCAPE)
        self.click_element(OrderLocators.rental_period)
        self.click_element(OrderLocators.two_days)
        self.click_element(OrderLocators.color)

    @allure.step('Кликнуть Заказать')
    def click_final_order(self):
        self.click_element(OrderLocators.final_order_button)

    @allure.step('Кликнуть на кнопку Да на странице подтверждения заказа')
    def confirm_order(self):
        self.click_element(OrderLocators.confirm)

    @allure.step('Проверить что заказ оформлен')
    def order_created(self):
        text = self.get_text(OrderLocators.order_created)
        return 'Заказ оформлен' in text

    def full_order_up_button(self, data):
        self.accept_cookies()
        self.click_up_order()
        self.fill_order_form(data)
        self.click_next()
        self.fill_info_about_order(data)
        self.click_final_order()
        self.confirm_order()

        
    def full_order_down_button(self, data):
        self.accept_cookies()
        self.click_down_order()
        self.fill_order_form(data)
        self.click_next()
        self.fill_info_about_order(data)
        self.click_final_order()
        self.confirm_order()
