Este repositorio contiene scripts en Python para automatizar la exportación de inventarios desde el sistema Panini/Ybridio mediante automatización de interfaz gráfica.

Los programas utilizan la librería pywinauto para interactuar con la aplicación, realizar el inicio de sesión y navegar por el sistema hasta generar un archivo de inventario.

Tecnologías utilizadas

Python

pywinauto

subprocess

automatización de GUI

Windows automation

Funcionalidad

Los scripts realizan automáticamente:

Abrir la aplicación remota del sistema.

Esperar a que el programa cargue.

Iniciar sesión con las credenciales correspondientes.

Navegar al módulo de Inventario.

Acceder a Almacén → Existencias.

Exportar el listado de inventario.

Guardar el archivo generado.

Cerrar la aplicación.

Estructura del repositorio
/inventario-automation
│
├── Inventario.py
│
├── ModBelenes.py
├── ModGran.py
├── ModPatria.py
├── ModSol.py
│
└── README.md

Cada script corresponde a una sucursal diferente y contiene las credenciales y nombre de archivo específico para esa exportación.

El programa abrirá automáticamente la aplicación y realizará el proceso de exportación.

Nota

Este proyecto fue desarrollado como práctica de automatización de tareas administrativas mediante scripting, con el objetivo de reducir trabajo manual y estandarizar procesos de exportación de datos.