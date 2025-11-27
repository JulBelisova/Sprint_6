import pytest
from selenium import webdriver
from data import *
from locators.questions_locators import QuestionLocatorsPage
from pages.questions_page import *


class TestQuestions:
    @pytest.mark.parametrize("question_number, expected_answer", [    
        (1, q1_expected_answer),
        (2, q2_expected_answer), 
        (3, q3_expected_answer),
        (4, q4_expected_answer),
        (5, q5_expected_answer),
        (6, q6_expected_answer),
        (7, q7_expected_answer),
        (8, q8_expected_answer)])

    @allure.title('Проверка раскрытия и наличия ответа на вопрос при клике на сам вопрос')
    def test_question(self, driver, question_number, expected_answer):
        question_page = QuestionsPage(driver)
        text = question_page.check_the_answer(question_number)
        locator = getattr(QuestionLocatorsPage, f'question_{question_number}')
        is_expanded = question_page.get_attribute(locator, "aria-expanded")
        assert is_expanded == "true"
        assert (text == expected_answer), f"Ожидался: '{expected_answer}', но получили: '{text}'"


