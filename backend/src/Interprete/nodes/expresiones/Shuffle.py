from backend.src.Interprete.nodes.Nodo import Nodo

class Shuffle(Nodo):
    def __init__(self, vector, linea, columna):
        super().__init__(linea, columna)
        self.vector = vector

    def get_vector(self):
        return self.vector
