import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

def test_check_title(browser, url1, expected_title="EPAM | Software Engineering & Product Development Services"):
    """Tests if the title of the provided URL matches the expected title."""
    browser.get(url1)
    actual_title = browser.title

    # Assert the actual title matches the expected title
    assert actual_title == expected_title, f"Title mismatch for {url1}. Expected: '{expected_title}', Actual: '{actual_title}'"
    print(f"Title for {url1} is correct: {actual_title}")