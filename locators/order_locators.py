from selenium.webdriver.common.by import By 

class OrderLocators:
    #кнопка "Заказать" в верхнем меню:
    order_up_button = [By.XPATH, ".//div[@class = 'Header_Header__214zg']//button[@class = 'Button_Button__ra12g']"]
    #кнопка "Заказать" в нижнем меню:
    order_down_button = [By.XPATH, ".//div[@class = 'Home_FinishButton__1_cWm']//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"]
    #Для кого самокат:
    name = [By.XPATH, ".//input[@placeholder='* Имя']"]
    surname = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    address = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    subway_station = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    phone = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    #кнопка "Далее":
    next = [By.XPATH, ".//div[@class = 'Order_NextButton__1_rCA']//button"]
    #Про аренду:
    when_to_deliver = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]  
    rental_period = [By.XPATH, "//div[@class='Dropdown-control']"]
    two_days = [By.XPATH, "//*[text()='двое суток']"]
    color = [By.ID, 'black']
    final_order_button = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM'][text()='Заказать']"]
    confirm = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM'][text()='Да']"]
    order_created = [By.XPATH, "//*[text()='Заказ оформлен']"]


    @staticmethod
    def subway_station_by_name(station_name):
        return (By.XPATH, f"//*[contains(text(), '{station_name}')]")
    
