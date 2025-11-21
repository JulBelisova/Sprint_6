import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from url import *



@pytest.fixture(scope='function')
def driver():
    options = Options()
    service = Service()
    browser = webdriver.Firefox(options=options, service=service)
    browser.get(main_site)
    yield browser
    browser.quit()