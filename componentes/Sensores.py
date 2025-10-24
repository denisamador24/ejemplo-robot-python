import random
from .Base import Sensor

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
  
class SensorSuelo(Sensor):
    def __init__(self, _id, marca, modelo):
        super().__init__(_id, marca, modelo, tipo="Suelo")
    
    def leer_datos(self):
      humedad_suelo = random.uniform(10.0, 60.0)  # Simula una lectura de humedad del suelo
      return humedad_suelo
class SensorDistancia(Sensor):
    def __init__(self, _id, marca, modelo):
        super().__init__(_id, marca, modelo, tipo="Distancia")

    def leer_datos(self):
        distancia = random.uniform(0.1, 5.0)  # Simula una lectura de distancia en metros
        return distancia

class SensorCamara(Sensor):
    def __init__(self, _id, marca, modelo):
        super().__init__(_id, marca, modelo, tipo="Camara")

    def leer_datos(self):
        # Placeholder para análisis de postura - por ahora solo simula detección
        personas_detectadas = random.randint(0, 10)
        return {"personas": personas_detectadas, "postura": "placeholder"}