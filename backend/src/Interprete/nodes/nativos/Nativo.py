from backend.src.Interprete.nodes.Nodo import Nodo

class Nativo(Nodo):
    # NODO PARA UN NÚMERO ENTERO O FLOTANTE
    def __init__(self, tipo, valor, linea=None, columna=None):
        super().__init__(tipo, linea, columna)
        self.valor = valor  # Valor del número (puede ser entero o flotante)

    def __repr__(self):
        return f"Valor({self.valor!r})"