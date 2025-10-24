import tkinter as tk
import threading
import time
from robot import Robot

class RobotGUIDynamic:
    def __init__(self, robot):
        self.robot = robot
        self.root = tk.Tk()
        self.root.title("Robot - Interfaz Dinámica")
        self.root.geometry("400x350")

        # Etiquetas para mostrar valores dinámicos
        self.label_titulo = tk.Label(self.root, text="Estado del Robot (Valores Dinámicos)", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        # Frame para sensores
        frame_sensores = tk.Frame(self.root)
        frame_sensores.pack(pady=10)

        tk.Label(frame_sensores, text="Sensores:", font=("Arial", 12)).pack()

        self.label_distancia = tk.Label(frame_sensores, text="Distancia frontal: -- m")
        self.label_distancia.pack()

        self.label_camara = tk.Label(frame_sensores, text="Cámara: -- personas")
        self.label_camara.pack()

        # Frame para actuadores
        frame_actuadores = tk.Frame(self.root)
        frame_actuadores.pack(pady=10)

        tk.Label(frame_actuadores, text="Actuadores:", font=("Arial", 12)).pack()

        self.label_motor_izq = tk.Label(frame_actuadores, text="Motor izquierdo: --")
        self.label_motor_izq.pack()

        self.label_motor_der = tk.Label(frame_actuadores, text="Motor derecho: --")
        self.label_motor_der.pack()

        # Energía
        self.label_energia = tk.Label(self.root, text="Energía: --/--")
        self.label_energia.pack(pady=10)

        # Estado de navegación
        self.label_navegacion = tk.Label(self.root, text="Navegación: Detenida")
        self.label_navegacion.pack(pady=5)

        # Botones de control
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        self.btn_iniciar = tk.Button(frame_botones, text="Iniciar Navegación", command=self.iniciar_navegacion)
        self.btn_iniciar.pack(side=tk.LEFT, padx=5)

        self.btn_detener = tk.Button(frame_botones, text="Detener Navegación", command=self.detener_navegacion, state=tk.DISABLED)
        self.btn_detener.pack(side=tk.LEFT, padx=5)

        # Variable para controlar el hilo de actualización
        self.actualizando = False
        self.navegando = False

    def actualizar_datos(self):
        """Actualiza los datos mostrados con valores dinámicos"""
        while self.actualizando:
            datos_sensores = self.robot.leer_sensores()

            # Actualizar labels
            self.label_distancia.config(text=f"Distancia frontal: {datos_sensores['distancia_frontal']:.2f} m")
            camara_data = datos_sensores['camara']
            self.label_camara.config(text=f"Cámara: {camara_data['personas']} personas")

            self.label_energia.config(text=f"Energía: {self.robot.energia.nivelActual}/{self.robot.energia.capacidad}")

            # Simular estado de motores (aleatorio para demo)
            import random
            estados_motor = ["Moviendo adelante", "Moviendo atrás", "Girando", "Detenido"]
            estado_izq = random.choice(estados_motor)
            estado_der = random.choice(estados_motor)
            self.label_motor_izq.config(text=f"Motor izquierdo: {estado_izq}")
            self.label_motor_der.config(text=f"Motor derecho: {estado_der}")

            time.sleep(1)  # Actualizar cada segundo

    def iniciar_navegacion(self):
        """Inicia la navegación autónoma"""
        self.navegando = True
        self.label_navegacion.config(text="Navegación: Activa")
        self.btn_iniciar.config(state=tk.DISABLED)
        self.btn_detener.config(state=tk.NORMAL)

        # Iniciar hilo de navegación
        threading.Thread(target=self.navegar, daemon=True).start()

    def detener_navegacion(self):
        """Detiene la navegación autónoma"""
        self.navegando = False
        self.label_navegacion.config(text="Navegación: Detenida")
        self.btn_iniciar.config(state=tk.NORMAL)
        self.btn_detener.config(state=tk.DISABLED)
        self.robot.detener()

    def navegar(self):
        """Hilo para navegación autónoma"""
        while self.navegando:
            self.robot.navegar_autonomamente()
            time.sleep(2)  # Navegar cada 2 segundos

    def run(self):
        """Ejecuta la interfaz gráfica"""
        self.actualizando = True
        # Iniciar hilo de actualización
        threading.Thread(target=self.actualizar_datos, daemon=True).start()

        self.root.mainloop()

def iniciar_gui_dinamica(robot):
    """Función para iniciar la GUI dinámica"""
    gui = RobotGUIDynamic(robot)
    gui.run()