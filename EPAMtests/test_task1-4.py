import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("expected_policy", [
    "INVESTORS", "COOKIE POLICY", "OPEN SOURCE",
    "APPLICANT PRIVACY NOTICE", "PRIVACY POLICY", "WEB ACCESSIBILITY"])

def test_check_policy_availability(browser, expected_policy):
    """Verifies the presence of a specific policy on the epam.com 'Policy' section."""

    browser.get("https://www.epam.com")

    # Click the "Accept All" cookies button (modify timeout if needed)
    accept_cookies_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
    )
    time.sleep(3)
    accept_cookies_button.click()

    # Scroll to the bottom of the page
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the 'Policy' section to be present
    policy_section = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "policies"))
    )

    # Find all policy links within the section
    policy_links = policy_section.find_elements(By.CSS_SELECTOR, "ul.policies-left a.fat-links, ul.policies-right a.fat-links")

    # Assert the presence of the expected policy
    assert any(link.text == expected_policy for link in policy_links), f"Policy '{expected_policy}' not found on the page."
