import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_company_logo(browser):
    """Checks if clicking the company logo leads to the main page."""

    # Open the EPAM About page
    browser.get("https://www.epam.com/about")

    # Find and click on the 'Accept All' cookies button (modify if needed)
    accept_cookies_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
    )
    accept_cookies_button.click()

    # Find the company logo link
    logo_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".header__logo-container a"))
    )

    # Click on the company logo link
    logo_link.click()

    # Wait for the page to load and verify the URL
    WebDriverWait(browser, 10).until(EC.url_to_be("https://www.epam.com/"))

    # Verify that the expected URL is loaded
    assert browser.current_url == "https://www.epam.com/", f"Error: Expected URL 'https://www.epam.com/' but got {browser.current_url}"
    print("Success! Clicking the company logo leads to the main page.")

    browser.quit()