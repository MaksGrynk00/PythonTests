from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def test_epam_search():
    """Tests the search functionality on EPAM.com."""

    driver = webdriver.Chrome()  # Replace with your preferred browser driver

    try:
        # Open EPAM.com
        driver.get("https://www.epam.com/about")

        # Find and click on 'Accept All' cookies button (modify if needed)
        accept_cookies_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
        )
        accept_cookies_button.click()

        # Find and click on the Search icon using XPath
        search_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ".//button[@class='header-search__button header__icon']"))
        )
        search_icon.click()

        # Wait for the search input field to appear
        search_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "new_form_search"))
        )

        # Type "AI" in the search input field
        search_input.send_keys("")
        search_input.send_keys("AI")

        # Find the submit button using XPath (fixed the space issue)
        # submit_button = driver.find_element(By.XPATH, ".//button[contains(@class, 'custom-search-button') and contains(text(), 'Find')]")
        submit_button = driver.find_element(By.CSS_SELECTOR, ".custom-search-button.button-text.font-900.gradient-border-button.large-gradient-button.uppercase-text")

        # Click the "Find" button
        submit_button.click()

        # Find the search results counter element
        results_counter = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//h2[@class='search-results__counter']"))
        )

        # Verify the search results counter text
        if results_counter:
            print("Search results found successfully!")
        else:
            print("Error: No results.")

    except TimeoutException as e:
        print(f"Error: Timeout waiting for element. {e}")
    except NoSuchElementException as e:
        print(f"Error: Element not found. {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_epam_search()