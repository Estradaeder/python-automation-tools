# Image Template Processor (Python)

Herramienta en Python para **procesar imágenes en lote**, redimensionarlas a un tamaño estándar y aplicar una **plantilla gráfica** encima.
Este script fue creado para automatizar la preparación de imágenes antes de subirlas a una página web o catálogo.

## Funcionalidades

* Procesa múltiples imágenes automáticamente desde una carpeta.
* Redimensiona imágenes manteniendo proporciones (sin deformar).
* Centra la imagen en un canvas de tamaño fijo.
* Aplica una plantilla PNG con transparencia encima.
* Exporta todas las imágenes finales en formato **JPG optimizado**.

## Flujo del programa

1. El script toma imágenes desde la carpeta `base/`.
2. Redimensiona cada imagen para ajustarla al tamaño definido.
3. La centra sobre un fondo blanco.
4. Aplica una plantilla (`plantilla.png`) como overlay.
5. Guarda el resultado final en la carpeta `salida/`.

## Estructura del proyecto

```
project
│
├── base/           # imágenes originales
├── salida/         # imágenes generadas
├── plantilla.png   # plantilla que se coloca encima
├── main.py         # script principal
└── README.md
```

## Requisitos

Python 3.x

Instalar dependencias:

```
pip install pillow
```

## Uso

1. Colocar las imágenes originales en la carpeta `base/`.
2. Colocar la plantilla en `plantilla.png`.
3. Ejecutar el script:

```
python main.py
```

Las imágenes procesadas aparecerán en la carpeta:

```
/salida
```

## Tecnologías utilizadas

* Python
* Pillow (PIL)
* Procesamiento de imágenes
* Automatización de tareas

## Notas

Este proyecto forma parte de un conjunto de herramientas personales de **automatización con Python** utilizadas para optimizar flujos de trabajo repetitivos relacionados con manejo de imágenes.
