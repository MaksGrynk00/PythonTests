import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

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
def expected_policy(request):
    return request.param

# Fixture to provide download directory path
@pytest.fixture
def get_download_dir():
  return os.path.join(os.environ["USERPROFILE"], "Downloads")