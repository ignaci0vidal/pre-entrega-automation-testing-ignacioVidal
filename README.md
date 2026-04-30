# Pre-Entrega | Automatización QA con Selenium y Pytest

## Propósito del proyecto

Este proyecto corresponde a la pre-entrega del curso de Automatización QA.

El objetivo es automatizar flujos básicos de navegación web sobre el sitio [SauceDemo](https://www.saucedemo.com/), aplicando Selenium WebDriver con Python y Pytest.

La automatización incluye:

- Login con credenciales válidas.
- Validación de redirección a la página de inventario.
- Verificación del catálogo de productos.
- Validación de elementos principales de la interfaz.
- Interacción con productos.
- Agregado de un producto al carrito.
- Validación del producto dentro del carrito.
- Generación de reporte HTML con Pytest.
- Capturas automáticas en caso de fallos.

## Sitio utilizado

[SauceDemo](https://www.saucedemo.com/)

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Git
- GitHub

## Estructura del proyecto

```text
pre-entrega-automation-testing-ignacio-vidal/
│
├── tests/
│   └── test_saucedemo.py
│
├── utils/
│   ├── driver_factory.py
│   └── saucedemo_helpers.py
│
├── reports/
│   └── reporte.html
│
├── screenshots/
│   └── capturas generadas en caso de fallo
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Casos de prueba automatizados

### 1. Login exitoso

Pasos automatizados:

1. Navegar a `https://www.saucedemo.com/`.
2. Ingresar usuario válido: `standard_user`.
3. Ingresar contraseña válida: `secret_sauce`.
4. Hacer clic en el botón de login.
5. Validar que la URL contenga `/inventory.html`.
6. Validar que se visualicen los textos `Products` y `Swag Labs`.

### 2. Navegación y verificación del catálogo

Validaciones realizadas:

1. Validar que el título de la página de inventario sea `Products`.
2. Comprobar que existan productos visibles en la página.
3. Obtener y listar el nombre del primer producto.
4. Obtener y listar el precio del primer producto.
5. Validar que el menú principal esté presente.
6. Validar que el filtro de ordenamiento esté presente.
7. Validar que el ícono del carrito esté presente.

### 3. Interacción con productos y carrito

Pasos automatizados:

1. Iniciar sesión con credenciales válidas.
2. Obtener el nombre y precio del primer producto visible.
3. Hacer clic en el botón para agregar el primer producto al carrito.
4. Verificar que el contador del carrito muestre `1`.
5. Navegar a la página del carrito.
6. Validar que el producto agregado aparezca correctamente en el carrito.
7. Validar que el precio del producto en el carrito coincida con el precio obtenido desde el catálogo.

## Organización del código

El proyecto está dividido en archivos separados para mejorar la claridad y el mantenimiento.

### Carpeta `tests/`

Contiene los casos de prueba automatizados.

Archivo principal:

- `test_saucedemo.py`

Este archivo incluye los tests de:

- Login exitoso.
- Validación del catálogo.
- Agregado de producto al carrito.

### Carpeta `utils/`

Contiene funciones auxiliares reutilizables.

Archivos principales:

- `driver_factory.py`
- `saucedemo_helpers.py`

El archivo `driver_factory.py` se encarga de crear y configurar el navegador.

El archivo `saucedemo_helpers.py` contiene funciones auxiliares como:

- Login válido.
- Esperas explícitas.
- Capturas de pantalla.

## Instalación de dependencias

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd pre-entrega-automation-testing-ignacio-vidal
```

### 2. Instalar dependencias

```bash
py -m pip install -r requirements.txt
```

## Ejecución de pruebas

### Ejecutar todos los tests

```bash
py -m pytest -v
```

### Ejecutar tests y generar reporte HTML


py -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html


## Reporte HTML

El reporte HTML se genera dentro de la carpeta `reports/`.

    Ruta esperada:

        reports/reporte.html


Este archivo contiene el resultado de la ejecución de las pruebas automatizadas.

## Evidencias

El proyecto contempla dos tipos de evidencias:

    1. Reporte HTML generado por Pytest.
    2. Capturas de pantalla automáticas en caso de fallos.

    Las capturas se guardan en la carpeta:

        screenshots/


## Datos de prueba utilizados

Credenciales válidas de SauceDemo:

    Usuario: standard_user
    Contraseña: secret_sauce


## Criterios cumplidos de la pre-entrega

- Automatización de login.
- Uso de espera explícita.
- Validación de `/inventory.html`.
- Validación de textos `Products` y `Swag Labs`.
- Verificación del catálogo.
- Validación de productos visibles.
- Obtención del nombre y precio del primer producto.
- Interacción con productos.
- Agregado del primer producto al carrito.
- Validación del contador del carrito.
- Validación del producto dentro del carrito.
- Organización del código en carpetas `tests/` y `utils/`.
- Uso de Pytest.
- Uso de Selenium WebDriver.
- Generación de reporte HTML.
- README completo.
- Proyecto preparado para subir a GitHub.


## Autor
Ignacio Vidal