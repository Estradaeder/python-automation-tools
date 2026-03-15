import time
import subprocess
from pywinauto import Application, Desktop
from pywinauto.mouse import click
from pywinauto.keyboard import send_keys

MANIFEST_URL = "http://demo.demo.com/y/demo.application"
USERNAME = "DEMO"
PASSWORD = "DEMO"
MAIN_WINDOW_TITLE_PART = "Panini"
LAUNCH_TIMEOUT = 180

def launch_remote_application(url):
    subprocess.Popen(['rundll32.exe', 'dfshim.dll,ShOpenVerbApplication', url], shell=False)

def wait_for_child_process(exe_name, timeout=60):
    end = time.time() + timeout
    while time.time() < end:
        out = subprocess.check_output(['tasklist', '/FO', 'CSV', '/NH'], text=True)
        for line in out.splitlines():
            if exe_name.lower() in line.lower():
                return True
        time.sleep(0.5)
    return False

def connect_to_app(title_part, exe_name, timeout=120):
    wait_for_child_process(exe_name, timeout)
    return Application(backend="uia").connect(title_re=f".*{title_part}.*", timeout=timeout)

def click_por_coordenadas(x: int, y: int) -> bool:
    try:
        click(button='left', coords=(x, y))
        return True
    except Exception as e:
        print(f"Error al hacer clic en ({x},{y}): {e}")
        return False

def find_and_set_credentials(dlg, username, password):
    edits = [e for e in dlg.descendants(control_type="Edit") if e.is_visible()]
    if len(edits) >= 2:
        edits[0].set_edit_text(username)
        edits[1].set_edit_text(password)
    elif len(edits) == 1:
        edits[0].set_edit_text(username + "\t" + password)
    for b in dlg.descendants(control_type="Button"):
        if "ingresar" in (b.window_text() or "").lower():
            b.click_input()
            break
def escribir_nombre_archivo(x: int, y: int, nombre: str) -> bool:
    try:
        click(button='left', coords=(x, y))
        time.sleep(0.5)
        send_keys(nombre, with_spaces=True)
        return True
    except Exception as e:
        print(f"Error al escribir nombre de archivo: {e}")
        return False

def main():
    launch_remote_application(MANIFEST_URL)
    app = connect_to_app(MAIN_WINDOW_TITLE_PART, "Ybridio.exe", LAUNCH_TIMEOUT)
    dlg = app.top_window()
    dlg.set_focus()
    find_and_set_credentials(dlg, USERNAME, PASSWORD)
    time.sleep(5)

    waits = {
        'after_login': 2.0,
        'after_login2': 5.0,
        'after_tab': 0.6,
        'after_menu': 0.6,
        'after_item': 4.0,
        'after_download': 3.0,
        'after_nombre':3.0,
        'after_guardar':1.0,
        'after_confirmar':1.0,
        'after_cerrar':2.0,
        'after_final':2.0
    }

    if click_por_coordenadas(994, 642):
        time.sleep(waits['after_login'])
    else:
        print("No se pudo hacer clic en 'Inventario'")
        return

    if click_por_coordenadas(1144, 606):
        time.sleep(waits['after_login2'])
    else:
        print("No se pudo hacer clic en 'Inventario'")
        return
    dlg.set_focus()
    time.sleep(1)

    # 1) Pestaña Inventario
    if click_por_coordenadas(305, 70):
        time.sleep(waits['after_tab'])
    else:
        print("No se pudo hacer clic en 'Inventario'")
        return False

    # 2) Abrir Almacén
    if click_por_coordenadas(483, 117):
        time.sleep(waits['after_menu'])
    else:
        print("No se pudo hacer clic en 'Almacén'")
        return False

    # 3) Seleccionar Existencias
    if click_por_coordenadas(525, 224):
        time.sleep(waits['after_item'])
    else:
        print("No se pudo hacer clic en 'Existencias'")
        return False
    # 4) Descargar listado 
    if click_por_coordenadas(448, 120):
        time.sleep(waits['after_download'])
    else:
        print("No se pudo hacer clic en 'descargar'")
        return False 
    
    # 5) Escribir nombre en campo de archivo
    if not escribir_nombre_archivo(707, 480, "Sol"):
        print("No se pudo escribir el nombre del archivo")
        return False
    time.sleep(waits['after_nombre'])

    # 6) Confirmar guardado
    if not click_por_coordenadas(954, 568):
        print("No se pudo confirmar el guardado")
        return False
    time.sleep(waits['after_guardar']) #(1038,649)

    if not click_por_coordenadas(1067, 618):
        print("No se pudo confirmar el guardado")
        return False
    time.sleep(waits['after_guardar']) #

    # 7) Cerrar aplicación
    if not click_por_coordenadas(1675, 27):
        print("No se pudo hacer clic en 'cerrar'")
        return False
    time.sleep(waits['after_cerrar'])

    # 8) Confirmación final
    if not click_por_coordenadas(1067, 610):
        print("No se pudo hacer clic en 'final'")
        return False
    time.sleep(waits['after_final'])

    return True

if __name__ == "__main__":
    main()
