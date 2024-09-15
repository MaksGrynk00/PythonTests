import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="session")
def first_name_length():
    return 10

# Setup Chrome/Firefox
@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    yield driver
    driver.quit()
