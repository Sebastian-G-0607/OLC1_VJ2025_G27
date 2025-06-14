from backend.src.Interprete.nodes.Nodo import Nodo

class DoWhile(Nodo):
    _contador = 0

    def __init__(self, instrucciones, condicion, line = None, column = None):
        super().__init__(None, line, column)
        self.instrucciones = instrucciones
        self.condicion = condicion
        DoWhile._contador += 1
        self.id = DoWhile._contador