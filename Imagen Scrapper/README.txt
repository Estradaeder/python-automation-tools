Script en Python que busca automáticamente URLs de imágenes de productos a partir de una lista de SKU almacenada en un archivo de Excel.

El programa utiliza DuckDuckGo Images para encontrar imágenes relacionadas con cada SKU y guarda la primera URL encontrada en un nuevo archivo de Excel.

Tecnologías utilizadas

Python

requests

BeautifulSoup

pandas

threading (multihilo)

web scraping

Funcionamiento

El script realiza el siguiente proceso:

Lee un archivo de Excel que contiene una columna con SKUs.

Para cada SKU realiza una búsqueda de imágenes en DuckDuckGo.

Obtiene la primera URL de imagen encontrada.

Ejecuta las búsquedas usando múltiples hilos para acelerar el proceso.

Guarda los resultados en un nuevo archivo de Excel con dos columnas:

SKU

URL de imagen

Estructura esperada del Excel

El archivo debe contener una columna llamada:

SKU

Ejemplo:

SKU
12345
ABC-987
PROD-001
Instalación

Instalar las dependencias necesarias:

pip install requests beautifulsoup4 pandas openpyxl
Configuración

En el script se pueden modificar los siguientes parámetros:

EXCEL_PATH = "ruta_del_archivo.xlsx"
COLUMNA_SKU = "SKU"
NUM_HILOS = 5
SALIDA_FINAL = "urls_imagenes_duck.xlsx"

EXCEL_PATH → ruta del archivo con los SKUs

COLUMNA_SKU → nombre de la columna en Excel

NUM_HILOS → número de procesos simultáneos

SALIDA_FINAL → nombre del archivo de resultados

Ejecución

Ejecutar el script con:

python buscador_imagenes.py
Salida

Se generará un archivo Excel con la siguiente estructura:

SKU	URL
12345	https://example.com/image.jpg

ABC-987	https://example.com/image2.jpg

Si no se encuentra imagen, se mostrará:

NO ENCONTRADA
Nota

Este script fue desarrollado como una herramienta para automatizar la obtención de imágenes de productos a partir de SKUs, reduciendo el trabajo manual de búsqueda.