from backend.src.Interprete.nodes.Nodo import Nodo
from backend.src.Interprete.simbol.RaizArbol import Arbol

class Println(Nodo):
    # NODO PARA LA INSTRUCCION PRINTLN
    def __init__(self, expresion):
        self.expresion = expresion

    def __repr__(self):
        return f"Println({self.expresion!r})"