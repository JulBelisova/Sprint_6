from selenium import webdriver
from data import *
from locators.questions_locators import QuestionLocatorsPage
from pages.questions_page import *


class TestQuestions:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_question_1(self, driver):
        question_page = QuestionsPage(driver)

        text = question_page.check_the_answer(1)
        element = driver.find_element(*QuestionLocatorsPage.question_1)
        assert element.get_attribute("aria-expanded") == "true"
        assert (
            text == q1_expected_answer
        ), f"Ожидался: '{q1_expected_answer}', но получили: '{text}'"

    def test_question_2(self, driver):
        question_page = QuestionsPage(driver)

        text = question_page.check_the_answer(2)
        element = driver.find_element(*QuestionLocatorsPage.question_2)
        assert element.get_attribute("aria-expanded") == "true"
        assert text == q2_expected_answer, f"получили: '{text}'"

    def test_question_3(self, driver):
        question_page = QuestionsPage(driver)

        text = question_page.check_the_answer(3)
        element = driver.find_element(*QuestionLocatorsPage.question_3)
        assert element.get_attribute("aria-expanded") == "true"
        assert text == q3_expected_answer, f"получили: '{text}'"

    def test_question_4(self, driver):
        question_page = QuestionsPage(driver)

        text = question_page.check_the_answer(4)
        element = driver.find_element(*QuestionLocatorsPage.question_4)
        assert element.get_attribute("aria-expanded") == "true"
        assert text == q4_expected_answer, f"получили: '{text}'"

    def test_question_5(self, driver):
        question_page = QuestionsPage(driver)

        text = question_page.check_the_answer(5)
        element = driver.find_element(*QuestionLocatorsPage.question_5)
        assert element.get_attribute("aria-expanded") == "true"
        assert text == q5_expected_answer, f"получили: '{text}'"

    def test_question_6(self, driver):
        question_page = QuestionsPage(driver)

        text = question_page.check_the_answer(6)
        element = driver.find_element(*QuestionLocatorsPage.question_6)
        assert element.get_attribute("aria-expanded") == "true"
        assert text == q6_expected_answer, f"получили: '{text}'"

    def test_question_7(self, driver):
        question_page = QuestionsPage(driver)

        text = question_page.check_the_answer(7)
        element = driver.find_element(*QuestionLocatorsPage.question_7)
        assert element.get_attribute("aria-expanded") == "true"
        assert text == q7_expected_answer, f"получили: '{text}'"

    def test_question_8(self, driver):
        question_page = QuestionsPage(driver)

        text = question_page.check_the_answer(8)
        element = driver.find_element(*QuestionLocatorsPage.question_8)
        assert element.get_attribute("aria-expanded") == "true"
        assert text == q8_expected_answer, f"получили: '{text}'"
