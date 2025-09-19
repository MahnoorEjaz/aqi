import time
import pytest
from selenium.webdriver.common.by import By


def test_upload_button(driver, base_url):
    driver.get(base_url)

    time.sleep(2)

    upload_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Upload']")
    upload_btn.click()

    time.sleep(2)

    heading = driver.find_element(By.XPATH, "//h2[normalize-space()='Upload CSV & Check AQI']")
    assert heading.is_displayed()
