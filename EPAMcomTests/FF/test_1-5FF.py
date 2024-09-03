from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def check_location_switching():
    """Checks that location switching by region works on epam.com."""

    regions = ["AMERICAS", "EMEA", "APAC"]

    driver = webdriver.Firefox()  # Use Firefox

    try:
        # Open the EPAM About page
        driver.get("https://www.epam.com/about")

        # Find and click on the 'Accept All' cookies button
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
        
        # EMEA area
        # Check if the "Austria" element is initially not displayed
        austria_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='locations-viewer-23__country-title list' and text()='Austria']"))
        )
        print("Austria element is initially not displayed.")

        # Find the EMEA region link

        emea_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@role='tab' and text()='EMEA']"))
        )
        print("emea_link located")
        
        driver.implicitly_wait(10) # 20 seconds wait
        
        # Click the EMEA link
        emea_link.click()
        
        driver.implicitly_wait(10) # 10 seconds wait

        print("emea located and clicked")
        
        # Locate the Austria element on page
        austria_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='locations-viewer-23__country-title list' and text()='Austria']"))
        )      
        # Verify if the "Austria" element is displayed

        print("Austria element is displayed successfully.")
        
        # Find the APAC region link
        apac_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@role='tab' and text()='APAC']"))
        )
        # Click the EMEA link
        apac_link.click()
        
        print("APAC located and clicked")
        
        # Locate the India element on page
        india_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='locations-viewer-23__country-title list' and text()='India']"))
        )
        
        # Verify if the "India" element is displayed
        if india_element.is_displayed():
            print("India element is displayed successfully.")
        else:
            print("Error: India element not found.")
        
    except TimeoutException as e:
        print(f"Error: Timeout waiting for element. {e}")
    except NoSuchElementException as e:
        print(f"Error: Element not found. {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    check_location_switching()