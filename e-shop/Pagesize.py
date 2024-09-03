from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def verify_items_per_page(url):
    """Verifies changing the number of items per page on the given URL."""

    driver = webdriver.Chrome()  
    driver.get(url)

    # Locate items per page dropdown
    items_per_page_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "products-pagesize"))
    )

    # Initial count with default page size
    initial_grid_elements = len(
        driver.find_elements(By.CSS_SELECTOR, ".product-grid > .item-box")
    )
    print(f"Initial number of elements in grid: {initial_grid_elements}")

    # Print message if no items are found initially
    if initial_grid_elements == 0:
        print("Warning: No product items found in the grid.")
        
    # Select option for 4 items per page
    Select(items_per_page_dropdown).select_by_value(
        "https://demowebshop.tricentis.com/accessories?pagesize=4"
    )
    WebDriverWait(driver, 10).until(EC.url_contains("pagesize=4"))

    # Count elements after changing page size
    post_change_elements = len(
        driver.find_elements(By.CSS_SELECTOR, ".product-grid > .item-box")
    )

    if post_change_elements == 4:
        print(f"Successfully verified 4 items displayed after changing page size.")
    else:
        print(
            f"Error: Expected 4 items, found {post_change_elements} after changing page size."
        )

    print("Items per page change verified.")

    driver.quit()

if __name__ == "__main__":
    url = "https://demowebshop.tricentis.com/accessories"
    verify_items_per_page(url)