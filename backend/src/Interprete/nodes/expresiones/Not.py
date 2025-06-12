from backend.src.Interprete.nodes.Nodo import Nodo

class Not(Nodo):
    def __init__(self, expresion):
        self.expresion = expresion

    def __str__(self):
        return f"NOT {self.expresion}"

    def __repr__(self):
        return f"Not({self.expresion})"
