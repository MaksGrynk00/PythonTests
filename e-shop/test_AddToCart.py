import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


def test_verify_add_to_cart(browser):
    """Verifies adding an item to the shopping cart"""
    browser.get("https://demowebshop.tricentis.com/cell-phones")
    # Find first product item within grid
    first_product_item = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".product-grid .item-box .product-item"))
    )
    first_product_item.click()

    # Find product title within product-item
    product_title = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='product-name']//h1[@itemprop='name']"))
    ).text

    print(f"First product title: {product_title}")

    # Find and click "Add to Cart" button
    add_to_cart_button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, ".//input[@type='button' and @value='Add to cart']"))
    )
    add_to_cart_button.click()
    print("Click on Add to cart button")

    # Wait for success message
    success_message = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.XPATH, "//p[@class='content']"))  # Assuming success message is within this element
        )
    assert success_message is not None, "Success message element not found"
    print("Success: Product added to shopping cart.")

    # Navigate to shopping cart page
    cart_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Shopping cart']"))
    )
    cart_link.click()

    # Find product in shopping cart table
    cart_product_title = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='product-name']"))
    )
    cart_product_title_text = cart_product_title.text

    # Verify product titles match
    assert product_title.lower() == cart_product_title_text.lower(), (
        f"Mismatch in product titles. Added: '{product_title}', shopping cart: '{cart_product_title_text}'"
    )
    print("Success: Product found to shopping cart.")
    browser.quit()