from backend.src.Interprete.nodes.Nodo import Nodo
from backend.src.Interprete.simbol.ListaTipos import Tipos

class ParametroDefinicion(Nodo):
    def __init__(self, tipo, id, linea=None, columna=None):
        super().__init__(None, linea, columna)
        match tipo:
            case "int":
                self.tipo = Tipos.INT
            case "float":
                self.tipo = Tipos.FLOAT
            case "str":
                self.tipo = Tipos.STRING
            case "bool":
                self.tipo = Tipos.BOOL
            case "char":
                self.tipo = Tipos.CHAR
            case _:
                self.tipo = None

        self.id = id
