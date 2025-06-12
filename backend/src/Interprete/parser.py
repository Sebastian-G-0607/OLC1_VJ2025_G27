import ply.yacc as yacc
from backend.src.Interprete.nodes.expresiones.AccesoVariable import AccesoVariable
from backend.src.Interprete.nodes.expresiones.And import And
from backend.src.Interprete.nodes.expresiones.DiferenteQue import DiferenteQue
from backend.src.Interprete.nodes.expresiones.IgualQue import IgualQue
from backend.src.Interprete.nodes.expresiones.MayorIgualQue import MayorIgualQue
from backend.src.Interprete.nodes.expresiones.MayorQue import MayorQue
from backend.src.Interprete.nodes.expresiones.MenorIgualQue import MenorIgualQue
from backend.src.Interprete.nodes.expresiones.MenorQue import MenorQue
from backend.src.Interprete.nodes.expresiones.Modulo import Modulo
from backend.src.Interprete.nodes.expresiones.Not import Not
from backend.src.Interprete.nodes.expresiones.Or import Or
from backend.src.Interprete.nodes.expresiones.Umenos import Umenos
from backend.src.Interprete.nodes.expresiones.Xor import Xor
from backend.src.Interprete.nodes.instrucciones.Decremento import Decremento
from backend.src.Interprete.nodes.instrucciones.For import For
from backend.src.Interprete.nodes.instrucciones.Incremento import Incremento
from backend.src.Interprete.nodes.instrucciones.While import While
from backend.src.Interprete.nodes.instrucciones.Asignacion import Asignacion
from backend.src.Interprete.nodes.instrucciones.Declaracion import Declaracion
from backend.src.Interprete.nodes.instrucciones.Else import Else
from backend.src.Interprete.nodes.instrucciones.If import If
from backend.src.Interprete.nodes.instrucciones.IfElse import IfElse
from backend.src.Interprete.nodes.instrucciones.IfElseIf import IfElseIf
from backend.src.Interprete.scanner import tokens
from backend.src.Interprete.nodes.expresiones.Suma import Suma
from backend.src.Interprete.nodes.expresiones.Resta import Resta
from backend.src.Interprete.nodes.expresiones.Multiplicacion import Multiplicacion
from backend.src.Interprete.nodes.expresiones.Division import Division
from backend.src.Interprete.nodes.expresiones.Potencia import Potencia
from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.nodes.instrucciones.Print import Println

# PRESEDENCIA Y ASOCIACION DE LOS OPERADORES
precedence = (
    ('right','UMENOS'),
    ('nonassoc', 'POTENCIA'), 
    ('left','MULTIPLICACION','DIVISION'),
    ('left','IGUALQUE','DIFERENTEQUE'),
    ('left','MAYORQUE','MENORQUE'),
    ('left','MAYORIGUALQUE','MENORIGUALQUE'),
)

# ANALISIS SINTÁCTICO
def p_programa(t):
    '''programa : sentencias'''
    t[0] = t[1]  # El resultado del programa es la lista de sentencias
    
def p_lista_sentencias(t):
    '''sentencias : sentencias sentencia''' 
    t[0] = t[1]
    t[0].append(t[2])  # Agrega la nueva sentencia a la lista de sentencias

def p_una_sentencia(t):
    '''sentencias : sentencia'''
    t[0] = list()
    t[0].append(t[1])  # Crea una lista con la única sentencia

def p_sentencia_print(t):
    '''sentencia : PRINT PARENTESIS_IZQ expresion PARENTESIS_DER PUNTO_Y_COMA'''
    t[0] = Println(t[3])  # Crea un nodo Println con la expresión a imprimir

def p_sentencia_declaracion(t):
    '''sentencia : declaracion'''
    t[0] = t[1]  # La sentencia es una declaración, se asigna directamente

def p_sentencia_asignacion(t):
    '''sentencia : asignacion'''
    t[0] = t[1]  # La sentencia es una asignación, se asigna directamente

def p_sentencia_if(t):
    '''sentencia : sentenciaIf'''
    t[0] = t[1]  # La sentencia es una sentencia If, se asigna directamente

def p_sentencia_while(t):
    '''sentencia : WHILE PARENTESIS_IZQ condicion PARENTESIS_DER LLAVE_IZQ sentencias LLAVE_DER'''
    # SE CREA UN NODO WHILE CON LA CONDICION Y LAS INSTRUCCIONES
    t[0] = While(t[3], t[6])  # Crea un nodo While con la condición y las sentencias

def p_sentencia_for(t):
    '''sentencia : FOR PARENTESIS_IZQ inicio_for condicion PUNTO_Y_COMA actualizacion PARENTESIS_DER LLAVE_IZQ sentencias LLAVE_DER'''
    # SE CREA UN NODO FOR CON LA DECLARACION, CONDICION, ACTUALIZACION Y LAS INSTRUCCIONES
    t[0] = For(t[3], t[4], t[6], t[9])  # Crea un nodo For con la declaración, condición, actualización y sentencias

def p_inicio_for_asignacion(t):
    '''inicio_for : asignacion'''
    # SE CREA UN NODO FOR CON LA ASIGNACION
    t[0] = t[1]  # La asignación se asigna directamente

def p_inicio_for_declaracion(t):
    '''inicio_for : declaracion_valor'''
    t[0] = t[1]  # La declaración o asignación se asigna directamente

def p_actualizacion_incremento(t):
    '''actualizacion : IDENTIFICADOR INCREMENTO'''
    # SE CREA UN NODO ASIGNACION CON EL IDENTIFICADOR Y LA EXPRESION DE INCREMENTO
    t[0] = Incremento(t[1])  # Crea un nodo Incremento con el identificador

def p_actualizacion_decremento(t):
    '''actualizacion : IDENTIFICADOR DECREMENTO'''
    # SE CREA UN NODO ASIGNACION CON EL IDENTIFICADOR Y LA EXPRESION DE DECREMENTO
    t[0] = Decremento(t[1])  # Crea un nodo Decremento con el identificador

def p_actualizacion_asignacion(t):
    '''actualizacion : IDENTIFICADOR IGUAL expresion'''
    # SE CREA UN NODO ASIGNACION CON EL IDENTIFICADOR Y LA EXPRESION
    t[0] = Asignacion(t[1], t[3])  # Crea un nodo Asignacion con el identificador y la expresión

def p_sentencia_incremento(t):
    '''sentencia : IDENTIFICADOR INCREMENTO PUNTO_Y_COMA'''
    # SE CREA UN NODO ASIGNACION CON EL IDENTIFICADOR Y LA EXPRESION DE INCREMENTO
    t[0] = Incremento(t[1])

def p_sentencia_decremento(t):
    '''sentencia : IDENTIFICADOR DECREMENTO PUNTO_Y_COMA'''
    # SE CREA UN NODO ASIGNACION CON EL IDENTIFICADOR Y LA EXPRESION DE DECREMENTO
    t[0] = Decremento(t[1])

def p_asignacion(t):
    '''asignacion : IDENTIFICADOR IGUAL expresion PUNTO_Y_COMA'''
    # SE CREA UN NODO ASIGNACION CON EL IDENTIFICADOR Y LA EXPRESION
    t[0] = Asignacion(t[1], t[3])

def p_declaracion_init(t):
    '''declaracion : declaracion_valor'''
    t[0] = t[1]

def p_declaracion_no_init(t):
    '''declaracion : declaracion_sin_valor'''
    t[0] = t[1]

def p_declaracion_op_igual(t):
    '''declaracion_valor : tipo IDENTIFICADOR IGUAL expresion PUNTO_Y_COMA'''
    t[0] = Declaracion(t[1], t[2], t[4])

def p_declaracion_op_pto_y_coma(t):
    '''declaracion_sin_valor : tipo IDENTIFICADOR PUNTO_Y_COMA'''
    t[0] = Declaracion(t[1], t[2])  # Declaración sin inicialización

def p_expresion_suma(t):
    '''expresion : expresion MAS expresion'''
    #SE CREA UN NODO SUMA CON LOS HIJOS t[1] Y t[3]
    t[0] = Suma(t[1], t[3], t[1].linea, t[1].columna)

def p_expresion_resta(t):
    '''expresion : expresion MENOS expresion'''
    #SE CREA UN NODO RESTA CON LOS HIJOS t[1] Y t[3]
    t[0] = Resta(t[1], t[3])

def p_expresion_multiplicacion(t):
    '''expresion : expresion MULTIPLICACION expresion'''
    # SE CREA UN NODO MULTIPLICACION CON LOS HIJOS t[1] Y t[3]
    t[0] = Multiplicacion(t[1], t[3])

def p_expresion_division(t):
    '''expresion : expresion DIVISION expresion'''
    # SE CREA UN NODO DIVISION CON LOS HIJOS t[1] Y t[3]
    t[0] = Division(t[1], t[3])

def p_expresion_potencia(t):
    '''expresion : expresion POTENCIA expresion'''
    # SE CREA UN NODO POTENCIA CON LOS HIJOS t[1] Y t[3]
    t[0] = Potencia(t[1], t[3])

def p_expresion_menos_int(t):
    'expresion : MENOS expresion %prec UMENOS'
    # SE CREA UN NODO RESTA CON EL VALOR 0 Y EL HIJO t[2]
    t[0] = Umenos(t[2])  # Aplicar el signo negativo

def p_expresion_modulo(t):
    '''expresion : expresion MODULO expresion'''
    # SE CREA UN NODO MODULO CON LOS HIJOS t[1] Y t[3]
    t[0] = Modulo(t[1], t[3])
    
def p_expresion_relacionales(t):
    '''expresion : relacional'''
    t[0] = t[1] # SE ASIGNA LA COMPARACION RELACIONAL A t[0]

def p_expresion_logica(t):
    '''expresion : logica'''
    t[0] = t[1]  # SE ASIGNA LA EXPRESION LOGICA A t[0]

def p_expresion_identificador(t):
    '''expresion : IDENTIFICADOR'''
    # SE CREA UN NODO ACCESO VARIABLE CON EL IDENTIFICADOR
    t[0] = AccesoVariable(t[1])

def p_relacional_igualque(t):
    '''relacional : expresion IGUALQUE expresion'''
    # SE CREA UN NODO IGUALQUE CON LOS HIJOS t[1] Y t[3]
    t[0] = IgualQue(t[1], t[3])

def p_relacional_diferenteque(t):
    '''relacional : expresion DIFERENTEQUE expresion'''
    # SE CREA UN NODO DIFERENTEQUE CON LOS HIJOS t[1] Y t[3]
    t[0] = DiferenteQue(t[1], t[3])

def p_relacional_mayorque(t):
    '''relacional : expresion MAYORQUE expresion'''
    # SE CREA UN NODO MAYORQUE CON LOS HIJOS t[1] Y t[3]
    t[0] = MayorQue(t[1], t[3])

def p_relacional_mayorigualque(t):
    '''relacional : expresion MAYORIGUALQUE expresion'''
    # SE CREA UN NODO MAYORIGUALQUE CON LOS HIJOS t[1] Y t[3]
    t[0] = MayorIgualQue(t[1], t[3])

def p_relacional_menorque(t):
    '''relacional : expresion MENORQUE expresion'''
    # SE CREA UN NODO MENORQUE CON LOS HIJOS t[1] Y t[3]
    t[0] = MenorQue(t[1], t[3])

def p_relacional_menorigualque(t):
    '''relacional : expresion MENORIGUALQUE expresion'''
    # SE CREA UN NODO MENORIGUALQUE CON LOS HIJOS t[1] Y t[3]
    t[0] = MenorIgualQue(t[1], t[3])

def p_logica_and(t):
    '''logica : expresion AND expresion'''
    # SE CREA UN NODO AND CON LOS HIJOS t[1] Y t[3]
    t[0] = And(t[1], t[3])

def p_logica_or(t):
    '''logica : expresion OR expresion'''
    # SE CREA UN NODO OR CON LOS HIJOS t[1] Y t[3]
    t[0] = Or(t[1], t[3])

def p_logica_not(t):
    '''logica : NOT expresion'''
    # SE CREA UN NODO NOT CON EL HIJO t[2]
    t[0] = Not(t[2])

def p_logica_xor(t):
    '''logica : expresion XOR expresion'''
    # SE CREA UN NODO XOR CON LOS HIJOS t[1] Y t[3]
    t[0] = Xor(t[1], t[3])

def p_logica_true(t):
    '''logica : TRUE'''
    # SE ASIGNA EL VALOR TRUE A t[0]
    t[0] = Nativo(Tipos.BOOL, True)

def p_logica_false(t):
    '''logica : FALSE'''
    # SE ASIGNA EL VALOR FALSE A t[0]
    t[0] = Nativo(Tipos.BOOL, False)

def p_logica_identificador(t):
    '''logica : IDENTIFICADOR'''
    # SE CREA UN NODO ACCESO VARIABLE CON EL IDENTIFICADOR
    t[0] = AccesoVariable(t[1])  # Retorna el acceso a la variable

def p_expresion_entero(t):
    '''expresion : ENTERO'''
    # SE ASIGNA EL VALOR ENTERO A t[0]
    t[0] = Nativo(Tipos.INT, int(t[1]), t.slice[1].lineno, find_column(t.lexer.lexdata, t.slice[1]))

def p_expresion_flotante(t):
    '''expresion : FLOTANTE'''
    # SE ASIGNA EL VALOR FLOTANTE A t[0]
    t[0] = Nativo(Tipos.FLOAT, float(t[1]), t.slice[1].lineno, find_column(t.lexer.lexdata, t.slice[1]))

def p_expresion_true(t):
    '''expresion : TRUE'''
    t[0] = Nativo(Tipos.BOOL, True, t.slice[1].lineno, find_column(t.lexer.lexdata, t.slice[1]))

def p_expresion_false(t):
    '''expresion : FALSE'''
    t[0] = Nativo(Tipos.BOOL, False, t.slice[1].lineno, find_column(t.lexer.lexdata, t.slice[1]))

def p_expresion_cadena(t):
    '''expresion : CADENA'''
    t[0] = Nativo(Tipos.STRING, str(t[1]), t.slice[1].lineno, find_column(t.lexer.lexdata, t.slice[1]))

def p_expresion_caracter(t):
    '''expresion : CARACTER'''
    # SE ASIGNA EL VALOR CARACTER A t[0]
    t[0] = Nativo(Tipos.CHAR, str(t[1]))

def p_expresion_agrupada_exp(t):
    'expresion : expresion_agrupada'
    t[0] = t[1]  # Retorna la expresión agrupada

def p_expresion_agrupada(t):
    'expresion_agrupada : PARENTESIS_IZQ expresion PARENTESIS_DER'
    t[0] = t[2]  # Retorna la expresión dentro de los paréntesis

def p_sentencia_if_simple(t):
    '''sentenciaIf : IF PARENTESIS_IZQ condicion PARENTESIS_DER LLAVE_IZQ sentencias LLAVE_DER'''
    t[0] = If(t[3], t[6])

def p_sentencia_if_else(t):
    '''sentenciaIf : IF PARENTESIS_IZQ condicion PARENTESIS_DER LLAVE_IZQ sentencias LLAVE_DER ELSE LLAVE_IZQ selse LLAVE_DER'''
    # SE CREA UN NODO IF CON LA CONDICION Y LAS INSTRUCCIONES
    t[0] = IfElse(t[3], t[6], t[10])

def p_sentencia_else(t):
    '''selse : sentencias'''
    t[0] = Else(t[1])

def p_sentencia_if_else_if(t):
    '''sentenciaIf : IF PARENTESIS_IZQ condicion PARENTESIS_DER LLAVE_IZQ sentencias LLAVE_DER ELSE sentenciaIf'''
    t[0] = IfElseIf(t[3], t[6], t[9])

def p_condicion_logica(t):
    '''condicion : logica'''
    # SE ASIGNA LA EXPRESION A LA CONDICION
    t[0] = t[1]  # Retorna la expresión como condición

def p_condicion_relacional(t):
    '''condicion : relacional'''
    # SE ASIGNA LA EXPRESION A LA CONDICION
    t[0] = t[1]  # Retorna la expresión como condición

def p_tipo_int(t):
    'tipo : TIPO_INT'
    t[0] = t[1]

def p_tipo_float(t):
    'tipo : TIPO_FLOAT'
    t[0] = t[1]

def p_tipo_bool(t):
    'tipo : TIPO_BOOL'
    t[0] = t[1]

def p_tipo_char(t):
    'tipo : TIPO_CHAR'
    t[0] = t[1]

def p_tipo_str(t):
    'tipo : TIPO_STR'
    t[0] = t[1]

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def p_error(t):
    if t:
        print(f"Error de sintaxis: token inesperado '{t.value}' en línea {t.lineno}")
    else:
        print("Error de sintaxis: fin de entrada inesperado")
    return

print("Construyendo el analizador sintáctico...\n")
parser = yacc.yacc(debug=True)