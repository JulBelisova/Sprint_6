from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click_element(self, locator):
        self.find_element(locator).click()

    def get_text(self, locator):
        return self.find_element(locator).text
    
    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)
    
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)