from backend.src.Interprete.nodes.Nodo import Nodo

class For(Nodo):
    _contador = 0

    def __init__(self, declaracion, condicion, actualizacion, instrucciones, linea = None, columna = None):
        super().__init__(linea, columna)
        self.declaracion = declaracion  # Variable de control del bucle
        self.condicion = condicion     # Valor de la condición del bucle
        self.actualizacion = actualizacion            # Valor final del bucle
        self.instrucciones = instrucciones  # Instrucciones a ejecutar en cada iteración
        For._contador += 1
        self.id = For._contador