from backend.src.Interprete.nodes.Nodo import Nodo

class Umenos(Nodo):
    # NODO PARA LA OPERACIÓN DE SUMA
    def __init__(self, expresion, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.expresion = expresion

    def __repr__(self):
        return f"Umenos({self.expresion!r})"