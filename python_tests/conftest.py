import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "http://127.0.0.1:8000"   # Your Laravel app URL

@pytest.fixture
def driver():
    """Provide a Chrome driver instance and quit after the test."""
    opts = Options()
    opts.add_experimental_option("excludeSwitches", ["enable-logging"])
    d = webdriver.Chrome(options=opts)
    d.maximize_window()
    yield d
    d.quit()
