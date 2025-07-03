from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_Not(nodo1, t1):
    if nodo1.tipo == Tipos.BOOL:
        return not t1, Tipos.BOOL
    else:
        return Error('semántico', 'No se puede aplicar el operador NOT a este tipo', nodo1.linea, nodo1.columna), None