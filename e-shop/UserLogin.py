from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def verify_login():
    """Verifies user login on demo webshop."""

    driver = webdriver.Chrome()
    driver.get("https://demowebshop.tricentis.com/login")

    # Verify login fields are present
    try:
        email_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='Email']"))
        )
        password_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='Password']"))
        )
    except TimeoutException:
        print("Error: Login fields not found.")
        driver.quit()
        return

    # Set login credentials 
    email_field.send_keys("bdkcjns@cdsjn.dd")
    password_field.send_keys("9Mb_SEjw@q$Ua")

    # Click login button
    login_button = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button")
    login_button.click()

    # Verify login successful
    try:
        # Check for logout link
        logout_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ico-logout"))
        )

        # Check for user email
        user_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".account"))
        )

        if logout_link.is_displayed() and user_email.text == "bdkcjns@cdsjn.dd":
            print("Login successful!")
        else:
            print("Error: Login verification failed.")
    except TimeoutException:
        print("Error: Login verification elements not found.")

    driver.quit()

if __name__ == "__main__":
    verify_login()