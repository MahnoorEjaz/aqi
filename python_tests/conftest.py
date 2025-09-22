import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

@pytest.fixture(scope="session")
def base_url():
  
    return "http://localhost:8000"
@pytest.fixture
def driver():
   
    chromedriver_autoinstaller.install()

    options = Options()
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--no-sandbox")  
    options.add_argument("--disable-dev-shm-usage")  
    options.add_argument("--disable-gpu")  
    options.add_argument("--ignore-certificate-errors") 
    options.add_argument("--allow-insecure-localhost")  
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
