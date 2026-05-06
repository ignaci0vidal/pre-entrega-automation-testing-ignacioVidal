from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def crear_driver():
    """
    Crea y configura una instancia de Chrome WebDriver.
    Se utiliza modo incógnito para evitar guardar sesión,
    usuario, contraseña o datos de navegación entre ejecuciones.
    """
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(2)

    return driver