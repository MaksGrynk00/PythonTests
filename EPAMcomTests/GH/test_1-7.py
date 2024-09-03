from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

def validate_contact_form():
    """Validates the contact form on EPAM.com."""

    driver = webdriver.Chrome()  # Replace with your preferred browser driver

    try:
        # Open the EPAM contact page
        driver.get("https://www.epam.com/about/who-we-are/contact")

        # Find and click on the 'Accept All' cookies button (modify if needed)
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
        )
        accept_cookies_button.click()

        # Scroll down the page
        driver.execute_script("window.scrollTo(0, 5000)")

        # Find and validate labels' color
        label_selectors = [
            "label[for='_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_first_name']",
            "label[for='_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_last_name']",
            "label[for='_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_email']",
            "label[for='_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_phone']",
            "label[for='_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_comment_how_hear_about']",
        ]

        for selector in label_selectors:
            label_element = driver.find_element(By.CSS_SELECTOR, selector)
            label_color = label_element.value_of_css_property("color")
            if label_color.lower() != "rgba(255, 255, 255, 1)":  # White color in RGB
                print(f"Error: Label '{label_element.text}' has color {label_color} instead of white.")
            else:
                print(f"Label '{label_element.text}' has the expected white color.")
                
        # Scroll down the page
        scroll_position = 2000  # Adjust if needed
        driver.execute_script("window.scrollTo(0, {});".format(scroll_position))

        # Find the submit button and click
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-ui[type='submit']"))
        )
        submit_button.click()

        # Validate required fields are highlighted after submit
        for selector in label_selectors:
            label_element = driver.find_element(By.CSS_SELECTOR, selector)
            parent_div = label_element.find_element(By.XPATH, "..")
            border_color = parent_div.value_of_css_property("border-color")
            if border_color.lower() != "rgb(255, 77, 64)":  # Red color in RGB
                print(f"Error: Label '{label_element.text}' is not highlighted in red.")
            else:
                print(f"Label '{label_element.text}' is highlighted as required (red border).")

    except TimeoutException as e:
        print(f"Error: Timeout waiting for element. {e}")
    except NoSuchElementException as e:
        print(f"Error: Element not found. {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    validate_contact_form()