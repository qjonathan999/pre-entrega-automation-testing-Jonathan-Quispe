from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import URL, USERNAME, PASSWORD

class LoginPage:
    _NAME_INPUT="user-name"
    _PASSWORD_INPUT="password"
    _LOGIN_BUTTON="login-button"

    def __init__(self,driver):
        self.driver=driver

    def open(self):
        self.driver.get(URL)

    def login(self,username=USERNAME,password=PASSWORD):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(("id", self._NAME_INPUT)))
        self.driver.find_element("id", self._NAME_INPUT).send_keys(username)
        self.driver.find_element("id", self._PASSWORD_INPUT).send_keys(password)
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(("id", self._LOGIN_BUTTON))).click()
        

