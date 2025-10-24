import cmd
from robot import Robot

class RobotCMDInterface(cmd.Cmd):
    intro = 'Bienvenido a la interfaz de comandos del Robot. Escribe "help" o "?" para ver comandos disponibles.'
    prompt = '(robot) '

    def __init__(self, robot):
        super().__init__()
        self.robot = robot

    def do_leer_sensores(self, arg):
        """Lee y muestra los valores de todos los sensores"""
        datos = self.robot.leer_sensores()
        print("Datos de sensores:")
        for sensor, valor in datos.items():
            print(f"  {sensor}: {valor}")

    def do_mover_adelante(self, arg):
        """Mueve el robot hacia adelante"""
        self.robot.mover_adelante()

    def do_mover_atras(self, arg):
        """Mueve el robot hacia atrás"""
        self.robot.mover_atras()

    def do_girar_izquierda(self, arg):
        """Gira el robot a la izquierda"""
        self.robot.girar_izquierda()

    def do_girar_derecha(self, arg):
        """Gira el robot a la derecha"""
        self.robot.girar_derecha()

    def do_detener(self, arg):
        """Detiene el robot"""
        self.robot.detener()

    def do_recargar_energia(self, arg):
        """Recarga la energía del robot"""
        self.robot.recargar_energia()

    def do_navegar_autonomamente(self, arg):
        """Ejecuta navegación autónoma básica"""
        self.robot.navegar_autonomamente()

    def do_estado_energia(self, arg):
        """Muestra el estado actual de la energía"""
        print(f"Energía actual: {self.robot.energia.nivelActual}/{self.robot.energia.capacidad}")

    def do_salir(self, arg):
        """Sale de la interfaz de comandos"""
        print("Saliendo...")
        return True

def iniciar_cmd_interface(robot):
    """Función para iniciar la interfaz de comandos"""
    interface = RobotCMDInterface(robot)
    interface.cmdloop()