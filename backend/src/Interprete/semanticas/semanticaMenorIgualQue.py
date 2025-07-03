from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_Menorigualque(nodo1, nodo2, t1, t2):
    if nodo1.tipo == Tipos.INT:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return bool(t1 <= t2), Tipos.BOOL
            case Tipos.FLOAT: #float
                return bool(t1 <= t2), Tipos.BOOL
            case Tipos.BOOL: #bool
                return Error('semántico', 'No se puede comparar un entero con un booleano', nodo2.linea, nodo2.columna), None
            case Tipos.STRING: #string
                return Error('semántico', 'No se puede comparar un entero con una cadena', nodo2.linea, nodo2.columna), None
            case Tipos.CHAR: #char
                return bool(t1 <= ord(t2)), Tipos.BOOL
            case _: 
                return Error('semántico', 'Error al comparar la expresión', nodo2.linea, nodo2.columna), None

    elif nodo1.tipo == Tipos.FLOAT:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return bool(t1 <= t2), Tipos.BOOL
            case Tipos.FLOAT: #float
                return bool(t1 <= t2), Tipos.BOOL
            case Tipos.BOOL: #bool
                return Error('semántico', 'No se puede comparar un decimal con un booleano', nodo2.linea, nodo2.columna), None
            case Tipos.STRING: #string
                return Error('semántico', 'No se puede realizar división modular de un decimal con una cadena', nodo2.linea, nodo2.columna), None
            case Tipos.CHAR: #char
                return bool(t1 <= ord(t2)), Tipos.BOOL
            case _: 
                return Error('semántico', 'Error al realizar división modular a la expresión', nodo2.linea, nodo2.columna), None

    elif nodo1.tipo == Tipos.BOOL:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return Error('semántico', 'No se puede comparar un booleano con un entero', nodo2.linea, nodo2.columna), None
            case Tipos.FLOAT:
                return Error('semántico', 'No se puede comparar un booleano con un decimal', nodo2.linea, nodo2.columna), None
            case Tipos.BOOL:
                return t1<=t2, Tipos.BOOL
            case Tipos.STRING:
                return Error('semántico', 'No se puede comparar un booleano con una cadena', nodo2.linea, nodo2.columna), None
            case Tipos.CHAR:
                return Error('semántico', 'No se puede comparar un booleano con un caracter', nodo2.linea, nodo2.columna), None
            case _:
                return Error('semántico', 'Error al comparar la expresión', nodo2.linea, nodo2.columna), None

    elif nodo1.tipo == Tipos.CHAR:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return bool(ord(t1) <= t2), Tipos.BOOL
            case Tipos.FLOAT:
                return bool(ord(t1) <= t2), Tipos.BOOL
            case Tipos.BOOL:
                return Error('semántico', 'No se puede comparar un caracter con un booleano', nodo2.linea, nodo2.columna), None
            case Tipos.STRING:
                return Error('semántico', 'No se puede comparar un caracter con una cadena', nodo2.linea, nodo2.columna), None
            case Tipos.CHAR:
                return bool(ord(t1) <= ord(t2)), Tipos.BOOL
            case _: 
                return Error('semántico', 'Error al comparar la expresión', nodo2.linea, nodo2.columna), None

    elif nodo1.tipo == Tipos.STRING:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return Error('semántico', 'No se puede comparar una cadena con un entero', nodo2.linea, nodo2.columna), None
            case Tipos.FLOAT:
                return Error('semántico', 'No se puede comparar una cadena con un decimal', nodo2.linea, nodo2.columna), None
            case Tipos.BOOL:
                return Error('semántico', 'No se puede comparar una cadena con un booleano', nodo2.linea, nodo2.columna), None
            case Tipos.STRING:
                return bool(t1 <= t2), Tipos.BOOL    
            case Tipos.CHAR:
                return Error('semántico', 'No se puede comparar una cadena con un caracter', nodo2.linea, nodo2.columna), None
            case _:
                return Error('semántico', 'Error al comparar la expresión', nodo2.linea, nodo2.columna), None