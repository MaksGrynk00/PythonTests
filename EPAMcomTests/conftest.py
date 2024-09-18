import pytest
import os
import shutil
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

# Define the path where the downloads are stored
DOWNLOAD_DIR = "/path/to/your/download/directory"

@pytest.fixture(scope='function')
def get_download_dir():
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    yield
    shutil.rmtree(DOWNLOAD_DIR)

# Fixture to provide download directory path
@pytest.fixture
def get_download_dir():
  return os.path.join(os.environ["USERPROFILE"], "Downloads")