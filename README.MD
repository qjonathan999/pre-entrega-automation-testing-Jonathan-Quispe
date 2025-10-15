# Proyecto: Automatización básica con Selenium y Python

## Objetivo / Propósito

Aplicar conocimientos para automatizar flujos básicos de navegación web utilizando Selenium WebDriver y Python. El objetivo es diseñar y ejecutar scripts de prueba que interactúen con la aplicación de ejemplo situada en https://www.saucedemo.com/, validando escenarios comunes como inicio de sesión, navegación por productos, agregar/eliminar productos del carrito y finalizar una compra básica.

## Alcance

- Automatizar casos de uso funcionales básicos en la aplicación de demostración `saucedemo`.
- Implementar scripts reutilizables y fáciles de mantener que demuestren buenas prácticas de automatización (separación de locators, funciones reutilizables, manejo de esperas explícitas).
- Ejecutar las pruebas de forma local usando Python y Selenium WebDriver.

## Tecnologías

- Python 3.8+ (o la versión de tu entorno)
- Selenium WebDriver
- Navegadores soportados: Chrome, Firefox (requieren su correspondiente driver)

## Ejecución rápida (resumen)

1. Instalar dependencias (por ejemplo crear un virtualenv e instalar Selenium):

	pip install pytest pytest-html selenium

2. Asegurarse de tener el WebDriver adecuado en PATH (chromedriver/geckodriver).

3. Ejecutar los scripts de prueba desde la carpeta del proyecto. Ejemplo simple:

	python tests/test_login.py

Nota: Ajusta los nombres y rutas de los scripts según la estructura del repositorio.

## Credenciales de prueba (saucedemo)

Puedes usar las credenciales públicas del sitio de demostración:

- Usuario: standard_user
- Contraseña: secret_sauce

