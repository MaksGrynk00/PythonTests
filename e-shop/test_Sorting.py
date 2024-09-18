import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_verify_sorting_options(browser):
    """Verifies sorting options on the given URL."""
    browser.get("https://demowebshop.tricentis.com/cell-phones")

    # Locate sorting dropdown
    sorting_dropdown = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "products-orderby"))
    )
    # Get all sorting options
    sorting_options = [opt.get_attribute("value") for opt in Select(sorting_dropdown).options]

    # Define indices for desired options (adjust as needed)
    second_option_index = 1
    fourth_option_index = 3

    # Assert number of sorting options is greater than both indices
    assert len(sorting_options) > second_option_index, "Insufficient sorting options"
    assert len(sorting_options) > fourth_option_index, "Insufficient sorting options"

    # Select the second option and verify URL change
    second_option = sorting_options[second_option_index]
    Select(sorting_dropdown).select_by_value(second_option)
    assert second_option in browser.current_url, f"URL does not reflect second option: {second_option}"

    # Re-find the sorting dropdown for the next selection
    sorting_dropdown = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "products-orderby"))
    )

    # Select the fourth option and verify URL change
    fourth_option = sorting_options[fourth_option_index]
    Select(sorting_dropdown).select_by_value(fourth_option)
    assert fourth_option in browser.current_url, f"URL does not reflect fourth option: {fourth_option}"

    print("Sorting options verified successfully.")