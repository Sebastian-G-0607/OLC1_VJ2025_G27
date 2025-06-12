from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error


def validar_suma(nodo1, nodo2, t1, t2):
    if nodo1.tipo == Tipos.INT:
        match nodo2.tipo:
            #ENTERO + ENTERO = ENTERO
            case Tipos.INT: #entero
                return int(t1 + t2), Tipos.INT
            #ENTERO + DECIMAL = DECIMAL
            case Tipos.FLOAT: #float
                return float(t1 + t2), Tipos.FLOAT
            #ENTERO + BOOLEANO = ERROR
            case Tipos.BOOL: #bool
                return Error('semántico', 'No se puede sumar un valor entero con un booleano'), None
            case Tipos.STRING: #string
                return str(str(t1) + t2), Tipos.STRING
            case Tipos.CHAR: #char
                return int(t1 + ord(t2)), Tipos.INT
            #ENTERO + CADENA = CADENA
            case Tipos.STRING: #string
                return str(str(t1) + t2), Tipos.STRING
            case _: 
                return Error('semántico', 'Error al sumar la expresión'), None

    if nodo1.tipo == Tipos.FLOAT:
        match nodo2.tipo:
            #FLOAT + ENTERO = FLOAT
            case Tipos.INT: #entero
                return float(t1 + t2), Tipos.FLOAT
            #FLOAT + FLOAT = FLOAT
            case Tipos.FLOAT: #float
                return float(t1 + t2), Tipos.FLOAT
            #FLOAT + BOOLEANO = ERROR
            case Tipos.BOOL: #bool
                return Error('semántico', 'No se puede sumar un valor flotante con un booleano'), None
            case Tipos.STRING: #string
                return str(str(t1) + t2), Tipos.STRING
            #FLOAT + CARACTER = FLOAT 
            case Tipos.CHAR: #char
                return float(t1 + ord(t2)), Tipos.FLOAT
            case _: 
                return Error('semántico', 'Error al sumar la expresión'), None

    if nodo1.tipo == Tipos.BOOL:
        match nodo2.tipo:
            #BOOLEANO + ENTERO = ERROR
            case Tipos.INT: #entero
                return Error('semántico', 'No se puede sumar un valor booleano con un entero'), None
            case Tipos.FLOAT: #float
                return Error('semántico', 'No se puede sumar un valor booleano con un flotante'), None
            case Tipos.BOOL: #bool
                return Error('semántico', 'No se puede sumar un valor booleano con otro booleano'), None
            case Tipos.STRING: #string
                return str(str(t1) + t2), Tipos.STRING
            #BOOLEANO + CARACTER = ERROR  
            case Tipos.CHAR: #char
                return Error('semántico', 'No se puede sumar un valor booleano con un carácter'), None
            case _: 
                return Error('semántico', 'Error al sumar la expresión'), None

    if nodo1.tipo == Tipos.CHAR:
        match nodo2.tipo:
            #CARACTER + ENTERO = ENTERO
            case Tipos.INT: #entero
                return int(ord(t1) + t2), Tipos.INT 
            #CARACTER + FLOAT = FLOAT
            case Tipos.FLOAT: #float
                return float(ord(t1) + t2), Tipos.FLOAT
            #CARACTER + BOOLEANO = ERROR
            case Tipos.BOOL: #bool
                return Error('semántico', 'No se puede sumar un caracter con un valor booleano'), None
            case Tipos.STRING: #string
                return str(str(t1) + t2), Tipos.STRING
            #CARACTER + CARACTER = CADENA
            case Tipos.CHAR: #char
                return str(t1 + t2), Tipos.STRING
            case _: 
                return Error('semántico', 'Error al sumar la expresión'), None

    if nodo1.tipo == Tipos.STRING:
        match nodo2.tipo:
            #CADENA + ENTERO = CADENA
            case Tipos.INT: #entero
                return str(t1 + str(t2)), Tipos.STRING
            #CADENA + FLOAT = CADENA
            case Tipos.FLOAT: #float
                return str(t1 + str(t2)), Tipos.STRING
            #CADENA + BOOOLEANO = CADENA
            case Tipos.BOOL: #bool
                return str(t1 + str(t2)), Tipos.STRING
            #CADENA + CADENA = CADENA
            case Tipos.STRING: #string
                return str(t1 + t2), Tipos.STRING
            #CADENA + CARACTER = CADENA
            case Tipos.CHAR: #char
                return str(t1 + t2), Tipos.STRING
            case _: 
                return Error('semántico', 'Error al sumar la expresión'), None