from backend.src.Interprete.errors.Error import Error
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.simbol.InstanciaTabla import st

def recorrer_dimensiones(valores, dimensiones, linea = None, columna = None, name=None, nivel=0, indices=None):
    if indices is None:
        indices = []
    # Verificar que la longitud de valores coincida con la dimensión actual
    if not isinstance(valores, list) or len(valores) != dimensiones[nivel]:
        return Error('semántico', f'Las dimensiones del arreglo {name} no coinciden con su definición', linea, columna)
    if nivel == len(dimensiones) - 1:
        for i in range(dimensiones[nivel]):
            print(f"Índices: {indices + [i]}, Valor: {valores[i]}")
    else:
        for i in range(dimensiones[nivel]):
            res = recorrer_dimensiones(valores[i], dimensiones, linea, columna, name, nivel + 1, indices + [i])
            if isinstance(res, Error):
                return res
            
def validar_tipos(name, valores, tipo, dimensiones, linea = None, columna = None, nivel=0, indices=None):
    if indices is None:
        indices = []

    def es_tipo(valor, tipo):
        if tipo == Tipos.INT:
            return isinstance(valor, int)
        elif tipo == Tipos.FLOAT:
            return isinstance(valor, float)
        elif tipo == Tipos.CHAR:
            return isinstance(valor, str) and len(valor) == 1
        elif tipo == Tipos.BOOL:
            return isinstance(valor, bool)
        elif tipo == Tipos.STRING:
            return isinstance(valor, str)
        else:
            return False

    if nivel == len(dimensiones) - 1:
        for i in range(dimensiones[nivel]):
            valor = valores[i]
            # Solo valida si no es lista (dato primitivo)
            if not isinstance(valor, list) and not es_tipo(valor, tipo):
                return Error('semántico', f'El vector {name} contiene elementos que no coinciden con el tipo {tipo}', linea, columna)
    else:
        for i in range(dimensiones[nivel]):
            res = validar_tipos(name, valores[i], tipo, dimensiones, linea, columna, nivel + 1, indices + [i])
            if isinstance(res, Error):
                return res
    return True

def save_row_major(valores, dimensiones, id, tipo, ordenamiento, linea = None, columna = None, nivel=0, indices=None):
    if indices is None:
        indices = []
    # Verificar que la longitud de valores coincida con la dimensión actual
    if not isinstance(valores, list) or len(valores) != dimensiones[nivel]:
        return Error('semántico', 'Las dimensiones del arreglo no coinciden con su definición', linea, columna)
    if nivel == len(dimensiones) - 1:
        for i in range(dimensiones[nivel]):
            nombre_variable = f"{id}" + "".join(f"[{idx}]" for idx in indices + [i])
            st.add_vector(nombre_variable, tipo, valores[i], len(dimensiones), ordenamiento, linea, columna)
    else:
        for i in range(dimensiones[nivel]):
            res = save_row_major(valores[i], dimensiones, id, tipo, ordenamiento, linea, columna, nivel + 1, indices + [i])
            if isinstance(res, Error):
                return res
# add_vector(self, name, data_type, value=None, dimensions=None, line=None, column=None):