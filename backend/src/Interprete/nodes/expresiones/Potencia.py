from backend.src.Interprete.nodes.Nodo import Nodo

class Potencia(Nodo):
    # NODO PARA LA OPERACIÓN DE POTENCIA
    def __init__(self, base, exponente):
        self.izquierda = base      # Base de la potencia
        self.derecha = exponente  # Exponente de la potencia

    def __repr__(self):
        return f"Potencia({self.izquierda!r}, {self.derecha!r})"