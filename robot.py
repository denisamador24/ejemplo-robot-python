from core.estructura import Estructura, Material, ElementoEstructura
from componentes.Sensores import SensorDistancia, SensorCamara
from componentes.Actuador import MotorActuador
from core.controlador import Controlador
from core.energia import SumistroEnergia

class Robot(Estructura):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

        # Material base para el robot
        material_acero = Material(1, "Acero", 7.85, 400)

        # Elementos estructurales
        self.agregar_elemento(ElementoEstructura(1, "Chasis", "Soporte principal", material_acero))
        self.agregar_elemento(ElementoEstructura(2, "Ruedas", "Movilidad", material_acero))

        # Componentes del robot
        self.sensores = {
            "distancia_frontal": SensorDistancia(1, "Ultrasonic", "HC-SR04"),
            "distancia_trasero": SensorDistancia(2, "Ultrasonic", "HC-SR04"),
            "camara": SensorCamara(3, "Webcam", "Logitech C920")
        }

        self.actuadores = {
            "motor_izquierdo": MotorActuador(1, "DC Motor", "NEMA 17"),
            "motor_derecho": MotorActuador(2, "DC Motor", "NEMA 17")
        }

        self.controlador = Controlador(1, "Raspberry Pi", 50)
        self.energia = SumistroEnergia(100)  # Capacidad de 100 unidades

    def leer_sensores(self):
        """Lee todos los sensores y devuelve los valores"""
        datos = {}
        for nombre, sensor in self.sensores.items():
            datos[nombre] = sensor.leer_datos()
        return datos

    def mover_adelante(self):
        """Mueve el robot hacia adelante"""
        if self.energia.suministrarEnergia(5):
            self.actuadores["motor_izquierdo"].mover_adelante()
            self.actuadores["motor_derecho"].mover_adelante()
        else:
            print("Energía insuficiente para mover adelante")

    def mover_atras(self):
        """Mueve el robot hacia atrás"""
        if self.energia.suministrarEnergia(5):
            self.actuadores["motor_izquierdo"].mover_atras()
            self.actuadores["motor_derecho"].mover_atras()
        else:
            print("Energía insuficiente para mover atrás")

    def girar_izquierda(self):
        """Gira el robot a la izquierda"""
        if self.energia.suministrarEnergia(3):
            self.actuadores["motor_izquierdo"].detener()
            self.actuadores["motor_derecho"].girar_izquierda()
        else:
            print("Energía insuficiente para girar izquierda")

    def girar_derecha(self):
        """Gira el robot a la derecha"""
        if self.energia.suministrarEnergia(3):
            self.actuadores["motor_derecho"].detener()
            self.actuadores["motor_izquierdo"].girar_derecha()
        else:
            print("Energía insuficiente para girar derecha")

    def detener(self):
        """Detiene el robot"""
        self.actuadores["motor_izquierdo"].detener()
        self.actuadores["motor_derecho"].detener()

    def recargar_energia(self):
        """Recarga la energía del robot"""
        self.energia.recargar()

    def navegar_autonomamente(self):
        """Simula navegación autónoma básica"""
        datos_sensores = self.leer_sensores()
        distancia_frontal = datos_sensores["distancia_frontal"]

        if distancia_frontal > 1.0:
            self.mover_adelante()
        else:
            self.girar_izquierda()