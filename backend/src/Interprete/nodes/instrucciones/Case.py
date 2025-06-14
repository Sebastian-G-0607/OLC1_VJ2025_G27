from backend.src.Interprete.nodes.Nodo import Nodo

class Case(Nodo):
    _contador = 0

    def __init__(self, condicion, instrucciones_case, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.condicion = condicion
        self.instrucciones_case = instrucciones_case
        Case._contador += 1
        self.id = Case._contador

    def __str__(self):
        return f"Case(condicion={self.condicion}, instrucciones_case={self.instrucciones_case})"