from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.errors.Error import Error

def validar_Umenos(nodo1, t1):
    if nodo1.tipo == Tipos.INT:
        return -int(t1), Tipos.INT
    elif nodo1.tipo == Tipos.FLOAT:
        return -float(t1), Tipos.FLOAT
    else:
        return Error('Semántico', 'No se puede aplicar el operador unario menos a este tipo', nodo1.linea, nodo1.columna), None
