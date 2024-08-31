from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def check_policies():
    """Checks the availability of expected policies in the 'Policy' section on epam.com."""

    expected_policies = [
        "INVESTORS",
        "COOKIE POLICY",
        "OPEN SOURCE",
        "APPLICANT PRIVACY NOTICE",
        "PRIVACY POLICY",
        "WEB ACCESSIBILITY"
    ]

    driver = webdriver.Chrome()  # Replace with your preferred browser driver

    try:
        # Open epam.com
        driver.get("https://www.epam.com")

        # Click the "Accept All" cookies button (modify if needed)
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
        )
        accept_cookies_button.click()

        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the 'Policy' section to be present
        policy_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "policies"))
        )

        # Find all policy links within the section
        policy_links = policy_section.find_elements(By.CSS_SELECTOR, "ul.policies-left a.fat-links, ul.policies-right a.fat-links")

        # Check each expected policy against the found links
        for expected_policy in expected_policies:
            found = False
            for link in policy_links:
                if expected_policy == link.text:
                    found = True
                    break  # Exit inner loop if policy is found

            if not found:
                print(f"Error: Policy '{expected_policy}' not found on the page.")
                break  # Exit outer loop and stop checking if a policy is missing

        else:
            print("Success: All expected policies found on the page.")

    except TimeoutException as e:
        print(f"Error: Timeout waiting for element. {e}")
    except NoSuchElementException as e:
        print(f"Error: Element not found. {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    check_policies()