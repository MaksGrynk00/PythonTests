from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def verify_computer_subgroups():
    """Verifies the 'Computers' group and its sub-groups."""

    driver = webdriver.Chrome()  
    driver.get("https://demowebshop.tricentis.com/computers")

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
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, selector))
            )
        except TimeoutException:
            missing_subgroups.append(name)

    # Verify sub-groups on left navigation
    missing_left_menu = []
    for name, selector in expected_left_menu.items():
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, selector))
            )
        except TimeoutException:
            missing_left_menu.append(name)

    if missing_subgroups or missing_left_menu:
        error_message = (
            f"Error: Missing sub-groups: {', '.join(missing_subgroups + missing_left_menu)}"
        )
        print(error_message)
    else:
        print("Sub-groups for 'Computers' group verified successfully!")

    driver.quit()

if __name__ == "__main__":
    verify_computer_subgroups()