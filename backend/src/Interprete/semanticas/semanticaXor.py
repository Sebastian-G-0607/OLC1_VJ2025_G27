from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_Xor(nodo1, nodo2, t1, t2):
    if nodo1.tipo == Tipos.INT:
        match nodo2.tipo:
            case Tipos.INT: # entero
                return int(t1 ^ t2), Tipos.INT
            case Tipos.FLOAT:
                return Error('semántico', 'No se puede realizar XOR entre un entero y un flotante', nodo2.linea, nodo2.columna), None
            case Tipos.BOOL:
                return Error('semántico', 'No se puede realizar XOR entre un entero y un booleano', nodo2.linea, nodo2.columna), None
            case Tipos.STRING:
                return Error('semántico', 'No se puede realizar XOR entre un entero y una cadena', nodo2.linea, nodo2.columna), None
            case Tipos.CHAR:
                return Error('semántico', 'No se puede realizar XOR entre un entero y un caracter', nodo2.linea, nodo2.columna), None
            case _:
                return Error('semántico', 'Error al realizar la operación XOR', nodo2.linea, nodo2.columna), None
    elif nodo1.tipo == Tipos.FLOAT:
        match nodo2.tipo:
            case Tipos.INT:
                return Error('semántico', 'No se puede realizar XOR entre un flotante y un entero', nodo2.linea, nodo2.columna), None
            case Tipos.FLOAT:
                return float(t1 ^ t2), Tipos.FLOAT
            case Tipos.BOOL:
                return Error('semántico', 'No se puede realizar XOR entre un flotante y un booleano', nodo2.linea, nodo2.columna), None
            case Tipos.STRING:
                return Error('semántico', 'No se puede realizar XOR entre un flotante y una cadena', nodo2.linea, nodo2.columna), None
            case Tipos.CHAR:
                return Error('semántico', 'No se puede realizar XOR entre un flotante y un caracter', nodo2.linea, nodo2.columna), None
            case _:
                return Error('semántico', 'Error al realizar la operación XOR', nodo2.linea, nodo2.columna), None
    elif nodo1.tipo == Tipos.BOOL:
        match nodo2.tipo:
            case Tipos.INT:
                return Error('semántico', 'No se puede realizar XOR entre un booleano y un entero', nodo2.linea, nodo2.columna), None
            case Tipos.FLOAT:
                return Error('semántico', 'No se puede realizar XOR entre un booleano y un flotante', nodo2.linea, nodo2.columna), None
            case Tipos.BOOL:
                return bool(t1 ^ t2), Tipos.BOOL
            case Tipos.STRING:
                return Error('semántico', 'No se puede realizar XOR entre un booleano y una cadena', nodo2.linea, nodo2.columna), None
            case Tipos.CHAR:
                return Error('semántico', 'No se puede realizar XOR entre un booleano y un caracter', nodo2.linea, nodo2.columna), None
            case _:
                return Error('semántico', 'Error al realizar la operación XOR', nodo2.linea, nodo2.columna), None
    elif nodo1.tipo == Tipos.CHAR:
        match nodo2.tipo:
            case Tipos.INT:
                return Error('semántico', 'No se puede realizar XOR entre un caracter y un entero', nodo2.linea, nodo2.columna), None
            case Tipos.FLOAT:
                return Error('semántico', 'No se puede realizar XOR entre un caracter y un flotante', nodo2.linea, nodo2.columna), None
            case Tipos.BOOL:
                return Error('semántico', 'No se puede realizar XOR entre un caracter y un booleano', nodo2.linea, nodo2.columna), None
            case Tipos.STRING:
                return Error('semántico', 'No se puede realizar XOR entre un caracter y una cadena', nodo2.linea, nodo2.columna), None
            case Tipos.CHAR:
                return int(ord(t1) ^ ord(t2)), Tipos.INT
            case _:
                return Error('semántico', 'Error al realizar la operación XOR', nodo2.linea, nodo2.columna), None
    elif nodo1.tipo == Tipos.STRING:
        match nodo2.tipo:
            case Tipos.INT:
                    return Error('semántico', 'No se puede realizar XOR entre una cadena y un entero', nodo2.linea, nodo2.columna), None
            case Tipos.FLOAT:
                    return Error('semántico', 'No se puede realizar XOR entre una cadena y un flotante', nodo2.linea, nodo2.columna), None
            case Tipos.BOOL:
                    return Error('semántico', 'No se puede realizar XOR entre una cadena y un booleano', nodo2.linea, nodo2.columna), None
            case Tipos.STRING:
                    return Error('semántico', 'No se puede realizar XOR entre dos cadenas', nodo2.linea, nodo2.columna), None
            case Tipos.CHAR:
                    return Error('semántico', 'No se puede realizar XOR entre una cadena y un caracter', nodo2.linea, nodo2.columna), None
            case _:
                    return Error('semántico', 'Error al realizar la operación XOR', nodo2.linea, nodo2.columna), None