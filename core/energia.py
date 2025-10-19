class SumistroEnergia:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.nivelActual = capacidad

    def suministrarEnergia(self, cantidad):
        if self.nivelActual >= cantidad:
            self.nivelActual -= cantidad
            return True
        return False
    
    def recargar(self):
        self.nivelActual = self.capacidad
        print("Sistema de Energia Recargado")
    