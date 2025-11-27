import pytest
from data import *
from pages.order_page import *
from data import *

class TestCompleteOrder: 

    @allure.title('Проверка создания успешного заказа самоката, ' \
    'переход на страницу заказа по клику на кнопку "Заказать" в верхнем меню')
    @pytest.mark.parametrize("data_index", [0])  
    def test_order_via_up_button(self, driver, data_index):
        order_page = OrderPage(driver)
        data = VALID_ORDER_DATA[data_index] 
        order_page.full_order_up_button(data)

        assert order_page.order_created()
   
    @allure.title('Проверка создания успешного заказа самоката, ' \
    'переход на страницу заказа по клику на кнопку "Заказать" в нижней части страницы сайта')
    @pytest.mark.parametrize("data_index", [1])   
    def test_order_via_down_button(self, driver, data_index):
        order_page = OrderPage(driver)
        data = VALID_ORDER_DATA[data_index]  
        order_page.full_order_down_button(data)

        assert order_page.order_created()