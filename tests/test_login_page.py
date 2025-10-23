from page.login_page import LoginPage

def test_login(driver):
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url