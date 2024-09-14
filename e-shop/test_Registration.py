import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string  # For generating random email address


def test_verify_registration(browser, first_name_length):
    """Verifies user registration on demo webshop."""
    browser.get("https://demowebshop.tricentis.com/register")

    # Generate random user data with varying first name length
    last_name = ''.join(random.choice(string.ascii_letters) for i in range(10))
    email = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10)) + '@example.com'
    password = "password123"  # Replace with a more complex password

    # Set values and submit form
    first_name_field = browser.find_element(By.XPATH, "//input[@id='FirstName']")
    first_name_field.send_keys(''.join(random.choice(string.ascii_letters) for i in range(first_name_length)))

    last_name_field = browser.find_element(By.XPATH, "//input[@id='LastName']")
    last_name_field.send_keys(last_name)

    email_field = browser.find_element(By.XPATH, "//input[@id='Email']")
    email_field.send_keys(email)

    password_field = browser.find_element(By.XPATH, "//input[@id='Password']")
    password_field.send_keys(password)

    confirm_password_field = browser.find_element(By.XPATH, "//input[@id='ConfirmPassword']")
    confirm_password_field.send_keys(password)

    register_button = browser.find_element(By.XPATH, "//input[@id='register-button']")
    register_button.click()

    # Verify registration successful
    success_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".result"))
    )

    # Assert successful registration message
    assert success_message.text == "Your registration completed", "Unexpected registration message"

    print(f"Registration successful")

    browser.quit()