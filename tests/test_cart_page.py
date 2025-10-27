from page.login_page import LoginPage
from page.inventory_page import InventoryPage
import logging

def test_inventory(driver):
    log = logging.getLogger(__name__)
    loginPage = LoginPage(driver)
    inventoryPage = InventoryPage(driver)
    
    loginPage.open()
    loginPage.login()

    inventoryPage.is_loaded()
    inventoryPage.is_inventory_page()
    assert inventoryPage.exist_products()

    inventoryPage.click_to_cart()
    assert "cart.html" in driver.current_url