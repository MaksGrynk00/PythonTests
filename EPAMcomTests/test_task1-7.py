import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_validate_contact_form(browser):
    """Validates the contact form on EPAM.com."""

    # Open the EPAM contact page
    browser.get("https://www.epam.com/about/who-we-are/contact")

    # Find and click on the 'Accept All' cookies button
    accept_cookies_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[text()='Accept All']"))
    )
    time.sleep(3)
    accept_cookies_button.click()

    # Find and validate labels' color
    label_selectors = [
        "label[for='_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_first_name']",
        "label[for='_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_last_name']",
        "label[for='_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_email']",
        "label[for='_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_phone']",
        "label[for='_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_comment_how_hear_about']",
    ]
    colors_before = {}
    for selector in label_selectors:
        label_element = browser.find_element(By.CSS_SELECTOR, selector)
        initial_color = label_element.value_of_css_property("color")
        colors_before[selector] = initial_color

        # Click submit button
    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    time.sleep(3)
    submit_button.click()

    # Validate required fields are highlighted after submit
    for selector in label_selectors:
        label_element = browser.find_element(By.CSS_SELECTOR, selector)
        color_after_submit = label_element.value_of_css_property("color")

        # Assert color has changed after submitting the form
        assert (
                color_after_submit != colors_before[selector]
        ), f"Color of '{label_element.text}' did not change after submitting the form."