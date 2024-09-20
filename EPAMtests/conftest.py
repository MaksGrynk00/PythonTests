import pytest
from selenium import webdriver

# Setup Chrome/Firefox
@pytest.fixture()
def browser():
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.set_window_size(1200, 800)
    yield driver
    driver.quit()

# URL for tests
@pytest.fixture(params=["https://www.epam.com"])
def url1(request):
    return request.param

# test1-4
@pytest.fixture(scope="function")
def expected_policy(request):
    return request.param

# test1-5
@pytest.fixture(scope="function")
def region(request):
    return request.param

# test1-6
@pytest.fixture(scope="function")
def search_term(request):
    return request.param

# test1-9
@pytest.fixture()
def downloads():
    download_dir = 'C:\\Users\\Maksym_Grynkiv\\Downloads'
    return download_dir