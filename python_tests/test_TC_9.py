import time
import pytest
from selenium.webdriver.common.by import By
from conftest import BASE_URL

def test_populate_messages_and_save(driver):
    driver.get(BASE_URL)
    time.sleep(2)  
    time.sleep(2)

    upload_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Messages']")
    upload_btn.click()

    messages = {
        "Good (0-50)": "Good air quality message",
        "Moderate (51-100)": "Moderate air quality message",
        "Unhealthy Sensitive (101-150)": "Unhealthy sensitive message",
        "Unhealthy (151-200)": "Unhealthy message",
        "Very Unhealthy (201-300)": "Very unhealthy message",
        "Hazardous (301+)": "Hazardous message"
    }

    for placeholder, value in messages.items():
        input_field = driver.find_element(By.XPATH, f"//input[@placeholder='{placeholder}']")
        input_field.clear()
        input_field.send_keys(value)
        time.sleep(0.2) 

    save_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Save Messages']")
    save_btn.click()
    time.sleep(3) 

    success_msg = driver.find_element(
        By.CSS_SELECTOR,
    "div.mb-6.rounded-lg.border.border-green-200.bg-green-50.px-4.py-3.text-sm.text-green-800"
    )
    assert success_msg.is_displayed(), "Success message not shown after saving messages."
