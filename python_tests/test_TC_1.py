
from conftest import BASE_URL
import time
def test_homepage_contains_text(driver):

    driver.get(BASE_URL)

    time.sleep(2)

    page_text = driver.page_source.lower()
    assert "clean air awareness" in page_text