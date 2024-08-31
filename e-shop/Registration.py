from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from random import randint  # For generating random names
import string  # For generating random email address
import random

def verify_registration():
    """Verifies user registration on demo webshop."""

    driver = webdriver.Chrome()  # Replace with your preferred WebDriver
    driver.get("https://demowebshop.tricentis.com/register")

    # Verify required fields are present
    required_fields = [
        "FirstName",
        "LastName",
        "Email",
        "Password",
        "ConfirmPassword",
    ]
    missing_fields = []
    for field in required_fields:
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, f"//input[@id='{field}']"))
            )
        except TimeoutException:
            missing_fields.append(field)

    if missing_fields:
        print(f"Error: Following required fields are missing: {', '.join(missing_fields)}")
        driver.quit()
        return

    # Generate random names
    first_name = ''.join(random.choice(string.ascii_letters) for i in range(10))
    last_name = ''.join(random.choice(string.ascii_letters) for i in range(10))

    # Generate random email
    email = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10)) + '@example.com'

    # Set values and submit form
    first_name_field = driver.find_element(By.XPATH, "//input[@id='FirstName']")
    first_name_field.send_keys(first_name)

    last_name_field = driver.find_element(By.XPATH, "//input[@id='LastName']")
    last_name_field.send_keys(last_name)

    email_field = driver.find_element(By.XPATH, "//input[@id='Email']")
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, "//input[@id='Password']")
    password_field.send_keys("password123")  # Replace with a more complex password

    confirm_password_field = driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']")
    confirm_password_field.send_keys("password123")

    register_button = driver.find_element(By.XPATH, "//input[@id='register-button']")
    register_button.click()

    # Verify registration successful
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".result"))
        )
        if success_message.text == "Your registration completed":
            print("Registration successful!")
        else:
            print("Error: Unexpected registration message.")
    except TimeoutException:
        print("Error: Registration message not found.")

    driver.quit()

if __name__ == "__main__":
    verify_registration()