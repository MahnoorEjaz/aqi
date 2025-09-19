import time

from selenium.webdriver.common.by import By

def test_message_button(driver, base_url):
    driver.get(base_url)

    time.sleep(2)

    upload_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Analytics']")
    upload_btn.click()

    time.sleep(2)

    heading = driver.find_element(By.XPATH, "//h3[normalize-space()='AQI Overview']")
    assert heading.is_displayed()
