from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL_SAUCEDEMO = "https://www.saucedemo.com/"
USUARIO_VALIDO = "standard_user"
PASSWORD_VALIDO = "secret_sauce"


def esperar_elemento_visible(driver, locator, tiempo=10):
    """
    Espera explícitamente hasta que un elemento sea visible en pantalla.
    """
    wait = WebDriverWait(driver, tiempo)
    return wait.until(EC.visibility_of_element_located(locator))


def esperar_elemento_clickeable(driver, locator, tiempo=10):
    """
    Espera explícitamente hasta que un elemento pueda recibir clics.
    """
    wait = WebDriverWait(driver, tiempo)
    return wait.until(EC.element_to_be_clickable(locator))


def login_valido(driver):
    """
    Realiza el login en SauceDemo con credenciales válidas.
    """
    driver.get(URL_SAUCEDEMO)

    input_usuario = esperar_elemento_visible(driver, (By.ID, "user-name"))
    input_password = esperar_elemento_visible(driver, (By.ID, "password"))
    boton_login = esperar_elemento_clickeable(driver, (By.ID, "login-button"))

    input_usuario.send_keys(USUARIO_VALIDO)
    input_password.send_keys(PASSWORD_VALIDO)
    boton_login.click()


def tomar_captura(driver, nombre_base):
    """
    Guarda una captura de pantalla con fecha y hora.
    Se puede usar como evidencia cuando falla un test.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta = f"screenshots/{nombre_base}_{timestamp}.png"
    driver.save_screenshot(ruta)
    return ruta