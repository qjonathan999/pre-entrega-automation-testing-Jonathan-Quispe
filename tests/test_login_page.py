from page.login_page import LoginPage
from data.data_login import CASOS_LOGIN
import pytest

@pytest.mark.parametrize("username,password,expected_result", CASOS_LOGIN)
def test_login(driver,username,password,expected_result):
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login(username,password)

    if expected_result:
        assert "inventory.html" in driver.current_url
    else:
        assert "inventory.html" not in driver.current_url 