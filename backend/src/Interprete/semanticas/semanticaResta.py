from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_resta(nodo1, nodo2, t1, t2):
    if nodo1.tipo == Tipos.INT: 
        match nodo2.tipo:
            #Entero - Entero = Entero
            case Tipos.INT: 
                return int(t1 - t2), Tipos.INT
            #Entero - Decimal = Decimal
            case Tipos.FLOAT:
                return float(t1 - t2), Tipos.FLOAT 
            #Entero - Caracter = Entero
            case Tipos.CHAR: 
                return int(t1 - ord(t2)), Tipos.INT
            case _: 
                return Error('semántico', 'Error al resta la expresión', nodo2.linea, nodo2.columna), None

    if nodo1.tipo == Tipos.FLOAT: 
        match nodo2.tipo:
            #Float - Entero = Float
            case Tipos.INT: 
                return float(t1 - t2), Tipos.FLOAT
            #Float - Float = Float
            case Tipos.FLOAT: 
                return float(t1 - t2), Tipos.FLOAT
            #Float - Caracter = Float
            case Tipos.CHAR: 
                return float(t1 - ord(t2)), Tipos.FLOAT
            case _: 
                return Error('semántico', 'Error al resta la expresión', nodo2.linea, nodo2.columna), None

    if nodo1.tipo == Tipos.CHAR:
        match nodo2.tipo:
            #Caracter - Entero = Entero
            case Tipos.INT: 
                return int(ord(t1) - t2), Tipos.INT
            #Caracter - Float = Float
            case Tipos.FLOAT: 
                return float(ord(t1) - t2), Tipos.FLOAT
            #Caracter - Caracter = Entero
            case Tipos.CHAR: 
                return Error('semántico', 'No se puede restar un caracter con otro caracter', nodo2.linea, nodo2.columna), None
            case _: 
                return Error('semántico', 'Error al resta la expresión', nodo2.linea, nodo2.columna), None

    if nodo1.tipo == Tipos.STRING or nodo1.tipo == Tipos.BOOL:
        return Error('semántico', 'Los tipos de datos proporcionados no son compatibles para la operación de resta', nodo2.linea, nodo2.columna), None