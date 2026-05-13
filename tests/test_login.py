from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.saucedemo_helpers import (
    login_valido,
    esperar_elemento_visible,
    tomar_captura,
)


def test_login_exitoso(driver):
    """
    Caso de prueba:
    Validar que un usuario pueda iniciar sesión correctamente
    y sea redirigido a la página de inventario.
    """
    try:
        login_valido(driver)

        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

        assert "/inventory.html" in driver.current_url

        titulo_productos = esperar_elemento_visible(driver, (By.CLASS_NAME, "title"))
        logo = esperar_elemento_visible(driver, (By.CLASS_NAME, "app_logo"))

        assert titulo_productos.text == "Products"
        assert logo.text == "Swag Labs"

    except Exception:
        tomar_captura(driver, "fallo_login_exitoso")
        raise