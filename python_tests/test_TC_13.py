import time
from selenium.webdriver.common.by import By


 
FILE_PATH = r"D:\downloads\c.csv"  
def test_empty_csv(driver, base_url):
    driver.get(base_url)
    time.sleep(2)

    browse_label = driver.find_element(By.XPATH, "//label[normalize-space()='Browse']")
    browse_label.click()
    time.sleep(5)

    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(FILE_PATH)
    time.sleep(3)  

    process_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Process']")
    process_btn.click()
    time.sleep(5)  

    error_element = driver.find_element(By.XPATH, "//div[@id='file-error']")
    assert "CSV appears to be empty" in error_element.text, "Empty CSV error message not shown."