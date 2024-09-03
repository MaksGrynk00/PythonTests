from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def verify_checkout(url):
    """Verifies adding an item to the shopping cart and completing checkout"""

    driver = webdriver.Chrome()  # Replace with your preferred WebDriver
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
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='product-name']//h1[@itemprop='name']")
            )
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
            EC.presence_of_element_located((By.CSS_SELECTOR, ".content"))
        )
        success_text = success_message.text
        print("Success: Product added to shopping cart.")

    except TimeoutException:
        print("Error: Add to cart success message not found.")

    try:
        # Navigate to shopping cart page
        # Click the "shopping cart" link in the page header
        cart_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ico-cart"))
        )
        cart_link.click()

        # Find product in shopping cart table
        cart_product_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "td.product a.product-name")
            )
        )
        print("Product in shopping cart")

        # Agree with the terms of service
        termsofservice = driver.find_element(By.NAME, "termsofservice")
        termsofservice.click()

        # Find "Checkout" button
        checkout_button = driver.find_element(By.NAME, "checkout")
        checkout_button.click()

        # Find and click "Checkout as Guest" button (if applicable)
        checkout_as_guest = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//input[@type='button' and @value='Checkout as Guest']")
            )
        )
        checkout_as_guest.click()
        
        # Find Billing Address fields:
        first_name = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.ID, "BillingNewAddress_FirstName")
            )
        )
        first_name.send_keys("first_name")

        last_name = driver.find_element(By.ID, "BillingNewAddress_LastName")
        last_name.send_keys("last_name")

        email = driver.find_element(By.ID, "BillingNewAddress_Email")
        email.send_keys("bdkcjns@cdsjn.dd")

        city = driver.find_element(By.ID, "BillingNewAddress_City")
        city.send_keys("New York")

        address1 = driver.find_element(By.ID, "BillingNewAddress_Address1")
        address1.send_keys("Address1")

        address2 = driver.find_element(By.ID, "BillingNewAddress_Address2")
        address2.send_keys("Address2")

        zip_code = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        zip_code.send_keys("1234567")

        phone_number = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")
        phone_number.send_keys("112112121111")
        
        print("All billing address data set")

        # Locate Country dropdown
        country_dropdown = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.ID, "BillingNewAddress_CountryId")
            )
        )
        print("country select located")
        country_options = [option.get_attribute("value") for option in Select(country_dropdown).options]

        # Set the US country option
        us_country_option = country_options[2]

        # Select US country option
        Select(country_dropdown).select_by_value(us_country_option) #select.select_by_value(value)
        
        print("Country set")

        # Click button Continue
        bill_continue_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//input[@onclick='Billing.save()']")
            )
        )
        bill_continue_button.click()
        
        print("bill_continue_button")
        
        driver.implicitly_wait(15) # seconds
      
        # Navigate to Shipping addres 

        shipping_continue_button = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//input[@onclick='Shipping.save()']")
            )
        )
        shipping_continue_button.click()
        
        
        
        print("Shipping addres")
        
        # Shipping method Continue
        shipping_method_button = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//input[@onclick='ShippingMethod.save()']")
            )
        )
        shipping_method_button.click()
        
        # Payment method Continue
        payment_method_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//input[@onclick='PaymentMethod.save()']")
            )
        )
        payment_method_button.click()
        
        print("Payment method Continue")
        
        # Payment information Continue
        payment_info_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//input[@onclick='PaymentInfo.save()']")
            )
        )
        payment_info_button.click()
        
        print("payment_info_button")
        
        driver.implicitly_wait(10) # seconds
        
        # Order Confirmation
        confirmation_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//input[@onclick='ConfirmOrder.save()']")
            )
        )
        confirmation_button.click()
        print("Order Confirmation")
        
        driver.implicitly_wait(10) # seconds
        
        #Thank you page
        # Wait for the success message element to be present
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".order-completed .title strong"))
        )

        # Get the text content of the element
        success_text = success_message.text
        print("Success message found")
        
        # Verify the text matches the expected value
        if success_text == "Your order has been successfully processed!":
            print("Success message displayed correctly.")
        else:
            print(f"Error: Expected message 'Your order has been successfully processed!', but found '{success_text}'.")


    except TimeoutException:
        print("Error: Could not proceed timout error.")
    except NoSuchElementException:
        print("Error: Could not find element.")

    driver.quit()

if __name__ == "__main__":
    url = "https://demowebshop.tricentis.com/cell-phones"
    verify_checkout(url)