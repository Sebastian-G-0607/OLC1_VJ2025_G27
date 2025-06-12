from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_AND(nodo1, nodo2, t1, t2):
    if nodo1.tipo == Tipos.BOOL:
        match nodo2.tipo:
            # BOOLEANO AND BOOLEANO = BOOLEANO
            case Tipos.BOOL:
                return t1 and t2, Tipos.BOOL
            # BOOLEANO AND ENTERO = ERROR
            case Tipos.INT:
                return Error('Semántico', 'No se puede realizar una operación AND entre un booleano y un entero'), None
            # BOOLEANO AND FLOAT = ERROR
            case Tipos.FLOAT:
                return Error('Semántico', 'No se puede realizar una operación AND entre un booleano y un flotante'), None
            # BOOLEANO AND CARACTER = ERROR
            case Tipos.CHAR:
                return Error('Semántico', 'No se puede realizar una operación AND entre un booleano y un carácter'), None
            # BOOLEANO AND CADENA = ERROR
            case Tipos.STRING:
                return Error('Semántico', 'No se puede realizar una operación AND entre un booleano y una cadena'), None
            case _:
                return Error('Semántico', 'Error al comparar la expresión'), None

    else:
        return Error('Semántico', 'El primer operando debe ser de tipo booleano para la operación AND'), None