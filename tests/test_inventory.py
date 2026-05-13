from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.saucedemo_helpers import (
    esperar_elemento_visible,
    tomar_captura,
)


def test_catalogo_muestra_productos(login_in_driver):
    """
    Caso de prueba:
    Validar que la página de inventario muestre el catálogo,
    productos visibles y elementos principales de la interfaz.
    """
    driver = login_in_driver

    try:
        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

        titulo_productos = esperar_elemento_visible(driver, (By.CLASS_NAME, "title"))
        assert titulo_productos.text == "Products"

        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0

        primer_producto = productos[0]

        nombre_primer_producto = primer_producto.find_element(
            By.CLASS_NAME,
            "inventory_item_name"
        )

        precio_primer_producto = primer_producto.find_element(
            By.CLASS_NAME,
            "inventory_item_price"
        )

        assert nombre_primer_producto.text != ""
        assert precio_primer_producto.text != ""

        print(f"Primer producto: {nombre_primer_producto.text}")
        print(f"Precio: {precio_primer_producto.text}")

        menu = esperar_elemento_visible(driver, (By.ID, "react-burger-menu-btn"))
        filtro = esperar_elemento_visible(driver, (By.CLASS_NAME, "product_sort_container"))
        carrito = esperar_elemento_visible(driver, (By.CLASS_NAME, "shopping_cart_link"))

        assert menu.is_displayed()
        assert filtro.is_displayed()
        assert carrito.is_displayed()

    except Exception:
        tomar_captura(driver, "fallo_catalogo")
        raise