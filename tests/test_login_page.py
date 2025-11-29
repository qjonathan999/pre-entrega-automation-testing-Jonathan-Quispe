from page.login_page import LoginPage
from data.data_login import CASOS_LOGIN
from utils.helperCSV import get_login_csv
from utils.helperCSV import get_login_json
from utils.faker import get_login_faker
import pytest
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("username,password,expected_result",get_login_faker())
def test_login(driver,username,password,expected_result):
    log = logging.getLogger(__name__)
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login(username,password)
    if expected_result:
        WebDriverWait(driver,4).until(EC.url_contains("inventory.html"))
        assert "inventory.html" in driver.current_url
    else:
        assert "inventory.html" not in driver.current_url 