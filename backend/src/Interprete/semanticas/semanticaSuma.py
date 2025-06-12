from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_suma(nodo1, nodo2, t1, t2):
    if nodo1.tipo == Tipos.INT:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return int(t1 + t2), Tipos.INT
            case Tipos.FLOAT: #float
                return float(t1 + t2), Tipos.FLOAT
            case Tipos.BOOL: #bool
                return Error('semántico', 'No se puede sumar un valor entero con un booleano'), None
            case Tipos.STRING: #string
                return str(str(t1) + t2), Tipos.STRING
            case Tipos.CHAR: #char
                return int(t1 + ord(t2)), Tipos.INT
            case _: 
                return Error('semántico', 'Error al sumar la expresión'), None

    if nodo1.tipo == Tipos.FLOAT:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return float(t1 + t2), Tipos.FLOAT
            case Tipos.FLOAT: #float
                return float(t1 + t2), Tipos.FLOAT
            case Tipos.BOOL: #bool
                return Error('semántico', 'No se puede sumar un valor flotante con un booleano'), None
            case Tipos.STRING: #string
                return str(str(t1) + t2), Tipos.STRING
            case Tipos.CHAR: #char
                return float(t1 + ord(t2)), Tipos.FLOAT
            case _: 
                return Error('semántico', 'Error al sumar la expresión'), None

    if nodo1.tipo == Tipos.BOOL:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return Error('semántico', 'No se puede sumar un valor booleano con un entero'), None
            case Tipos.FLOAT: #float
                return Error('semántico', 'No se puede sumar un valor booleano con un flotante'), None
            case Tipos.BOOL: #bool
                return Error('semántico', 'No se puede sumar un valor booleano con otro booleano'), None
            case Tipos.STRING: #string
                return str(str(t1) + t2), Tipos.STRING  
            case Tipos.CHAR: #char
                return Error('semántico', 'No se puede sumar un valor booleano con un carácter'), None
            case _: 
                return Error('semántico', 'Error al sumar la expresión'), None

    if nodo1.tipo == Tipos.CHAR:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return int(ord(t1) + t2), Tipos.INT 
            case Tipos.FLOAT: #float
                return float(ord(t1) + t2), Tipos.FLOAT
            case Tipos.BOOL: #bool
                return Error('semántico', 'No se puede sumar un caracter con un valor booleano'), None
            case Tipos.STRING: #string
                return str(str(t1) + t2), Tipos.STRING
            case Tipos.CHAR: #char
                return str(t1 + t2), Tipos.STRING
            case _: 
                return Error('semántico', 'Error al sumar la expresión'), None

    if nodo1.tipo == Tipos.STRING:
        match nodo2.tipo:
            case Tipos.INT: #entero
                return str(t1 + str(t2)), Tipos.STRING
            case Tipos.FLOAT: #float
                return str(t1 + str(t2)), Tipos.STRING
            case Tipos.BOOL: #bool
                return str(t1 + str(t2)), Tipos.STRING
            case Tipos.STRING: #string
                return str(t1 + t2), Tipos.STRING
            case Tipos.CHAR: #char
                return str(t1 + t2), Tipos.STRING
            case _: 
                return Error('semántico', 'Error al sumar la expresión'), None