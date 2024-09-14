import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_verify_login(browser):
    """Verifies user login on demo webshop."""
    browser.get("https://demowebshop.tricentis.com/login")
    # Verify login fields are present
    email_field = WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//input[@id='Email']"))
    )
    password_field = WebDriverWait(browser, 5).until(
      EC.presence_of_element_located((By.XPATH, "//input[@id='Password']"))
    )

    # Assert email field presence
    assert email_field is not None, "Email field not found"

    # Assert password field presence
    assert password_field is not None, "Password field not found"

    # Set login credentials
    email_field.send_keys("bdkcjns@cdsjn.dd")
    password_field.send_keys("9Mb_SEjw@q$Ua")

    # Click login button
    login_button = browser.find_element(By.CSS_SELECTOR, ".button-1.login-button")
    login_button.click()

    # Verify login successful
    logout_link = WebDriverWait(browser, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".ico-logout"))
    )
    user_email = WebDriverWait(browser, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".account"))
    )

    # Assert logout link is displayed
    assert logout_link.is_displayed(), "Logout link not found - Login unsuccessful"

    # Assert user email is correct
    assert user_email.text == "bdkcjns@cdsjn.dd", "Incorrect user email after login"

    print("Login successful!")

    browser.quit()