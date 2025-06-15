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
                return Error('semántico', 'No se puede realizar una operación AND entre un booleano y un entero', nodo2.linea, nodo2.columna), None
            # BOOLEANO AND FLOAT = ERROR
            case Tipos.FLOAT:
                return Error('semántico', 'No se puede realizar una operación AND entre un booleano y un flotante', nodo2.linea, nodo2.columna), None
            # BOOLEANO AND CARACTER = ERROR
            case Tipos.CHAR:
                return Error('semántico', 'No se puede realizar una operación AND entre un booleano y un carácter', nodo2.linea, nodo2.columna), None
            # BOOLEANO AND CADENA = ERROR
            case Tipos.STRING:
                return Error('semántico', 'No se puede realizar una operación AND entre un booleano y una cadena', nodo2.linea, nodo2.columna), None
            case _:
                return Error('semántico', 'Error al comparar la expresión', nodo2.linea, nodo2.columna), None

    else:
        return Error('semántico', 'Los tipos de datos proporcionados no son compatibles para la operación AND', nodo1.linea, nodo1.columna), None