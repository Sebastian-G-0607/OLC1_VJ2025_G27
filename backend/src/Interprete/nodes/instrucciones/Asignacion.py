from backend.src.Interprete.nodes.Nodo import Nodo

class Asignacion(Nodo):
    def __init__(self, id, valor, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.id = id
        self.valor = valor

    def __repr__(self):
        return f"Asignacion({self.id!r}, {self.valor!r})"