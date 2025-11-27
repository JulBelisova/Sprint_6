import allure
from locators.questions_locators import QuestionLocatorsPage
from .base_page import BasePage

class QuestionsPage(BasePage):
    
    def __init__(self, driver): 
        super().__init__(driver) 
    
    @allure.step('Прокруть вниз до нужного вопроса')
    def find_question(self, question_number):
        locator = getattr(QuestionLocatorsPage, f'question_{question_number}')
        self.scroll_to_element(locator)

    @allure.step('Принять куки')
    def accept_cookies(self):
        self.click_element(QuestionLocatorsPage.accept_cookies)

    @allure.step('Кликнуть на вопрос для появления ответа на него')
    def click_question(self, question_number):
        locator = getattr(QuestionLocatorsPage, f'question_{question_number}')
        self.click_element(locator)

    @allure.step('Получить текст ответа')
    def get_answer_text(self, question_number):
        locator = getattr(QuestionLocatorsPage, f'answer_{question_number}')
        return self.get_attribute(locator, "textContent")

    @allure.step("Проверить ответ на вопрос №{question_number}")
    def check_the_answer(self, question_number):
        self.find_question(question_number)
        self.accept_cookies()
        self.click_question(question_number)
        return self.get_answer_text(question_number)       