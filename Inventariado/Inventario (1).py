import time
from ModPatria import main as ejecutar_login_y_exportacion_Patria
from ModSol import main as ejecutar_login_y_exportacion_Sol
from ModBelenes import main as ejecutar_login_y_exportacion_Belenes
from ModGran import main as ejecutar_login_y_exportacion_Gran
from Inventario import main as procesar_inventario_y_generar_reporte

def ejecutar_flujo(nombre, login_func,):
    print(f"\nEjecutando {nombre}...")
    app = login_func()
    if not app:
        print("Falló la sesión o conexión. Abortando.")
        return

    time.sleep(2)

def main():
    ejecutar_flujo("ModPatria", ejecutar_login_y_exportacion_Patria)
    time.sleep(20)
    print("espera terminada")  # Espera adicional para asegurar que el primer proceso haya terminado
    ejecutar_flujo("ModSol", ejecutar_login_y_exportacion_Sol)
    time.sleep(20)  # Espera adicional para asegurar que el segundo proceso haya terminado
    ejecutar_flujo("ModBelenes", ejecutar_login_y_exportacion_Belenes)
    time.sleep(20)  # Espera adicional para asegurar que el tercer proceso haya terminado
    ejecutar_flujo("ModGran", ejecutar_login_y_exportacion_Gran)
    print("\nProcesando inventario y generando reporte...")
    procesar_inventario_y_generar_reporte()

if __name__ == "__main__":
    main()