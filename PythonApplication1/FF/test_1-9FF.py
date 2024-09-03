from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os

def download_epam_glance():
  """Attempts to download the EPAM at a Glance file and checks for download popups."""

  driver = webdriver.Firefox()  # Use Firefox 

  try:
    # Open the EPAM About page
    driver.get("https://www.epam.com/about")

    # Find and click on the 'Accept All' cookies button
    accept_cookies_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
    )
    accept_cookies_button.click()
    
    # Scroll to a specific position within the page (adjust as needed)
    scroll_position = 2000  # Adjust this value based on your observations
    driver.execute_script("window.scrollTo(0, {});".format(scroll_position))

    # Find the "Download" button within the "EPAM at a Glance" block
    download_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, ".//span[@class='button__inner']//span[contains(text(), 'DOWNLOAD')]")
        )
    )

    # Click the "Download" button
    download_button.click()

    # Simulate a short wait to allow download initiation (optional)
    driver.implicitly_wait(5)


    # Check for the downloaded file
    download_path = "c:\\Users\\Maksym_Grynkiv\\Downloads\\"
    expected_filename = "EPAM_Corporate_Overview_Q4_EOY.pdf"

    file_path = os.path.join(download_path, expected_filename)
    if os.path.exists(file_path):
        print("File downloaded successfully.")
    else:
        print("Error: Downloaded file not found.")    

  except TimeoutException as e:
    print(f"Error: Timeout waiting for element. {e}")
  except NoSuchElementException as e:
    print(f"Error: Element not found. {e}")
  except Exception as e:
    print(f"Unexpected error: {e}")
  finally:
    driver.quit()

if __name__ == "__main__":
  download_epam_glance()