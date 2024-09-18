from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_verify_checkout(browser):
  """Verifies adding an item to the shopping cart and completing checkout."""
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
      EC.presence_of_element_located(
          (By.XPATH, "//div[@class='product-name']//h1[@itemprop='name']")
      )
  )
  product_title = product_title.text
  print(f"First product title: {product_title}")

  # Find and click "Add to Cart" button
  add_to_cart_button = WebDriverWait(browser, 5).until(
      EC.presence_of_element_located(
          (By.XPATH, ".//input[@type='button' and @value='Add to cart']")
      )
  )
  print("Click on Add to cart button")
  add_to_cart_button.click()

  # Wait for success message
  success_message = WebDriverWait(browser, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".content"))
  )
  success_text = success_message.text
  print("Success: Product added to shopping cart.")

  # Navigate to shopping cart page
  # Click the "shopping cart" link in the page header
  cart_link = WebDriverWait(browser, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".ico-cart"))
  )
  cart_link.click()

  # Find product in shopping cart table
  cart_product_title = WebDriverWait(browser, 10).until(
      EC.presence_of_element_located(
          (By.CSS_SELECTOR, "td.product a.product-name")
      )
  )
  assert cart_product_title.text == product_title, "Product title mismatch in cart"
  print("Product in shopping cart")

  # Agree with the terms of service
  termsofservice = browser.find_element(By.NAME, "termsofservice")
  termsofservice.click()

  # Find "Checkout" button
  checkout_button = browser.find_element(By.NAME, "checkout")
  checkout_button.click()

  # Find "Checkout as Guest" button
  checkout_as_guest = WebDriverWait(browser, 5).until(
      EC.presence_of_element_located(
          (By.XPATH, ".//input[@type='button' and @value='Checkout as Guest']")
      )
  )

  # Assert the button is in clickable state
  assert checkout_as_guest.is_enabled(), "Checkout as Guest button is not clickable"

  # Click the button
  checkout_as_guest.click()

  # Find Billing Address fields:
  first_name = WebDriverWait(browser, 5).until(
      EC.presence_of_element_located(
          (By.ID, "BillingNewAddress_FirstName")
      )
  )
  first_name.send_keys("first_name")

  last_name = browser.find_element(By.ID, "BillingNewAddress_LastName")
  last_name.send_keys("last_name")

  email = browser.find_element(By.ID, "BillingNewAddress_Email")
  email.send_keys("bdkcjns@cdsjn.dd")

  city = browser.find_element(By.ID, "BillingNewAddress_City")
  city.send_keys("New York")

  address1 = browser.find_element(By.ID, "BillingNewAddress_Address1")