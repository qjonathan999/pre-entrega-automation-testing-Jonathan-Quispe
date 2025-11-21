from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    _CART_ITEM = "cart_item"

    def __init__(self, driver):
        self.driver = driver

    def get_cant_productos_en_carrito(self):
        productos = self.driver.find_elements("class name",self._CART_ITEM)
        return len(productos)
    
    def logout(self):
        menu_button_id="react-burger-menu-btn"
        logout_sidebar_link_id="logout_sidebar_link"
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(("id", menu_button_id))).click()
        time.sleep(3)  # Espera breve para que se abra el menú
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(("id", logout_sidebar_link_id))).click()
        time.sleep(3)  # Espera breve para que se complete el logout