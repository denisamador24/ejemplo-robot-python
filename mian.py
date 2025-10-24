# Archivo principal para el sistema de robot de navegación

from robot import Robot
from interfaces.cmd_interface import iniciar_cmd_interface
from interfaces.gui_static import iniciar_gui_estatica
from interfaces.gui_dynamic import iniciar_gui_dinamica
import sys

def main():
    # Crear instancia del robot
    robot = Robot(1, "Robot Navegador")

    print("Sistema de Robot Navegador Iniciado")
    print("Seleccione una interfaz:")
    print("1. Interfaz de comandos (CMD)")
    # print("2. Interfaz gráfica estática")
    print("2. Interfaz gráfica dinámica")

    while True:
        try:
            opcion = input("Opción (1-3): ").strip()

            if opcion == "1":
                print("Iniciando interfaz de comandos...")
                iniciar_cmd_interface(robot)
                break
            # elif opcion == "2":
            #     print("Iniciando interfaz gráfica estática...")
            #     iniciar_gui_estatica(robot)
            #     break
            elif opcion == "2":
                print("Iniciando interfaz gráfica dinámica...")
                iniciar_gui_dinamica(robot)
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except KeyboardInterrupt:
            print("\nSaliendo del sistema...")
            sys.exit(0)

if __name__ == "__main__":
    main()