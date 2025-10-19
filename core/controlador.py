class Controlador:
    def __init__(self, _id, model, frecuencia):
        self.id =   _id
        self.modelo = model
        self.frecuencia = frecuencia

    def procesarIntrucciones(self):
        print(f"Controlador {self.modelo} procesando a una frecuencia de {self.frecuencia} Hz.")

