import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("search_term", ["AI"])
def test_epam_search(browser, search_term):
    """Tests the search functionality on EPAM.com with a given search term."""
    browser.get("https://www.epam.com/about")

    # Find and click on 'Accept All' cookies button (modify if needed)
    accept_cookies_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
    )
    accept_cookies_button.click()

    # Find and click on the Search icon
    search_icon = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[@class='header-search__button header__icon']"))
    )
    search_icon.click()

    # Wait for the search input field to appear
    search_input = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='new_form_search']"))
    )
    # Type the search term in the search input field
    search_input.send_keys("AI")

    # Find the submit button using CSS selector (more reliable)
    submit_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='bth-text-layer']")
        )
    )
    # Click the "Find" button
    submit_button.click()

    # Find the search results counter element
    results_counter = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//h2[@class='search-results__counter']"))
    )

    # Verify the presence of search results counter
    assert results_counter.is_displayed(), "Search results counter not found"
    print(f"Search results found for '{search_term}': {results_counter.text}")

    browser.quit()