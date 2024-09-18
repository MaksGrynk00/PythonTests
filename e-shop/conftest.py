import pytest
from selenium import webdriver


# set length for field

@pytest.fixture()
def first_name_length():
    return 10


# Setup Chrome/Firefox

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    yield driver
