from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_diferenciacion(nodo1, nodo2, t1, t2):
    print(nodo1.tipo)
    print(nodo2.tipo)

    if nodo1.tipo == Tipos.INT: 
        match nodo2.tipo:
            # ENTERO != ENTERO = BOOLEANO
            case Tipos.INT:
                return t1 != t2, Tipos.BOOL
            # ENTERO != DECIMAL = BOOLEANO
            case Tipos.FLOAT:
                return t1 != t2, Tipos.BOOL
            # ENTERO != BOOLEANO = ERROR
            case Tipos.BOOL:
                return Error('Semántico', 'No se puede comparar un valor entero con un booleano'), None
            # ENTERO != CARACTER = BOOLEANO
            case Tipos.CHAR:
                return t1 != ord(t2), Tipos.BOOL
            # ENTERO != CADENA = ERROR
            case Tipos.STRING:
                return Error('Semántico', 'No se puede comparar un valor entero con una cadena'), None
            case _:
                return Error('Semántico', 'Error al comparar la expresión'), None
    
    if nodo1.tipo == Tipos.FLOAT:
        match nodo2.tipo:
            # FLOAT != ENTERO = BOOLEANO
            case Tipos.INT:
                return t1 != t2, Tipos.BOOL
            # FLOAT != FLOAT = BOOLEANO
            case Tipos.FLOAT:
                return t1 != t2, Tipos.BOOL
            # FLOAT != BOOLEANO = ERROR
            case Tipos.BOOL:
                return Error('Semántico', 'No se puede comparar un valor flotante con un booleano'), None
            # FLOAT != CARACTER = BOOLEANO
            case Tipos.CHAR:
                return t1 != ord(t2), Tipos.BOOL
            # FLOAT != CADENA = ERROR
            case Tipos.STRING:
                return Error('Semántico', 'No se puede comparar un valor flotante con una cadena'), None
            case _:
                return Error('Semántico', 'Error al comparar la expresión'), None
    
    if nodo1.tipo == Tipos.BOOL:
        match nodo2.tipo:
            # BOOLEANO != ENTERO = ERROR
            case Tipos.INT:
                return Error('Semántico', 'No se puede comparar un valor booleano con un entero'), None
            # BOOLEANO != FLOAT = ERROR
            case Tipos.FLOAT:
                return Error('Semántico', 'No se puede comparar un valor booleano con un flotante'), None
            # BOOLEANO != BOOLEANO = BOOLEANO
            case Tipos.BOOL:
                return t1 != t2, Tipos.BOOL
            #BOOLEANO != CARACTER = ERRO
            case Tipos.CHAR:
                return Error('Semántico', 'No se puede comparar un valor booleano con un carácter'), None
            # BOOLEANO != CADENA = ERROR
            case Tipos.STRING:
                return Error('Semántico', 'No se puede comparar un valor booleano con una cadena'), None
            case _:
                return Error('Semántico', 'Error al comparar la expresión'), None
            
    if nodo1.tipo == Tipos.CHAR:
        match nodo2.tipo:
            # CARACTER != ENTERO = BOOLEANO
            case Tipos.INT:
                return ord(t1) != t2, Tipos.BOOL
            # CARACTER != FLOAT = BOOLEANO
            case Tipos.FLOAT:
                return ord(t1) != t2, Tipos.BOOL
            # CARACTER != BOOLEANO = ERROR
            case Tipos.BOOL:
                return Error('Semántico', 'No se puede comparar un valor carácter con un booleano'), None
            # CARACTER != CARACTER = BOOLEANO
            case Tipos.CHAR:
                return t1 != t2, Tipos.BOOL
            # CARACTER != CADENA = ERROR
            case Tipos.STRING:
                return Error('Semántico', 'No se puede comparar un valor carácter con una cadena'), None
            case _:
                return Error('Semántico', 'Error al comparar la expresión'), None
            
    if nodo1.tipo == Tipos.STRING:
        match nodo2.tipo:
            # CADENA != ENTERO = ERROR
            case Tipos.INT:
                return Error('Semántico', 'No se puede comparar una cadena con un entero'), None
            # CADENA != FLOAT = ERROR
            case Tipos.FLOAT:
                return Error('Semántico', 'No se puede comparar una cadena con un flotante'), None
            # CADENA != BOOLEANO = ERROR
            case Tipos.BOOL:
                return Error('Semántico', 'No se puede comparar una cadena con un booleano'), None
            # CADENA != CARACTER = ERROR
            case Tipos.CHAR:
                return Error('Semántico', 'No se puede comparar una cadena con un carácter'), None
            # CADENA != CADENA = BOOLEANO
            case Tipos.STRING:
                return t1 != t2, Tipos.BOOL
            case _:
                return Error('Semántico', 'Error al comparar la expresión'), None