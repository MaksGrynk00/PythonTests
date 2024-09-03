from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def check_company_logo():
    """Checks if clicking the company logo leads to the main page."""

    driver = webdriver.Chrome()  # Replace with your preferred browser driver

    try:
        # Open the EPAM About page
        driver.get("https://www.epam.com/about")

        # Find and click on the 'Accept All' cookies button (modify if needed)
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
        )
        accept_cookies_button.click()

        # Find the company logo link
        logo_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header__logo-container a"))
        )

        # Get the current URL
        current_url = driver.current_url

        # Click on the company logo link
        logo_link.click()

        # Wait for the page to load and verify the URL
        WebDriverWait(driver, 10).until(EC.url_to_be("https://www.epam.com/"))

        # Verify that the expected URL is loaded
        if driver.current_url == "https://www.epam.com/":
            print("Success! Clicking the company logo leads to the main page.")
        else:
            print(f"Error: Expected URL 'https://www.epam.com/' but got {driver.current_url}")

    except TimeoutException as e:
        print(f"Error: Timeout waiting for element. {e}")
    except NoSuchElementException as e:
        print(f"Error: Element not found. {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    check_company_logo()