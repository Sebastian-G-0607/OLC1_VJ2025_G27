from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_multiplicacion(nodo1, nodo2, t1, t2):
    if nodo1.tipo == Tipos.INT: 
        match nodo2.tipo:
            # ENTERO * ENTERO = ENTERO
            case Tipos.INT: 
                return int(t1 * t2), Tipos.INT
            # ENTERO * DECIMAL = DECIMAL
            case Tipos.FLOAT: 
                return float(t1 * t2), Tipos.FLOAT 
            # ENTERO * CARACTER = ENTERO
            case Tipos.CHAR: 
                return int(t1 * ord(t2)), Tipos.INT
            case _: 
                return Error('Semántico', 'Error al multiplicar la expresión'), None
    
    if nodo1.tipo == Tipos.FLOAT:
        match nodo2.tipo:
            # FLOAT * ENTERO = FLOAT
            case Tipos.INT: 
                return float(t1 * t2), Tipos.FLOAT
            # FLOAT * FLOAT = FLOAT
            case Tipos.FLOAT: 
                return float(t1 * t2), Tipos.FLOAT
            # FLOAT * CARACTER = FLOAT
            case Tipos.CHAR: 
                return float(t1 * ord(t2)), Tipos.FLOAT
            case _: 
                return Error('Semántico', 'Error al multiplicar la expresión'), None
    
    if nodo1.tipo == Tipos.CHAR:
        match nodo2.tipo:
            # CARACTER * ENTERO = ENTERO
            case Tipos.INT: 
                return int(ord(t1) * t2), Tipos.INT
            # CARACTER * FLOAT = FLOAT
            case Tipos.FLOAT: 
                return float(ord(t1) * t2), Tipos.FLOAT
            # CARACTER * CARACTER = ERROR
            case Tipos.CHAR: 
                return Error('Semántico', 'No se puede multiplicar un caracter con otro caracter'), None
            case _: 
                return Error('Semántico', 'Error al multiplicar la expresión'), None
    
    if nodo1.tipo == Tipos.STRING or nodo1.tipo == Tipos.BOOL:
        return Error('Semántico', 'Los tipos de datos proporcionados no son compatibles para la operación de multiplicación'), None