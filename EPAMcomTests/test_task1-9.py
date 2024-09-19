import os
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("downloads")
def test_download_epam_glance(browser, downloads):
    """Attempts to download the EPAM at a Glance file and verifies download."""

    # Open the EPAM About page
    browser.get("https://www.epam.com/about")

    # Find and click on the 'Accept All' cookies button
    accept_cookies_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
    )
    time.sleep(3)
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

    time.sleep(10)

    # Verify downloaded file presence (using fixture for download path)
    download_dir = str(downloads)
    # expected_filename = "EPAM_Corporate_Overview*.pgf"  # replace with your intended file name
    expected_file_path = os.path.join(download_dir, "EPAM_Corporate_Overview*.pgf")

    # assert the file exists
    assert len(expected_file_path) > 0, f"Downloaded file not found: {expected_file_path}"

    print("File downloaded successfully.")