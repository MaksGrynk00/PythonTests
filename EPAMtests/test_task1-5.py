import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("region", ["EMEA", "APAC"])
def test_check_location_switching(browser, region):
    """Verifies location switching by region on epam.com."""

    regions = {
        "EMEA": "Austria",
        "APAC": "India",
    }

    browser.get("https://www.epam.com/about")

    # Click the "Accept All" cookies button (modify if needed)
    accept_cookies_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
    )
    time.sleep(3)
    accept_cookies_button.click()

    # Scroll to a specific position within the page (optional)
    # You might not need this depending on element visibility
    scroll_position = 8500  # Adjust this value based on your observations
    browser.execute_script("window.scrollTo(0, {});".format(scroll_position))

    # Locate the initial "Not displayed" element based on the region "APAC": "India"
    not_displayed_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//div[@class='locations-viewer-23__country-title list' and text()='{regions[region]}']")
        )
    )

    # Assert the initial "Not displayed" element is not visible
    assert not not_displayed_element.is_displayed(), (
        f"{regions[region]} element should initially be hidden."
    )

    # Find the desired region link APAC
    region_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//a[@role='tab' and text()='{region}']"))
    )

    # Click the region link
    region_link.click()

    # Locate the element that should be displayed after switching
    displayed_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//div[@class='locations-viewer-23__country-title list' and text()='{regions[region]}']")
        )
    )

    # Assert the element is displayed after switching
    assert displayed_element.is_displayed(), f"{regions[region]} element not found after switching."