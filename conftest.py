import pytest

from utils.driver_factory import crear_driver
from utils.saucedemo_helpers import login_valido


@pytest.fixture
def driver():
    """
    Crea un navegador nuevo para cada test y lo cierra al finalizar.
    Esto permite que los tests sean independientes entre sí.
    """
    navegador = crear_driver()
    yield navegador
    navegador.quit()


@pytest.fixture
def login_in_driver(driver):
    """
    Inicia sesión antes de ejecutar los tests que necesitan estar en inventario.
    """
    login_valido(driver)
    return driver