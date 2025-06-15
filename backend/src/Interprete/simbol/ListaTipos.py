from enum import Enum

class Tipos(Enum):
    INT = 1
    FLOAT = 2
    BOOL = 3
    STRING = 4
    CHAR = 5
    
    def __str__(self):
        nombres = {
            Tipos.INT: "Entero",
            Tipos.FLOAT: "Decimal",
            Tipos.BOOL: "Booleano",
            Tipos.STRING: "Cadena",
            Tipos.CHAR: "Caracter"
        }
        return nombres.get(self, "Desconocido")