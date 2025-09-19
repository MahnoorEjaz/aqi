import time
import pytest
from selenium.webdriver.common.by import By


def test_save_messages_with_empty_fields(driver, base_url):
    driver.get(base_url)
    time.sleep(2)

    # Click Messages button
    messages_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Messages']")
    messages_btn.click()
    time.sleep(1)

    # Intentionally leave some fields empty
    messages = {
        "Good (0-50)": "",  # empty to trigger error
        "Moderate (51-100)": "",
        "Unhealthy Sensitive (101-150)": "",
        "Unhealthy (151-200)": "",
        "Very Unhealthy (201-300)": "",
        "Hazardous (301+)": ""
    }

    for placeholder, value in messages.items():
        input_field = driver.find_element(By.XPATH, f"//input[@placeholder='{placeholder}']")
        input_field.clear()
        input_field.send_keys(value)
        time.sleep(0.2)

    save_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Save Messages']")
    save_btn.click()
    time.sleep(2)

    error_elements = driver.find_elements(
        By.XPATH,
        "//div[contains(@class,'bg-red-50') or contains(text(),'required') or contains(text(),'Please')]"
    )
    success_elements = driver.find_elements(
        By.CSS_SELECTOR,
        "div.mb-6.rounded-lg.border.border-green-200.bg-green-50.px-4.py-3.text-sm.text-green-800"
    )

    if error_elements and error_elements[0].is_displayed():
       
        assert True
    elif success_elements and success_elements[0].is_displayed():
       
        pytest.fail("Success message shown despite empty fields. Validation failed.")
    else:
     
        pytest.fail("No success or error message appeared after clicking Save Messages.")
