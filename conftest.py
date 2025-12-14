import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

import os
import pytest

# Verificar si la carpeta "reports" existe, y si no, crearla
if not os.path.exists('reports'):
    os.makedirs('reports')

# Ejecutar pytest programáticamente
os.system('pytest --html=reports/report.html --maxfail=1 --disable-warnings')

def pytest_configure():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Valores compartidos para las páginas/tests
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        yield driver
    finally:
        try:
            driver.quit()
        except Exception:
            pass