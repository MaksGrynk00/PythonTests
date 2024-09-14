import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_verify_add_to_whitelist(browser):
    """Verifies adding an item to the Wishlist on the given URL."""
    browser.get("https://demowebshop.tricentis.com/cell-phones")

    # Find first product item within grid
    first_product_item = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-grid .item-box .product-item")
        )
    )
    first_product_item.click()

    # Find product title within product-item
    product_title = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='product-name']//h1[@itemprop='name']"))
    )
    product_title = product_title.text

    print(f"First product title: {product_title}")

    # Find and click "Add to wishlist" button
    add_to_wishlist_button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, ".//input[@type='button' and @value='Add to wishlist']")
        )
    )
    print("Click on Wishlist button")
    add_to_wishlist_button.click()

    # Wait for success message
    success_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".content"))
    )
    success_text = success_message.text

    # Assert presence of "wishlist" (ignoring case) in success message
    assert "wishlist" in success_text.lower(), "Success message does not contain 'wishlist'"

    print("Success: Product added to wishlist.")

    # **Optional: Navigate to wishlist page and verify product**
    # Assuming wishlist navigation functionality is available, uncomment these sections:

    # wishlist_link = WebDriverWait(browser, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, ".ico-wishlist"))
    # )
    # wishlist_link.click()

    # wishlist_product_title = WebDriverWait(browser, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "td.product a"))
    # )
    # wishlist_product_title_text = wishlist_product_title.text

    # assert product_title.lower() == wishlist_product_title_text.lower(), (
    #     f"Mismatch in product titles. Added: '{product_title}', Wishlist: '{wishlist_product_title_text}'"
    # )
    # print(f"Success: Product '{product_title}' found in wishlist.")

    browser.quit()