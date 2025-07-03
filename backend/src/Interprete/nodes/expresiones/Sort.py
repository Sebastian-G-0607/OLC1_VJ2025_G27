from backend.src.Interprete.nodes.Nodo import Nodo

class Sort(Nodo):
    def __init__(self, vector, linea: int, columna: int):
        super().__init__(linea, columna)
        self.vector = vector