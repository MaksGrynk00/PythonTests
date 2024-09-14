import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("get_download_dir")
def test_download_epam_glance(browser, get_download_dir):
  """Attempts to download the EPAM at a Glance file and verifies download."""

  # Open the EPAM About page
  browser.get("https://www.epam.com/about")

  # Find and click on the 'Accept All' cookies button
  accept_cookies_button = WebDriverWait(browser, 10).until(
      EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
  )
  accept_cookies_button.click()

  # Scroll to a specific position within the page (adjust as needed)
  scroll_position = 2000  # Adjust this value based on your observations
  browser.execute_script(f"window.scrollTo(0, {scroll_position});")

  # Find the "Download" button within the "EPAM at a Glance" block
  download_button = WebDriverWait(browser, 10).until(
      EC.presence_of_element_located(
          (By.XPATH, ".//span[@class='button__inner']//span[contains(text(), 'DOWNLOAD')]")
      )
  )

  # Click the "Download" button
  download_button.click()

  # Verify downloaded file presence (using fixture for download path)
  download_path = get_download_dir
  expected_filename = "EPAM_Corporate_Overview_Q4_EOY.pdf"
  expected_file_path = os.path.join(download_path, expected_filename)

  assert os.path.exists(expected_file_path), f"Downloaded file not found: {expected_filename}"
  print("File downloaded successfully.")

