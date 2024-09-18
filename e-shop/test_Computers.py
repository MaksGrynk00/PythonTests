from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_verify_computer_subgroups(browser):
  """Verifies the 'Computers' group and its sub-groups."""
  browser.get("https://demowebshop.tricentis.com/computers")

  # Expected sub-group names
  expected_subgroups = {
      "Desktops": "//a[@title='Show products in category Desktops'][normalize-space()='Desktops']",
      "Notebooks": "//a[@title='Show products in category Notebooks'][normalize-space()='Notebooks']",
      "Accessories": "//a[@title='Show products in category Accessories'][normalize-space()='Accessories']",
  }

  # Expected sub-group names (left navigation)
  expected_left_menu = {
      "Desktops": "//li[@class='inactive']//a[normalize-space()='Desktops']",
      "Notebooks": "//li[@class='inactive']//a[normalize-space()='Notebooks']",
      "Accessories": "//li[@class='inactive']//a[normalize-space()='Accessories']",
  }
  # Verify sub-groups on product page
  missing_subgroups = []
  for name, selector in expected_subgroups.items():
      element = WebDriverWait(browser, 5).until(
          EC.presence_of_element_located((By.XPATH, selector))
      )
      assert element is not None, f"Sub-group '{name}' not found on product page"

  # Verify sub-groups on left navigation
  missing_left_menu = []
  for name, selector in expected_left_menu.items():
      element = WebDriverWait(browser, 5).until(
          EC.presence_of_element_located((By.XPATH, selector))
      )
      assert element is not None, f"Sub-group '{name}' not found in left navigation"

  print("Sub-groups for 'Computers' group verified successfully!")
  browser.quit()
