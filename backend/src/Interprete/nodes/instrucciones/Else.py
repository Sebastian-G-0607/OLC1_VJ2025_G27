from backend.src.Interprete.nodes.Nodo import Nodo

class Else(Nodo):
    _contador = 0

    def __init__(self, instrucciones, linea = None, columna = None):
        super().__init__(linea, columna)
        self.instrucciones = instrucciones
        Else._contador += 1
        self.id = Else._contador
        
    def __str__(self):
        return f"Else(instrucciones={self.instrucciones})"