from backend.src.Interprete.nodes.Nodo import Nodo

class Coseno(Nodo):
    def __init__(self, expresion, tipo, linea=None, columna=None):
        super().__init__(tipo, linea, columna)
        self.expresion = expresion

    def getNodo(self):
        nodo = Nodo("COSENO")
        nodo.agregarHijo(self.expresion.getNodo())
        return nodo

    def getTipo(self):
        return "COSENO"