from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_verify_remove_from_cart(browser):
    """Verifies removing an item from the shopping cart."""
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
    ).text


    # Find and click "Add to Cart" button
    add_to_cart_button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, ".//input[@type='button' and @value='Add to cart']")
        )
    )

    add_to_cart_button.click()

    # Assert success message
    success_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".content"))
    )
    assert "shopping cart" in success_message.text, "Success message doesn't contain 'shopping cart'"


    # Navigate to shopping cart page
    cart_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ico-cart"))
    )
    cart_link.click()

    # Find product in shopping cart table
    cart_product_title = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "td.product a.product-name"))
    )

    assert cart_product_title.text == product_title, "Product title in cart doesn't match"

    # Find "Remove" checkbox for the product
    remove_checkbox = browser.find_element(By.NAME, "removefromcart")

    remove_checkbox.click()

    # Find and click "Update shopping cart" button
    update_cart_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='updatecart']"))
    )
    update_cart_button.click()

    empty_cart_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".order-summary-content"))
    )
    empty_cart_text = empty_cart_message.text

    assert "empty" in empty_cart_text.lower(), f"Product '{product_title}' might not be removed"

