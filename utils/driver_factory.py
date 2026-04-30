from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def crear_driver():
    """
    Crea y configura una instancia de Chrome WebDriver.
    Se utiliza una función separada para reutilizar la configuración
    en todos los tests del proyecto.
    """
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(2)

    return driver