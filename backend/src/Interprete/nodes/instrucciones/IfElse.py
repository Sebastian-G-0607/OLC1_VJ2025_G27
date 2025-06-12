from backend.src.Interprete.nodes.Nodo import Nodo

class IfElse(Nodo):
    _contador = 0

    def __init__(self, condicion, instrucciones_if, instrucciones_else, linea = None, columna = None):
        super().__init__(linea, columna)
        self.condicion = condicion
        self.instrucciones_if = instrucciones_if
        self.instrucciones_else = instrucciones_else
        IfElse._contador += 1
        self.id = IfElse._contador

    def __str__(self):
        return f"IfElse(condicion={self.condicion}, instrucciones_if={self.instrucciones_if}, instrucciones_else={self.instrucciones_else})"