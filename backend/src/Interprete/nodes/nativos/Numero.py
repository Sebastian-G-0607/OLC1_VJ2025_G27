from backend.src.Interprete.nodes.Nodo import Nodo

class Numero(Nodo):
    # NODO PARA UN NÚMERO ENTERO O FLOTANTE
    def __init__(self, valor):
        self.valor = valor  # Valor del número (puede ser entero o flotante)

    def __repr__(self):
        return f"Numero({self.valor!r})"