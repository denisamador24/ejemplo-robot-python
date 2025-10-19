class Material: 
  def __init__(self, _id, nombre, densidad, resistencia):
    self.id = _id
    self.nombre = nombre
    self.densidad = densidad
    self.resistencia = resistencia

class ElementoEstructura:
  def __init__ (self, _id, nombre, funcion, material: Material):
    self.id = _id
    self.nombre = nombre
    self.funcion = funcion
    self.material = material

class Estructura:
  def __init__(self, id, nombre):
    self.id = id
    self.nombre = nombre
    self.elementos = []

  def agregar_elemento(self, elemento: ElementoEstructura):
    self.elementos.append(elemento)
    
    
