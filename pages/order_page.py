from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.questions_locators import QuestionLocatorsPage
from locators.order_locators import OrderLocators
from selenium.webdriver.common.keys import Keys

class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(QuestionLocatorsPage.accept_cookies))
        element.click()

    def click_up_order(self):
        self.driver.find_element(*OrderLocators.order_up_button).click()

    def click_down_order(self):
        self.driver.find_element(*OrderLocators.order_down_button).click()

    def fill_order_form(self, data):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderLocators.name))
        self.driver.find_element(*OrderLocators.name).send_keys(data["name"])
        self.driver.find_element(*OrderLocators.surname).send_keys(data["surname"])
        self.driver.find_element(*OrderLocators.address).send_keys(data["address"])

        self.driver.find_element(*OrderLocators.subway_station).send_keys(data["subway"])
        station_option = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(OrderLocators.subway_station_by_name(data['subway'])))
        station_option.click()
    
        self.driver.find_element(*OrderLocators.phone).send_keys(data["phone"])


    def click_next(self):
        self.driver.find_element(*OrderLocators.next).click()

    def fill_info_about_order(self, data):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderLocators.when_to_deliver))
        self.driver.find_element(*OrderLocators.when_to_deliver).send_keys(data["when"])
        self.driver.find_element(*OrderLocators.when_to_deliver).send_keys(Keys.ESCAPE)
        self.driver.find_element(*OrderLocators.rental_period).click()
        self.driver.find_element(*OrderLocators.two_days).click()
        self.driver.find_element(*OrderLocators.color).click()


    def click_final_order(self):
        self.driver.find_element(*OrderLocators.final_order_button).click()


    def confirm_order(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderLocators.confirm))
        element.click()


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