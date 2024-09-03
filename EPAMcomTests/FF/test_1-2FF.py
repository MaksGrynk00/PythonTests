from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def check_theme_switcher():
  """Check the ability to switch Light / Dark mode."""

  driver = webdriver.Firefox()  # Use Firefox

  try:
    # Open epam.com
    driver.get("https://www.epam.com/about/")

    # Click the "Accept All" cookies button (modify if needed)
    accept_cookies_button = WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
    )
    accept_cookies_button.click()

    # Locate the toggle element using the defined selector
    #switcher_tog = driver.find_element(By.CSS_SELECTOR, ".theme-switcher-ui .theme-switcher :last-child")
    switcher_tog = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'switch'))
    )

    print("switch element found")

    # Click the toggle element

    driver.execute_script("arguments[0].click();",switcher_tog)

    print("Theme switched click")

  except TimeoutException as e:
    print(f"Error: Timeout waiting for element. {e}")
  except NoSuchElementException as e:
    print(f"Error: Element not found. {e}")
  finally:
    driver.quit()

if __name__ == "__main__":
  check_theme_switcher()