from backend.src.Interprete.nodes.Nodo import Nodo

class IfElseIf(Nodo):
    _contador = 0

    def __init__(self, condicion, instrucciones_if, elseif, linea = None, columna = None):
        super().__init__(None, linea, columna)
        self.condicion = condicion
        self.instrucciones_if = instrucciones_if
        self.elseif = elseif
        IfElseIf._contador += 1
        self.id = IfElseIf._contador

    def __str__(self):
        return f"IfElseIf(condicion={self.condicion}, instrucciones_if={self.instrucciones_if}, instrucciones_elseif={self.instrucciones_elseif}, instrucciones_else={self.instrucciones_else})"