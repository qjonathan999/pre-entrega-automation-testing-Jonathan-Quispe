from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage:
    _INVENTORY_CONTAINER="inventory_container"
    _PRODUCT_SORT_CONTAINER="product_sort_container"
    _INVENTORY_ITEM="inventory_item"
    _INVENTORY_ITEM_NAME="inventory_item_name"

    def __init__(self,driver):
        self.driver=driver

    def is_loaded(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(("id", self._INVENTORY_CONTAINER)))

    def is_inventory_page(self):
        WebDriverWait(self.driver,5).until(EC.url_contains("inventory.html"))

    def exist_products(self):
        cantidad=0
        productos=self.driver.find_elements("class name", self._INVENTORY_ITEM)
        for producto in productos:
            cantidad+=1
        print(f"Cantidad de productos encontrados: {cantidad}")    
        return cantidad > 0
    
    def get_first_product_name(self):
        productos=self.driver.find_elements("class name", self._INVENTORY_ITEM)
        if productos:
            nombre=productos[0].find_element("class name",self._INVENTORY_ITEM_NAME).text
            return nombre
        return None
    
    def logout(self):
        menu_button_id="react-burger-menu-btn"
        logout_sidebar_link_id="logout_sidebar_link"
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(("id", menu_button_id))).click()
        time.sleep(3)  # Espera breve para que se abra el menú
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(("id", logout_sidebar_link_id))).click()
        time.sleep(3)  # Espera breve para que se complete el logout

    def click_to_cart(self):
        cart_button_class="shopping_cart_link"
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(("class name", cart_button_class))).click()
        time.sleep(2)  # Espera breve para que se abra el carrito    