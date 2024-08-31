from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def check_policies():
    """Checks the availability of expected policies in the 'Policy' section on epam.com."""

    expected_policies = [
        "INVESTORS",
        "COOKIE POLICY",
        "OPEN SOURCE",
        "APPLICANT PRIVACY NOTICE",
        "PRIVACY POLICY",
        "WEB ACCESSIBILITY"
    ]

    driver = webdriver.Chrome()  # Replace with your preferred browser driver

    try:
        # Open epam.com
        driver.get("https://www.epam.com/about/")

        # Click the "Accept All" cookies button (modify if needed)
        accept_cookies_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
        )
        accept_cookies_button.click()

        # Wait for hamburger menu button and click
        #hamburger_button = WebDriverWait(driver, 50).until(
        #    EC.element_to_be_clickable((By.CSS_SELECTOR, ".hamburger-menu__button"))
        #)
        
        hamburger_button = driver.find_element(By.CSS_SELECTOR, ".hamburger-menu__button")
        hamburger_button.click()
        
        # Set the browser window size
        #driver.set_window_size(width=1380, height=820)

        # Locate the theme label element
        theme_label_D = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(@class,'theme-switcher-label body-text-small')][contains(text(),'Dark Mode')]"))
        )
        
        print("Theme label Dark Mode located")

        # Locate the toggle element
        toggle_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".theme-switcher"))
        )

        # Click the toggle element
        toggle_element.click()

        # Wait for the theme change (optional, depends on implementation)
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".theme-switcher-label.body-text-small"), "Light Mode")
        )

        # Verify theme change
        theme_label_L = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(@class,'theme-switcher-label body-text-small')][contains(text(),'Light Mode')]"))
        )
        if theme_label_L.is_displayed():
            print("Theme switched to Light Mode successfully!")
        else:
            print("Error: Theme switch failed.")


    except TimeoutException as e:
        print(f"Error: Timeout waiting for element. {e}")
    except NoSuchElementException as e:
        print(f"Error: Element not found. {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    check_policies()