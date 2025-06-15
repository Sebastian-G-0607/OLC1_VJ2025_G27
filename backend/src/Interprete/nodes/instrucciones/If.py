from backend.src.Interprete.nodes.Nodo import Nodo

class If(Nodo):
    _contador = 0

    def __init__(self, condicion, instrucciones, linea = None, columna = None):
        super().__init__(None, linea, columna)
        self.condicion = condicion
        self.instrucciones = instrucciones
        If._contador += 1
        self.id = If._contador

    def __str__(self):
        return f"If(condicion={self.condicion}, instrucciones={self.instrucciones})"