import pytest
from selenium import webdriver
from data import *
from locators.order_locators import OrderLocators
from pages.order_page import *
from data import *

class TestCompleteOrder: 

    @pytest.mark.parametrize("data_index", [0])  
    def test_order_via_up_button(self, driver, data_index):
        order_page = OrderPage(driver)
        data = VALID_ORDER_DATA[data_index] 
        order_page.full_order_up_button(data)

        element = driver.find_element(*OrderLocators.order_created).text
        assert 'Заказ оформлен' in element

    @pytest.mark.parametrize("data_index", [1])   
    def test_order_via_down_button(self, driver, data_index):
        order_page = OrderPage(driver)
        data = VALID_ORDER_DATA[data_index]  
        order_page.full_order_down_button(data)

        element = driver.find_element(*OrderLocators.order_created).text
        assert 'Заказ оформлен' in element