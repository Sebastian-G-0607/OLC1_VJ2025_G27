from backend.src.Interprete.nodes.Nodo import Nodo

class Switch(Nodo):
    def __init__(self, expresion, lista_casos, caso_default=None, linea=None, columna=None):
        super().__init__(None, linea, columna)
        self.expresion = expresion
        self.lista_casos = lista_casos