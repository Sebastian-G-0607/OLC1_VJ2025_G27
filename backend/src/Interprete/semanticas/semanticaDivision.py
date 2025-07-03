from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_division(nodo1, nodo2, t1, t2):
    if nodo1.tipo == Tipos.INT:
        match nodo2.tipo:
            #Entero / Entero = Float
            case Tipos.INT: 
                return float(t1 / t2), Tipos.FLOAT
            #Entero / Float = Float
            case Tipos.FLOAT:
                return float(t1 / t2), Tipos.FLOAT
            #Entero / Caracter = Float 
            case Tipos.CHAR: 
                return float(t1 / ord(t2)), Tipos.FLOAT
            case _:
                return Error('semántico','Error al dividir la expresión', nodo2.linea, nodo2.columna), None

    elif nodo1.tipo == Tipos.FLOAT: 
        match nodo2.tipo: 
            #Float / Entero = Float
            case Tipos.INT: 
                return float(t1 / t2 ), Tipos.FLOAT
            #Float / Float = Float
            case Tipos.FLOAT: 
                return float(t1 / t2), Tipos.FLOAT
            #Float / Caracter  = Float
            case Tipos.CHAR: 
                return float(t1 / ord(t2)), Tipos.FLOAT
            case _:
                return Error('semántico', 'Error al dividir la expresión', nodo2.linea, nodo2.columna), None

    elif nodo1.tipo == Tipos.CHAR: 
        match nodo2.tipo:
            #Caracter / Entero = Float
            case Tipos.INT: 
                return float(ord(t1) / t2), Tipos.FLOAT
            #Caracter / Float = Float
            case Tipos.FLOAT: 
                return float(ord(t1) / t2), Tipos.FLOAT
            #Caracter / Caracter = Float
            case Tipos.CHAR: 
                return Error('semántico', 'No se puede dividir un carácter por otro carácter', nodo2.linea, nodo2.columna), None
            case _: 
                return Error('semántico', 'Error al dividir la expresión', nodo2.linea, nodo2.columna), None

    else:
        return Error('semántico', 'Los tipos de datos proporcionados no son compatibles para la operación de división', nodo1.linea, nodo1.columna), None