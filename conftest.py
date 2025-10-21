import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL="https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.fixture
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    try:
        yield driver
    finally:
        try:
            driver.quit()
        except Exception:
            pass