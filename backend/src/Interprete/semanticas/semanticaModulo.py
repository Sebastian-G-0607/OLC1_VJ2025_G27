from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_modulo(nodo1, nodo2, t1, t2):
    if nodo1.tipo == Tipos.INT:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return float(t1 % t2), Tipos.FLOAT
            case Tipos.FLOAT: #float
                return float(t1 % t2), Tipos.FLOAT
            case Tipos.BOOL: #bool
                return Error('semántico', 'No se puede realizar división modular de un entero con un booleano', nodo2.linea, nodo2.columna), None
            case Tipos.STRING: #string
                return Error('semántico', 'No se puede realizar división modular de un entero con una cadena', nodo2.linea, nodo2.columna), None
            case Tipos.CHAR: #char
                return Error('semántico', 'No se puede realizar división modular de un entero con un caracter', nodo2.linea, nodo2.columna), None
            case _: 
                return Error('semántico', 'Error al realizar división modular a la expresión', nodo2.linea, nodo2.columna), None

    elif nodo1.tipo == Tipos.FLOAT:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return float(t1 % t2), Tipos.FLOAT
            case Tipos.FLOAT: #float
                return float(t1 % t2), Tipos.FLOAT
            case Tipos.BOOL: #bool
                return Error('semántico', 'No se puede realizar división modular de un decimal con un booleano', nodo2.linea, nodo2.columna), None
            case Tipos.STRING: #string
                return Error('semántico', 'No se puede realizar división modular de un decimal con una cadena', nodo2.linea, nodo2.columna), None
            case Tipos.CHAR: #char
                return Error('semántico', 'No se puede realizar división modular de un decimal con un caracter', nodo2.linea, nodo2.columna), None
            case _: 
                return Error('semántico', 'Error al realizar división modular a la expresión', nodo2.linea, nodo2.columna), None
    else:
        return Error('semántico', 'Los tipos de datos proporcionados no son compatibles para la operación de módulo', nodo2.linea, nodo2.columna), None