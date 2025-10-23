from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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