from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
import logging
import random

def test_inventory(driver):
    log = logging.getLogger(__name__)
    loginPage = LoginPage(driver)
    inventoryPage = InventoryPage(driver)
    cartPage = CartPage(driver)
    
    loginPage.open()
    loginPage.login()

    inventoryPage.is_loaded()
    inventoryPage.is_inventory_page()
    assert inventoryPage.exist_products()

    cant_productos = inventoryPage.get_cant_productos()
    log.info(f"Cantidad de productos en el inventario: {cant_productos}")

    cant_prod_selec = 3
# --- Seleccionar aleatoriamente n productos ---
    indices = random.sample(range(cant_productos), cant_prod_selec)

    for i in indices:
        log.info(f"Seleccionando producto en el índice: {i}")
        inventoryPage.select_product_by_index(i)

    inventoryPage.click_to_cart()
    assert "cart.html" in driver.current_url    

    assert cartPage.get_cant_productos_en_carrito() == cant_prod_selec

    cartPage.logout()
    assert "https://www.saucedemo.com/" in driver.current_url