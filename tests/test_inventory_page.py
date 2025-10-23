from page.login_page import LoginPage
from page.inventory_page import InventoryPage
import logging

def test_inventory(driver):
    log = logging.getLogger(__name__)
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login("standard_user", "secret_sauce")

    inventoryPage = InventoryPage(driver)
    inventoryPage.is_loaded()
    # Verificación adicional: URL contiene inventory
    assert "inventory.html" in driver.current_url
    assert inventoryPage.exist_products()
    
    log.info(f"Primer producto: {inventoryPage.get_first_product_name()}")