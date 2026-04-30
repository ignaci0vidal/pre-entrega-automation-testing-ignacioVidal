import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import crear_driver
from utils.saucedemo_helpers import (
    login_valido,
    esperar_elemento_visible,
    esperar_elemento_clickeable,
    tomar_captura,
)


@pytest.fixture
def driver():
    """
    Fixture de Pytest.
    Crea un navegador para cada test y lo cierra al finalizar.
    Esto permite que los tests sean independientes entre sí.
    """
    navegador = crear_driver()
    yield navegador
    navegador.quit()


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


def test_catalogo_muestra_productos(driver):
    """
    Caso de prueba:
    Validar que la página de inventario muestre el catálogo,
    productos visibles y elementos principales de la interfaz.
    """
    try:
        login_valido(driver)

        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

        titulo_productos = esperar_elemento_visible(driver, (By.CLASS_NAME, "title"))
        assert titulo_productos.text == "Products"

        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0

        primer_producto = productos[0]

        nombre_primer_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name")
        precio_primer_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price")

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


def test_agregar_primer_producto_al_carrito(driver):
    """
    Caso de prueba:
    Agregar el primer producto disponible al carrito,
    validar que el contador aumente y comprobar que el producto
    aparezca correctamente en la página del carrito.
    """
    try:
        login_valido(driver)

        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

        primer_producto = esperar_elemento_visible(driver, (By.CLASS_NAME, "inventory_item"))

        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

        boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
        boton_agregar.click()

        contador_carrito = esperar_elemento_visible(driver, (By.CLASS_NAME, "shopping_cart_badge"))
        assert contador_carrito.text == "1"

        link_carrito = esperar_elemento_clickeable(driver, (By.CLASS_NAME, "shopping_cart_link"))
        link_carrito.click()

        WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

        producto_en_carrito = esperar_elemento_visible(driver, (By.CLASS_NAME, "inventory_item_name"))
        precio_en_carrito = esperar_elemento_visible(driver, (By.CLASS_NAME, "inventory_item_price"))

        assert producto_en_carrito.text == nombre_producto
        assert precio_en_carrito.text == precio_producto

    except Exception:
        tomar_captura(driver, "fallo_carrito")
        raise