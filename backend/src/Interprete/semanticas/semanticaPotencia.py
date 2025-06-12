from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_potencia(nodo1, nodo2, t1, t2):
    if nodo1.tipo == Tipos.INT:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return int(t1 ** t2), Tipos.INT
            case Tipos.FLOAT: #float
                return float(t1 ** t2), Tipos.FLOAT
            case Tipos.BOOL: #bool
                return Error('semántico', 'No se puede elevar un valor entero con un booleano'), None
            case Tipos.STRING: #string
                return Error('semántico', 'No se puede elevar un valor entero con una cadena'), None
            case Tipos.CHAR: #char
                return Error('semántico', 'No se puede elevar un valor entero con un caracter'), None
            case _: 
                return Error('semántico', 'Error al elevar la expresión'), None
            
    elif nodo1.tipo == Tipos.FLOAT:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return int(t1 ** t2), Tipos.FLOAT
            case Tipos.FLOAT: #float
                return float(t1 ** t2), Tipos.FLOAT
            case Tipos.BOOL: #bool
                return Error('semántico', 'No se puede elevar un valor decimal con un booleano'), None
            case Tipos.STRING: #string
                return Error('semántico', 'No se puede elevar un valor decimal con una cadena'), None
            case Tipos.CHAR: #char
                return Error('semántico', 'No se puede elevar un valor decimal con un caracter'), None
            case _: 
                return Error('semántico', 'Error al elevar la expresión'), None
            
    else:
        return Error('semántico', 'Los tipos de datos proporcionados no son compatibles para la operación de potencia'), None