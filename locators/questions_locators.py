from selenium.webdriver.common.by import By

class QuestionLocatorsPage:
    accept_cookies = [By.ID, 'rcc-confirm-button']
    logo = [By.XPATH, ".//div[@class ='Home_Header__iJKdX']"]
    question_1 = [By.ID, 'accordion__heading-0']
    answer_1 = [By.XPATH, ".//div[@class = 'accordion__panel'][@aria-labelledby = 'accordion__heading-0']//p"]
    question_2 = [By.ID, 'accordion__heading-1']
    answer_2 = [By.XPATH, ".//div[@class = 'accordion__panel'][@aria-labelledby = 'accordion__heading-1']//p"]
    question_3 = [By.ID, 'accordion__heading-2']
    answer_3 = [By.XPATH, ".//div[@class = 'accordion__panel'][@aria-labelledby = 'accordion__heading-2']//p"]
    question_4 = [By.ID, 'accordion__heading-3']
    answer_4 = [By.XPATH, ".//div[@class = 'accordion__panel'][@aria-labelledby = 'accordion__heading-3']//p"]
    question_5 = [By.ID, 'accordion__heading-4']
    answer_5 = [By.XPATH, ".//div[@class = 'accordion__panel'][@aria-labelledby = 'accordion__heading-4']//p"]
    question_6 = [By.ID, 'accordion__heading-5']
    answer_6 = [By.XPATH, ".//div[@class = 'accordion__panel'][@aria-labelledby = 'accordion__heading-5']//p"]
    question_7 = [By.ID, 'accordion__heading-6']
    answer_7 = [By.XPATH, ".//div[@class = 'accordion__panel'][@aria-labelledby = 'accordion__heading-6']//p"]
    question_8 = [By.ID, 'accordion__heading-7']
    answer_8 = [By.XPATH, ".//div[@class = 'accordion__panel'][@aria-labelledby = 'accordion__heading-7']//p"]


