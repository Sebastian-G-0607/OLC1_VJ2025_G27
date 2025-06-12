from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_Mayorigualque(nodo1, nodo2, t1, t2):
    if nodo1.tipo == Tipos.INT:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return bool(t1 >= t2), Tipos.BOOL
            case Tipos.FLOAT: #float
                return bool(t1 >= t2), Tipos.BOOL
            case Tipos.BOOL: #bool
                return Error('Semántico', 'No se puede comparar un entero con un booleano'), None
            case Tipos.STRING: #string
                return Error('Semántico', 'No se puede comparar un entero con una cadena'), None
            case Tipos.CHAR: #char
                return bool(t1 >= ord(t2)), Tipos.BOOL
            case _: 
                return Error('Semántico', 'Error al comparar la expresión'), None
            
    elif nodo1.tipo == Tipos.FLOAT:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return bool(t1 >= t2), Tipos.BOOL
            case Tipos.FLOAT: #float
                return bool(t1 >= t2), Tipos.BOOL
            case Tipos.BOOL: #bool
                return Error('Semántico', 'No se puede comparar un decimal con un booleano'), None
            case Tipos.STRING: #string
                return Error('Semántico', 'No se puede realizar división modular de un decimal con una cadena'), None
            case Tipos.CHAR: #char
                return bool(t1 >= ord(t2)), Tipos.BOOL
            case _: 
                return Error('Semántico', 'Error al realizar división modular a la expresión'), None
            
    elif nodo1.tipo == Tipos.BOOL:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return Error('Semántico', 'No se puede comparar un booleano con un entero'), None
            case Tipos.FLOAT:
                return Error('Semántico', 'No se puede comparar un booleano con un decimal'), None
            case Tipos.BOOL:
                return t1>=t2, Tipos.BOOL
            case Tipos.STRING:
                return Error('Semántico', 'No se puede comparar un booleano con una cadena'), None
            case Tipos.CHAR:
                return Error('Semántico', 'No se puede comparar un booleano con un caracter'), None
            case _:
                return Error('Semántico', 'Error al comparar la expresión'), None
            
    elif nodo1.tipo == Tipos.CHAR:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return bool(ord(t1) >= t2), Tipos.BOOL
            case Tipos.FLOAT:
                return bool(ord(t1) >= t2), Tipos.BOOL
            case Tipos.BOOL:
                return Error('Semántico', 'No se puede comparar un caracter con un booleano'), None
            case Tipos.STRING:
                return Error('Semántico', 'No se puede comparar un caracter con una cadena'), None
            case Tipos.CHAR:
                return bool(ord(t1) >= ord(t2)), Tipos.BOOL
            case _: 
                return Error('Semántico', 'Error al comparar la expresión'), None
            
    elif nodo1.tipo == Tipos.STRING:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return Error('Semántico', 'No se puede comparar una cadena con un entero'), None
            case Tipos.FLOAT:
                return Error('Semántico', 'No se puede comparar una cadena con un decimal'), None
            case Tipos.BOOL:
                return Error('Semántico', 'No se puede comparar una cadena con un booleano'), None
            case Tipos.STRING:
                return bool(t1 >= t2), Tipos.BOOL    
            case Tipos.CHAR:
                return Error('Semántico', 'No se puede comparar una cadena con un caracter'), None
            case _:
                return Error('Semántico', 'Error al comparar la expresión'), None