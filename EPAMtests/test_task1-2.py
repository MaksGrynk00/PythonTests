import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_check_theme_switch(browser):
    """Verifies the ability to switch theme on epam.com."""
    browser.get("https://www.epam.com/about/")

    # Click the "Accept All" cookies button (modify if needed)
    accept_cookies_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
    )
    time.sleep(3)
    accept_cookies_button.click()

    # Verify initial theme based on the parameter
    theme_label = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "dark-mode" )
        )
    )
    # Assert theme and print the result
    assert theme_label.is_displayed(), "Initial theme mismatch. Expected: Dark Mode"

    # Locate the toggle element
    toggle_element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='header__vaulting-container']//div[@class='theme-switcher']"))
    )

    # Click the toggle element
    toggle_element.click()

    # Verify theme change after clicking the toggle fonts-loaded light-mode
    new_theme_label_locator = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "light-mode" )
        )
    )

    assert new_theme_label_locator.is_displayed(), f"Theme switch not switched. "
