
def login_saucedemo(driver):
    
    # Usar localizadores por nombre de atributo (id)
    driver.find_element("id", "user-name").send_keys(USERNAME)
    driver.find_element("id", "password").send_keys(PASSWORD)
    driver.find_element("id", "login-button").click()
    return driver