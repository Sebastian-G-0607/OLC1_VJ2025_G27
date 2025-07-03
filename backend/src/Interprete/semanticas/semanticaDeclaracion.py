from backend.src.Interprete.simbol.ListaTipos import Tipos

def validarDeclaracion(nodo):
    # RETORNA UN VALOR POR DEFECTO SEGÚN EL TIPO DE DATO
    match nodo.tipoDato:
        case 'int':
            return 0, Tipos.INT
        case 'float':
            return 0.0, Tipos.FLOAT
        case 'bool':
            return True, Tipos.BOOL
        case 'char':
            return '\u0000', Tipos.CHAR
        case 'str':
            return "", Tipos.STRING
        case _:
            raise ValueError(f"Tipo de dato desconocido: {nodo.tipoDato}")