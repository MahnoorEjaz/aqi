
import time
def test_homepage_contains_text(driver, base_url):

    driver.get(base_url)

    time.sleep(2)

    page_text = driver.page_source.lower()
    assert "clean air awareness" in page_text