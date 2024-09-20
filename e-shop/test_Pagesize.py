from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_verify_items_per_page(browser):
    """Verifies changing the number of items per page on the given URL."""
    browser.get("https://demowebshop.tricentis.com/desktops")

    # Locate items per page dropdown
    items_per_page_dropdown = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "products-pagesize"))
    )
    # Initial count with default page size
    initial_grid_elements = len(
        browser.find_elements(By.CSS_SELECTOR, ".product-grid > .item-box")
    )

    # Assert initial grid element count is greater than zero
    assert initial_grid_elements > 0, "No product items found in the grid."

    # Select option for 4 items per page
    select_dropdown = Select(items_per_page_dropdown)
    select_dropdown.select_by_value("https://demowebshop.tricentis.com/desktops?pagesize=4")  # Select by value directly

    # Wait for URL update with "pagesize=4"
    WebDriverWait(browser, 10).until(EC.url_contains("pagesize=4"))

    # Count elements after changing page size
    post_change_elements = len(
        browser.find_elements(By.CSS_SELECTOR, ".product-grid > .item-box")
    )

    # Assert 4 items are displayed after changing page size
    assert post_change_elements == 4, f"Expected 4 items, found {post_change_elements}"