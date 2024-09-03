from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def verify_remove_from_cart(url):
    """Verifies adding an item to the shopping cart"""

    driver = webdriver.Chrome()  
    driver.get(url)

    # Find first product item within grid
    try:
        first_product_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".product-grid .item-box .product-item")
            )
        )
        first_product_item.click()

    # Find product title within product-item
        product_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-name']//h1[@itemprop='name']"))
        )
        product_title = product_title.text

        print(f"First product title: {product_title}")
        
    # Find and click "Add to Cart" button
        add_to_cart_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//input[@type='button' and @value='Add to cart']")
            )
        )
        print("Click on Add to cart button")
        add_to_cart_button.click()

    except TimeoutException:
        print("Error: Could not find first product item.")
        return

    # Wait for success message
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".content")) #:contains('shopping cart')
        )
        success_text = success_message.text

        print("Success: Product added to shopping cart.")
        
    except TimeoutException:
        print("Error: Add to cart success message not found.")
   
    try:
     # Navigate to shopping cart page
     # Click the "shopping cart" link in the page header
        cart_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                 (By.CSS_SELECTOR, ".ico-cart")
            )
        )
        cart_link.click()
    # Find product in shopping cart table
        cart_product_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "td.product a.product-name")
            )
        )

            
    # Find "Remove" checkbox for the product
        remove_checkbox = driver.find_element(By.NAME, "removefromcart")
        print("Remove check-box found in cart table.")

        remove_checkbox.click()

    # Find and click "Update shopping cart" button
        update_cart_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='updatecart']"))
        )
        update_cart_button.click()            
            
        empty_cart_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".order-summary-content"))
        )
        empty_cart_text = empty_cart_message.text
        if "empty" in empty_cart_text.lower():
            print(f"Success: Product '{product_title}' removed from cart.")
        else:
            print(f"Error: Product '{product_title}' might not be removed completely.")
        
    except TimeoutException:
         print("Error: Could not find product in shopping cart table.")
    except NoSuchElementException:
        print("Error: Could not find product title element in shopping cart.")


    driver.quit()

if __name__ == "__main__":
    url = "https://demowebshop.tricentis.com/cell-phones"
    verify_remove_from_cart(url)