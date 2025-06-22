from backend.src.Interprete.nodes.Nodo import Nodo

class Argumento(Nodo):
    def __init__(self, valor, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.valor = valor

    def __repr__(self):
        return f"Argumento({self.valor!r})"
    
    def getValor(self):
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor