import time
from selenium.webdriver.common.by import By
from conftest import BASE_URL

 
FILE_PATH = r"D:\downloads\thread.png"
def test_invalid_file(driver):
    driver.get(BASE_URL)
    time.sleep(2)

    browse_label = driver.find_element(By.XPATH, "//label[normalize-space()='Browse']")
    browse_label.click()
    time.sleep(5)

    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(FILE_PATH)
    time.sleep(3)  
 

    name_header = driver.find_element(By.XPATH, "//div[@id='file-error']")
    assert name_header.is_displayed(), "'Name' header not found after processing."