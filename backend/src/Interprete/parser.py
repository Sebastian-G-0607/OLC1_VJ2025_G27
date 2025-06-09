import ply.yacc as yacc
from backend.src.Interprete.scanner import tokens
from backend.src.Interprete.nodes.expresiones.Suma import Suma
from backend.src.Interprete.nodes.expresiones.Resta import Resta
from backend.src.Interprete.nodes.expresiones.Multiplicacion import Multiplicacion
from backend.src.Interprete.nodes.expresiones.Division import Division
from backend.src.Interprete.nodes.expresiones.Potencia import Potencia
from backend.src.Interprete.nodes.nativos.Numero import Numero
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
    t[0] = []
    t[0].append(t[1])  # Crea una lista con la única sentencia

def p_sentencia_declaracion(t):
    '''sentencia : declaracion'''

def p_sentencia_asignacion(t):
    '''sentencia : asignacion'''

def p_sentencia_print(t):
    '''sentencia : PRINT PARENTESIS_IZQ expresion PARENTESIS_DER PUNTO_Y_COMA'''
    t[0] = Println(t[3])  # Crea un nodo Println con la expresión a imprimir

def p_asignacion(t):
    '''asignacion : IDENTIFICADOR IGUAL expresion PUNTO_Y_COMA'''

def p_declaracion(t):
    '''declaracion : tipo IDENTIFICADOR declaracion_op'''

def p_declaracion_op_pto_y_coma(t):
    '''declaracion_op : PUNTO_Y_COMA '''

def p_declaracion_op_igual(t):
    '''declaracion_op : IGUAL expresion PUNTO_Y_COMA'''

def p_expresion_suma(t):
    '''expresion : expresion MAS expresion'''
    #SE CREA UN NODO SUMA CON LOS HIJOS t[1] Y t[3]
    t[0] = Suma(t[1], t[3])

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

def p_expresion_entero(t):
    '''expresion : ENTERO'''
    # SE ASIGNA EL VALOR ENTERO A t[0]
    t[0] = Numero(t[1])

def p_expresion_flotante(t):
    '''expresion : FLOTANTE'''
    # SE ASIGNA EL VALOR FLOTANTE A t[0]
    t[0] = Numero(t[1])

def p_expresion_menos_int(t):
    'expresion : MENOS expresion %prec UMENOS'
    # SE CREA UN NODO RESTA CON EL VALOR 0 Y EL HIJO t[2]
    t[0] = -t[2].valor  # Aplicar el signo negativo

def p_expresion_booleano(t):   
    '''expresion :    TRUE
                    | FALSE'''
    
def p_expresion_cadena(t):
    '''expresion :    CADENA
                    | CARACTER'''

def p_expresion_agrupada_exp(t):
    'expresion : expresion_agrupada'
    t[0] = t[1]  # Retorna la expresión agrupada

def p_expresion_agrupada(t):
    'expresion_agrupada : PARENTESIS_IZQ expresion PARENTESIS_DER'
    t[0] = t[2]  # Retorna la expresión dentro de los paréntesis

def p_tipo(t):
    '''tipo : TIPO_INT
            | TIPO_FLOAT
            | TIPO_BOOL
            | TIPO_CHAR
            | TIPO_STR'''

def p_error(t):
    print("Error sintáctico en '%s'" % t.value + " en la línea %d" % t.lineno)

print("Construyendo el analizador sintáctico...\n")
parser = yacc.yacc(debug=True)