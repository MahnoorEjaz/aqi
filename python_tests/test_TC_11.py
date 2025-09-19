import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
FILE_PATH = r"D:\downloads\contacts.csv"  
DOWNLOAD_DIR = r"D:\downloads"  
FILE_NAME = "aqi_results.csv"   

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True
    })
    d = webdriver.Chrome(options=chrome_options)
    d.maximize_window()
    yield d
    d.quit()

def test_download_csv(driver, base_url):
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

    # Click the "Download CSV" button
    download_btn = driver.find_element(By.XPATH, "//a[normalize-space()='Download CSV']")
    download_btn.click()
    time.sleep(5) 

    downloaded_file_path = os.path.join(DOWNLOAD_DIR, FILE_NAME)
    assert os.path.exists(downloaded_file_path), f"{FILE_NAME} was not downloaded."
