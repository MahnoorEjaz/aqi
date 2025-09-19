import time
import pytest
from selenium.webdriver.common.by import By
from conftest import BASE_URL

def test_click_download_only(driver):
    driver.get(BASE_URL)
    time.sleep(2) 

    download_btn = driver.find_element(By.XPATH, "//a[normalize-space()='Download CSV']")
    download_btn.click()
    time.sleep(4) 


    error_element = driver.find_element(
        By.XPATH,
        "//div[contains(@class,'font-semibold') and text()='No results available to download.']"
    )
    assert error_element.is_displayed(), "Error message not shown when trying to download without data."
