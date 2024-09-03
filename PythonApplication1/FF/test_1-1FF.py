from selenium import webdriver
from selenium.webdriver.common.by import By

def check_title(url, expected_title):
    """Checks the title of a given URL.

    Args:
        url (str): The URL to check.
        expected_title (str): The expected title of the page.

    Returns:
        bool: True if the title matches, False otherwise.
    """

    try:
        driver = webdriver.Firefox()  # Use Firefox
        driver.get(url)

        actual_title = driver.title

        if actual_title == expected_title:
            print("Title is correct:", actual_title)
            return True
        else:
            print("Title mismatch! Expected:", expected_title, "Actual:", actual_title)
            return False

    finally:
        driver.quit()

# Example usage:
url = "https://www.epam.com"
expected_title = "EPAM | Software Engineering & Product Development Services"

if check_title(url, expected_title):
    print("Test passed successfully")
else:
    print("Test failed")