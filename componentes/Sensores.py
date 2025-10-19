import random
from .base import Sensor

class SensorTemperatura(Sensor):
  def __init__(self, _id, marca, modelo):
    super().__init__(_id, marca, modelo, tipo="Temperatura")

  def leer_datos(self):
    temperatura = random.uniform(15.0, 30.0)  # Simula una lectura de temperatura
    return temperatura
  
class SensorHumedad(Sensor):
  def __init__(self, _id, marca, modelo):
    super().__init__(_id, marca, modelo, tipo="Humedad")

  def leer_datos(self):
    humedad = random.uniform(30.0, 90.0)  # Simula una lectura de humedad
    return humedad
  
class SensorCO2(Sensor):
  def __init__(self, _id, marca, modelo):
    super().__init__(_id, marca, modelo, tipo="CO2")

  def leer_datos(self):
    co2 = random.uniform(400.0, 2000.0)  # Simula una lectura de CO2 en ppm
    return co2
  
  class SensorSuelo(Sesnor): 
    def __init__(self, _id, marca, modelo):
      super().__init__(_id, marca, modelo, tipo="Suelo")  
    
    def leer_datos(self):
      humedad_suelo = random.uniform(10.0, 60.0)  # Simula una lectura de humedad del suelo
      return humedad_suelo