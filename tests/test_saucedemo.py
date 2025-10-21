import pytest
from conftest import get_driver
from utils.helpers import login_saucedemo


def test_login_success(get_driver):
    driver = get_driver
    driver.get(URL)
    login_saucedemo(driver)
    assert "inventory.html" in driver.current_url

def test_catalogo(get_driver):
    driver = get_driver
    driver.get(URL)
    login_saucedemo(driver)

    items = driver.find_elements("class name", "inventory_item")
    print(f"productos encontrados: {len(items)}")
    assert len(items) > 0
