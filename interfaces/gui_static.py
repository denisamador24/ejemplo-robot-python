import tkinter as tk
from robot import Robot

class RobotGUIStatic:
    def __init__(self, robot):
        self.robot = robot
        self.root = tk.Tk()
        self.root.title("Robot - Interfaz Estática")
        self.root.geometry("400x300")

        # Etiquetas para mostrar valores estáticos
        self.label_titulo = tk.Label(self.root, text="Estado del Robot (Valores Estáticos)", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        # Frame para sensores
        frame_sensores = tk.Frame(self.root)
        frame_sensores.pack(pady=10)

        tk.Label(frame_sensores, text="Sensores:", font=("Arial", 12)).pack()

        # Valores estáticos de ejemplo
        self.label_distancia = tk.Label(frame_sensores, text="Distancia frontal: 2.5 m")
        self.label_distancia.pack()

        self.label_camara = tk.Label(frame_sensores, text="Cámara: 3 personas detectadas")
        self.label_camara.pack()

        # Frame para actuadores
        frame_actuadores = tk.Frame(self.root)
        frame_actuadores.pack(pady=10)

        tk.Label(frame_actuadores, text="Actuadores:", font=("Arial", 12)).pack()

        self.label_motor_izq = tk.Label(frame_actuadores, text="Motor izquierdo: Detenido")
        self.label_motor_izq.pack()

        self.label_motor_der = tk.Label(frame_actuadores, text="Motor derecho: Detenido")
        self.label_motor_der.pack()

        # Energía
        self.label_energia = tk.Label(self.root, text="Energía: 100/100")
        self.label_energia.pack(pady=10)

        # Botón para actualizar (aunque los valores son estáticos)
        btn_actualizar = tk.Button(self.root, text="Actualizar", command=self.actualizar_datos)
        btn_actualizar.pack(pady=10)

    def actualizar_datos(self):
        """Actualiza los datos mostrados (valores fijos para interfaz estática)"""
        # En esta interfaz, los valores son estáticos, pero podríamos mostrar valores reales si quisiéramos
        pass

    def run(self):
        """Ejecuta la interfaz gráfica"""
        self.root.mainloop()

def iniciar_gui_estatica(robot):
    """Función para iniciar la GUI estática"""
    gui = RobotGUIStatic(robot)
    gui.run()