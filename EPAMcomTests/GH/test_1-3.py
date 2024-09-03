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

    driver = webdriver.Chrome()  # Create a new Chrome session

    try:
        # Open EPAM.com
        driver.get("https://www.epam.com")

        # Try to dismiss the cookie banner
        try:
            # Wait for accept button and click
            wait = WebDriverWait(driver, 10)
            cookie_banner = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='onetrust-button-group']/button[@id='onetrust-accept-btn-handler']")))
            cookie_banner.click()
        except Exception:
            print("Cookie banner button not found or not clickable.")
            pass  # Continue script execution if banner not found or not clickable
            

        # Wait for hamburger menu button and click
        hamburger_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[@class='hamburger-menu__button']")))
        hamburger_button.click()

        # Wait for language button in menu and click (uncomment if needed)
        language_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//span[@class='location-selector__button-language' and contains(., '(EN)')]")))
        language_button.click()

        # Wait for Ukrainian language option and click (uncomment if needed)
        ukrainian_option = wait.until(EC.element_to_be_clickable((By.XPATH, ".//a[@class='mobile-location-selector__link' and @href='https://careers.epam.ua' and @lang='uk']")))
        ukrainian_option.click()

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