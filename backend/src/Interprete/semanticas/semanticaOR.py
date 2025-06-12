from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_OR(nodo1, nodo2, t1, t2):
    if nodo1.tipo == Tipos.BOOL:
        match nodo2.tipo:
            # BOOLEANO OR BOOLEANO = BOOLEANO
            case Tipos.BOOL:
                return t1 or t2, Tipos.BOOL
            # BOOLEANO OR ENTERO = ERROR
            case Tipos.INT:
                return Error('Semántico', 'No se puede realizar una operación OR entre un booleano y un entero'), None
            # BOOLEANO OR FLOAT = ERROR
            case Tipos.FLOAT:
                return Error('Semántico', 'No se puede realizar una operación OR entre un booleano y un flotante'), None
            # BOOLEANO OR CARACTER = ERROR
            case Tipos.CHAR:
                return Error('Semántico', 'No se puede realizar una operación OR entre un booleano y un carácter'), None
            # BOOLEANO OR CADENA = ERROR
            case Tipos.STRING:
                return Error('Semántico', 'No se puede realizar una operación OR entre un booleano y una cadena'), None
            case _:
                return Error('Semántico', 'Error al comparar la expresión'), None

    else:
        return Error('Semántico', 'Los tipos de datos proporcionados no son compatibles para la operación OR'), None