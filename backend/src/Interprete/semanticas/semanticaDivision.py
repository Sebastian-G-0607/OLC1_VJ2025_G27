from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_division(nodo1, nodo2, t1, t2):
    print(nodo1.tipo)
    print(nodo2.tipo)

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
                return Error('Semático','Error al divir la expresión'), None
    
    if nodo1.tipo == Tipos.FLOAT: 
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
                return Error('Semántico', 'Error al dividir la expresión'), None
    
    if nodo1.tipo == Tipos.CHAR: 
        match nodo2.tipo:
            #Caracter / Entero = Float
            case Tipos.INT: 
                return float(ord(t1) / t2), Tipos.FLOAT
            #Caracter / Float = Float
            case Tipos.FLOAT: 
                return float(ord(t1) / t2), Tipos.FLOAT
            #Caracter / Caracter = Float
            case Tipos.CHAR: 
                return Error('Semántico', 'No se puede divir un carater por otro caracter'), None
            case _: 
                return Error('Semántico', 'Error al dividir la expresión'), None
    
    if nodo1.tipo == Tipos.STRING or nodo2.tipo == Tipos.STRING:
        return Error('Semántico', 'No se pueden divir valores de este tipo'), None