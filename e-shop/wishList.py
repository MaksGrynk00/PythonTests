from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def verify_add_to_wishlist(url):
    """Verifies adding an item to the Wishlist on the given URL."""

    driver = webdriver.Chrome()  # Replace with  preferred WebDriver
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
        
    # Find and click "Add to wishlist" button
        add_to_wishlist_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//input[@type='button' and @value='Add to wishlist']")
            )
        )
        print("Click on Wishlist button")
        add_to_wishlist_button.click()

    except TimeoutException:
        print("Error: Could not find first product item.")
        return

    # Wait for success message
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".content"))
        )
        success_text = success_message.text
        if "wishlist" in success_text.lower():
            print("Success: Product added to wishlist.")
        else:
            print(f"Error: Unexpected success message: {success_text}")
    except TimeoutException:
        print("Error: Wishlist success message not found.")
   
    try:
     # Navigate to wishlist page

     # Click the "Wishlist" link in the page header
        wishlist_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                 (By.CSS_SELECTOR, ".ico-wishlist")
            )
        )
        wishlist_link.click()
    # Find product title in wishlist table
        wishlist_product_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "td.product a")
            )
        )
        wishlist_product_title_text = wishlist_product_title.text

    # Verify product titles match
        if product_title.lower() == wishlist_product_title_text.lower():
            print(f"Success: Product '{product_title}' found in wishlist.")
        else:
            print(
                    f"Error: Mismatch in product titles. Added: '{product_title}', Wishlist: '{wishlist_product_title_text}'"
            )
    except TimeoutException:
         print("Error: Could not find product in wishlist table.")
    except NoSuchElementException:
        print("Error: Could not find product title element in wishlist.")


    driver.quit()

if __name__ == "__main__":
    url = "https://demowebshop.tricentis.com/cell-phones"
    verify_add_to_wishlist(url)