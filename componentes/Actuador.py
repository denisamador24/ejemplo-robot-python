from .base import Actuador

class ActuadorVentilador(Actuador):
  def __init__(self, _id, marca, modelo):
    super().__init__(_id, marca, modelo, accion="Ventilador")

  def encender(self):
    print(f"Ventilador {self.modelo} encendido.")

  def apagar(self):
    print(f"Ventilador {self.modelo} apagado.")

class ActuadorBombaDeAgua(Actuador):
  def __init__(self, _id, marca, modelo):
    super().__init__(_id, marca, modelo, accion="Bomba de Agua")  

  def bombear(self):
    print(f"Bomba de agua {self.modelo} en funcionamiento.")


class Persiana(Actuador):
  def __init__(self, _id, marca, modelo):
    super().__init__(_id, marca, modelo, accion="Persiana")

  def abrir(self):
    print(f"Persiana {self.modelo} abierta.")

  def cerrar(self):
    print(f"Persiana {self.modelo} cerrada.")