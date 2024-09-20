import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_change_language_to_ukrainian(browser):
    """Tests the ability to change the language to Ukrainian on EPAM.com."""

    browser.get("https://www.epam.com/about")
    # Click the "Accept All" cookies button (modify if needed)
    accept_cookies_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
    )
    time.sleep(3)
    accept_cookies_button.click()

    # Locate and click the language button
    language_button_locator = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='location-selector__button']"))
    )
    language_button_locator.click()

    # Locate Ukrainian language option
    ukrainian_option = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='location-selector__link'][contains(text(),'Україна')]"))
    )
    ukrainian_option.click()

    #Verify URL after clicking Ukrainian option
    expected_url = "https://careers.epam.ua/"
    assert browser.current_url == expected_url, f"Language change failed. Expected URL: {expected_url}"
