from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_modulo(nodo1, nodo2, t1, t2):
    if nodo1.tipo == Tipos.INT:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return int(t1 % t2), Tipos.FLOAT
            case Tipos.FLOAT: #float
                return float(t1 % t2), Tipos.FLOAT
            case Tipos.BOOL: #bool
                return Error('Semántico', 'No se puede realizar división modular de un entero con un booleano'), None
            case Tipos.STRING: #string
                return Error('Semántico', 'No se puede realizar división modular de un entero con una cadena'), None
            case Tipos.CHAR: #char
                return Error('Semántico', 'No se puede realizar división modular de un entero con un caracter'), None
            case _: 
                return Error('Semántico', 'Error al realizar división modular a la expresión'), None
            
    if nodo1.tipo == Tipos.FLOAT:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return int(t1 % t2), Tipos.FLOAT
            case Tipos.FLOAT: #float
                return float(t1 % t2), Tipos.FLOAT
            case Tipos.BOOL: #bool
                return Error('Semántico', 'No se puede realizar división modular de un decimal con un booleano'), None
            case Tipos.STRING: #string
                return Error('Semántico', 'No se puede realizar división modular de un decimal con una cadena'), None
            case Tipos.CHAR: #char
                return Error('Semántico', 'No se puede realizar división modular de un decimal con un caracter'), None
            case _: 
                return Error('Semántico', 'Error al realizar división modular a la expresión'), None
            

    