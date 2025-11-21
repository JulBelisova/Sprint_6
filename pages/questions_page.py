from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.questions_locators import QuestionLocatorsPage

class QuestionsPage:
    
    def __init__(self, driver): 
        self.driver = driver 

    def find_question(self, question_number):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(QuestionLocatorsPage.logo))
        locator = getattr(QuestionLocatorsPage, f'question_{question_number}')
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_question(self, question_number):
        locator = getattr(QuestionLocatorsPage, f'question_{question_number}')
        self.driver.find_element(*locator).click()

    def get_text(self, question_number):
        locator = getattr(QuestionLocatorsPage, f'answer_{question_number}')
        #return self.driver.find_element(*locator).text
        #locator = getattr(QuestionLocatorsPage, f'answer_{question_number}')
        element = self.driver.find_element(*locator)
        return element.get_attribute("textContent")


    def check_the_answer(self, question_number):
        self.find_question(question_number)
        self.click_question(question_number)
        return self.get_text(question_number)       