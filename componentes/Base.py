class Componente: 
  def __init__ (self, _id, marca, modelo):
    self.id = _id
    self.marca = marca
    self.modelo = modelo

  def iniciar(self):
    print(f"Componente {self.modelo} iniciado.")

  def detener(self):
    print(f"Componente {self.modelo} detenido.")

class Sensor(Componente):
  def __init__(self, _id, marca, modelo, tipo):
    super().__init__(_id, marca, modelo)
    self.tipo = tipo

  def leer_datos(self):
    print(f"Leyendo datos del sensor {self.modelo} de tipo {self.tipo}.")

class Actuador(Componente):
  def __init__(self, _id, marca, modelo, accion):
    super().__init__(_id, marca, modelo)
    self.accion = accion

  def ejecutar_accion(self):
    print(f"Ejecutando acción '{self.accion}' en el actuador {self.modelo}.")
  
