from backend.src.Interprete.nodes.Nodo import Nodo

class Declaracion(Nodo):
    def __init__(self, tipoDato, id, valor=None,tipo=None, linea=None, columna=None):
        super().__init__(tipo, linea, columna)
        self.tipoDato = tipoDato
        self.id = id  # Identificador de la variable
        self.valor = valor  # Valor inicial de la variable (opcional)

    def __repr__(self):
        return f"Declaracion({self.id!r}, {self.tipoDato!r}, {self.valor!r})"