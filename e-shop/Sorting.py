from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def verify_sorting_options(url):
    """Verifies sorting options on the given URL."""

    driver = webdriver.Chrome()  # Replace with your preferred WebDriver
    driver.get(url)

    # Locate sorting dropdown
    sorting_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "products-orderby"))
    )

    # Get all sorting options
    sorting_options = [option.get_attribute("value") for option in Select(sorting_dropdown).options]

    # Select the second and fourth options (adjust indices as needed)
    second_option = sorting_options[1]
    fourth_option = sorting_options[3]

    # Select the second option and verify URL change
    Select(sorting_dropdown).select_by_value(second_option)
    WebDriverWait(driver, 10).until(
        EC.url_contains(second_option)  # Verify URL change
    )
    
    # Re-find the sorting dropdown for the next selection
    sorting_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "products-orderby"))
    )

    # Select the fourth option and verify URL change
    Select(sorting_dropdown).select_by_value(fourth_option)
    WebDriverWait(driver, 10).until(
        EC.url_contains(fourth_option)  # Verify URL change
    )

    print("Sorting options verified successfully.")

    driver.quit()

if __name__ == "__main__":
    url = "https://demowebshop.tricentis.com/desktops"
    verify_sorting_options(url)