import time
import pytest
from selenium.webdriver.common.by import By
from conftest import BASE_URL

def test_process_without_data(driver):
    driver.get(BASE_URL)
    time.sleep(2)

    process_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Process']")
    process_btn.click()
    time.sleep(5)  

    try:
        error_element = driver.find_element(
            By.XPATH,
            "//div[contains(@class,'error') or contains(text(),'error') or contains(text(),'Please upload')]"
        )
        assert error_element.is_displayed(), "Expected error message is not visible."
    except Exception:
        pytest.fail("No error message appeared after clicking Process without uploading a file.")