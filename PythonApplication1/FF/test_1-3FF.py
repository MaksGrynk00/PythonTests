from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains  # For scrolling (optional)
import time

def test_change_language_to_ukrainian():
    """Tests the ability to change the language to Ukrainian on EPAM.com.

    This script opens EPAM.com, opens the language menu, clicks on Ukrainian,
    and verifies it forwards to the Ukrainian careers page.
    """

    driver = webdriver.Firefox()  # Use Firefox

    try:
        # Open epam.com
        driver.get("https://www.epam.com/about/")

        # Click the "Accept All" cookies button (modify if needed)
        accept_cookies_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
        )
        accept_cookies_button.click() 

        # Wait for language button in menu and click (uncomment if needed)
        language_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "location-selector__button"))
        )
        language_button.click()
        print("Language click")

        # Wait for Ukrainian language option and click (uncomment if needed)
        ukrainian_option = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, ".//a[@class='location-selector__link' and @href='https://careers.epam.ua' and @lang='uk']"))
        )
        ukrainian_option.click()
        print("Ukraine!!")

        # Verify we're on the Ukrainian careers page (uncomment if needed)
        expected_url = "https://careers.epam.ua/"
        current_url = driver.current_url

        if expected_url == current_url:
            print("Language successfully changed to Ukrainian!")
        else:
            print("Language change failed. Expected URL:", expected_url, "Actual URL:", current_url)

    except Exception as e:
        print("Error occurred:", e)
    finally:
        driver.quit()  # Always close the browser window

if __name__ == "__main__":
    test_change_language_to_ukrainian()