from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.saucedemo_helpers import tomar_captura


def test_agregar_primer_producto_al_carrito(login_in_driver):
    """
    Caso de prueba:
    Agregar el primer producto disponible al carrito,
    validar que el contador aumente y comprobar que el producto
    aparezca correctamente en la página del carrito.
    """
    driver = login_in_driver
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.url_contains("/inventory.html"))

        primer_producto = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

        nombre_producto = primer_producto.find_element(
            By.CLASS_NAME,
            "inventory_item_name"
        ).text

        precio_producto = primer_producto.find_element(
            By.CLASS_NAME,
            "inventory_item_price"
        ).text

        boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
        boton_agregar.click()

        contador_carrito = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )

        assert contador_carrito.text == "1"

        link_carrito = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        link_carrito.click()

        wait.until(EC.url_contains("/cart.html"))

        producto_en_carrito = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
        )

        precio_en_carrito = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_price"))
        )

        assert producto_en_carrito.text == nombre_producto
        assert precio_en_carrito.text == precio_producto

    except Exception:
        tomar_captura(driver, "fallo_carrito")
        raise