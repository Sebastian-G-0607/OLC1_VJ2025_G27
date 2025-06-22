import ply.yacc as yacc
from backend.src.Interprete.nodes.expresiones.AccesoVariable import AccesoVariable
from backend.src.Interprete.nodes.expresiones.AccesoVector import AccesoVector
from backend.src.Interprete.nodes.expresiones.And import And
from backend.src.Interprete.nodes.expresiones.Coseno import Coseno
from backend.src.Interprete.nodes.expresiones.DiferenteQue import DiferenteQue
from backend.src.Interprete.nodes.expresiones.IgualQue import IgualQue
from backend.src.Interprete.nodes.expresiones.Inversion import Inversion
from backend.src.Interprete.nodes.expresiones.MayorIgualQue import MayorIgualQue
from backend.src.Interprete.nodes.expresiones.MayorQue import MayorQue
from backend.src.Interprete.nodes.expresiones.MenorIgualQue import MenorIgualQue
from backend.src.Interprete.nodes.expresiones.MenorQue import MenorQue
from backend.src.Interprete.nodes.expresiones.Modulo import Modulo
from backend.src.Interprete.nodes.expresiones.Not import Not
from backend.src.Interprete.nodes.expresiones.Or import Or
from backend.src.Interprete.nodes.expresiones.Seno import Seno
from backend.src.Interprete.nodes.expresiones.Shuffle import Shuffle
from backend.src.Interprete.nodes.expresiones.Sort import Sort
from backend.src.Interprete.nodes.expresiones.Umenos import Umenos
from backend.src.Interprete.nodes.expresiones.Xor import Xor
from backend.src.Interprete.nodes.expresiones.Suma import Suma
from backend.src.Interprete.nodes.expresiones.Resta import Resta
from backend.src.Interprete.nodes.expresiones.Multiplicacion import Multiplicacion
from backend.src.Interprete.nodes.expresiones.Division import Division
from backend.src.Interprete.nodes.expresiones.Potencia import Potencia
from backend.src.Interprete.nodes.instrucciones.AsignacionVector import AsignacionVector
from backend.src.Interprete.nodes.instrucciones.Break import Break
from backend.src.Interprete.nodes.instrucciones.Case import Case
from backend.src.Interprete.nodes.instrucciones.Continue import Continue
from backend.src.Interprete.nodes.instrucciones.Decremento import Decremento
from backend.src.Interprete.nodes.instrucciones.DoWhile import DoWhile
from backend.src.Interprete.nodes.instrucciones.Execute import Execute
from backend.src.Interprete.nodes.instrucciones.For import For
from backend.src.Interprete.nodes.instrucciones.Incremento import Incremento
from backend.src.Interprete.nodes.instrucciones.ParametroDefinicion import ParametroDefinicion
from backend.src.Interprete.nodes.instrucciones.Procedimiento import Procedimiento
from backend.src.Interprete.nodes.instrucciones.Switch import Switch
from backend.src.Interprete.nodes.instrucciones.While import While
from backend.src.Interprete.nodes.instrucciones.Asignacion import Asignacion
from backend.src.Interprete.nodes.instrucciones.Declaracion import Declaracion
from backend.src.Interprete.nodes.instrucciones.Else import Else
from backend.src.Interprete.nodes.instrucciones.If import If
from backend.src.Interprete.nodes.instrucciones.IfElse import IfElse
from backend.src.Interprete.nodes.instrucciones.IfElseIf import IfElseIf
from backend.src.Interprete.nodes.instrucciones.Vector import Vector
from backend.src.Interprete.nodes.instrucciones.DeclaracionVector import DeclaracionVector
from backend.src.Interprete.scanner import tokens, build_lexer
from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.nodes.instrucciones.Print import Println
from backend.src.Interprete.simbol.ListaErrores import errores
from backend.src.Interprete.simbol.InstanciaTabla import st
from backend.src.Interprete.errors.Error import Error

# PRESEDENCIA Y ASOCIACION DE LOS OPERADORES
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','XOR'),
    ('right','NOT'),
    ('left','IGUALQUE','DIFERENTEQUE','MAYORQUE','MENORQUE','MAYORIGUALQUE','MENORIGUALQUE'),
    ('left','MAS','MENOS'),
    ('left','MULTIPLICACION','DIVISION'),
    ('nonassoc','POTENCIA'),
    ('right','UMENOS'),
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

def p_sentencia_empty(t):
    '''sentencias : '''
    pass

def p_sentencia_print(t):
    '''sentencia : PRINT PARENTESIS_IZQ expresion PARENTESIS_DER PUNTO_Y_COMA'''
    t[0] = Println(t[3], t.lineno(1), find_column(t, 1))  # Crea un nodo Println con la expresión a imprimir

'''PROCEDIMIENTOS -----------------'''
def p_sentencia_declaracion_proc(t):
    '''sentencia : PROC IDENTIFICADOR PARENTESIS_IZQ params PARENTESIS_DER LLAVE_IZQ sentencias LLAVE_DER'''
    # SE CREA UN NODO PROC CON EL NOMBRE Y LAS INSTRUCCIONES
    t[0] = Procedimiento(t[2], t[4], t[7], t.lineno(1), find_column(t, 1))  # Crea un nodo Procedimiento con el nombre, parámetros e instrucciones

def p_params(t):
    '''params : params param'''
    # SE AGREGA UN NUEVO PARAMETRO A LA LISTA DE PARAMETROS
    t[0] = t[1]
    t[0].append(t[2])  # Agrega el nuevo parámetro

def p_params_unico(t):
    '''params : param'''
    # SE CREA UNA LISTA CON UN SOLO PARAMETRO
    t[0] = list()
    t[0].append(t[1])  # Crea una lista con el único parámetro

def p_parametro(t):
    '''param : tipo DOS_PUNTOS IDENTIFICADOR'''
    # SE CREA UN NODO PARAMETRO CON EL TIPO Y EL IDENTIFICADOR
    t[0] = ParametroDefinicion(t[1], t[3], t.lineno(1), find_column(t, 1))  # Crea un nodo ParametroDefinicion con el tipo y el identificador

def p_sentencia_execute_proc(t):
    '''sentencia : EXEC IDENTIFICADOR PARENTESIS_IZQ args PARENTESIS_DER PUNTO_Y_COMA'''
    # SE CREA UN NODO NATIVE CON EL NOMBRE DEL PROCEDIMIENTO Y LOS ARGUMENTOS
    t[0] = Execute(t[2], t[4], t.lineno(1), find_column(t, 1))  # Crea un nodo Execute con el nombre del procedimiento y los argumentos

def p_args(t):
    '''args : args COMA arg'''
    # SE AGREGA UN NUEVO ARGUMENTO A LA LISTA DE ARGUMENTOS
    t[0] = t[1]
    t[0].append(t[3])  # Agrega el nuevo argumento

def p_args_unico(t):
    '''args : arg'''
    # SE CREA UNA LISTA CON UN SOLO ARGUMENTO
    t[0] = list()
    t[0].append(t[1])  # Crea una lista con el único argumento

'''VECTORES --------------------'''
def p_sentencia_declaracion_vector(t):
    '''sentencia : declaracion_vector'''
    # SE CREA UN NODO DECLARACION VECTOR CON EL TIPO, IDENTIFICADOR Y VALOR INICIAL
    t[0] = t[1]  # La sentencia es una declaración de vector, se asigna directamente

def p_declaracion_vector_valor(t):
    '''declaracion_vector : declaracion_vector_valor'''
    # SE CREA UN NODO DECLARACION VECTOR CON EL TIPO, IDENTIFICADOR Y VALORES
    t[0] = t[1]

def p_declaracion_vector_sin_valor(t):
    '''declaracion_vector : declaracion_vector_sin_valor'''
    # SE CREA UN NODO DECLARACION VECTOR CON EL TIPO Y IDENTIFICADOR, SIN VALORES INICIALES
    t[0] = t[1]

def p_declaracion_vector_sort(t):
    '''declaracion_vector : declaracion_vector_sort'''
    # SE CREA UN NODO DECLARACION VECTOR CON EL TIPO Y IDENTIFICADOR, SIN VALORES INICIALES
    t[0] = t[1]

def p_declaracion_vector_shuffle(t):
    '''declaracion_vector : declaracion_vector_shuffle'''
    # SE CREA UN NODO DECLARACION VECTOR CON EL TIPO Y IDENTIFICADOR, SIN VALORES INICIALES
    t[0] = t[1]

def p_vector_valor(t):
    '''declaracion_vector_valor : VECTOR CORCHETE_IZQ tipo CORCHETE_DER IDENTIFICADOR PARENTESIS_IZQ dimensiones PARENTESIS_DER IGUAL CORCHETE_IZQ vectores CORCHETE_DER PUNTO_Y_COMA'''
    t[0] = DeclaracionVector(t[3], t[5], t[7], t[11], t.lineno(1), find_column(t, 6))

def p_vector_valor_expresiones(t):
    '''declaracion_vector_valor : VECTOR CORCHETE_IZQ tipo CORCHETE_DER IDENTIFICADOR PARENTESIS_IZQ dimensiones PARENTESIS_DER IGUAL CORCHETE_IZQ expresiones CORCHETE_DER PUNTO_Y_COMA'''
    t[0] = DeclaracionVector(t[3], t[5], t[7], t[11], t.lineno(1), find_column(t, 6))

def p_vector_sin_valor(t):
    '''declaracion_vector_sin_valor : VECTOR CORCHETE_IZQ tipo CORCHETE_DER IDENTIFICADOR PARENTESIS_IZQ dimensiones PARENTESIS_DER PUNTO_Y_COMA'''
    t[0] = DeclaracionVector(t[3], t[5], t[7], None, t.lineno(1), find_column(t, 1))

def p_vector_sort(t):
    '''declaracion_vector_sort : VECTOR CORCHETE_IZQ tipo CORCHETE_DER IDENTIFICADOR PARENTESIS_IZQ dimensiones PARENTESIS_DER IGUAL sort PUNTO_Y_COMA'''
    t[0] = DeclaracionVector(t[3], t[5], t[7], t[10], t.lineno(1), find_column(t, 1))

def p_vector_shuffle(t):
    '''declaracion_vector_shuffle : VECTOR CORCHETE_IZQ tipo CORCHETE_DER IDENTIFICADOR PARENTESIS_IZQ dimensiones PARENTESIS_DER IGUAL shuffle PUNTO_Y_COMA'''
    t[0] = DeclaracionVector(t[3], t[5], t[7], t[10], t.lineno(1), find_column(t, 1))

def p_dimensiones(t):
    '''dimensiones : dimensiones COMA dimension'''
    # SE AGREGA UNA NUEVA DIMENSION A LA LISTA DE DIMENSIONES
    t[0] = t[1]
    t[0].append(t[3])  # Agrega la nueva dimensión a la lista de dimensiones

def p_dimensiones_unico(t):
    '''dimensiones : dimension'''
    # SE CREA UNA LISTA CON UNA SOLA DIMENSION
    t[0] = list()
    t[0].append(t[1])  # Crea una lista con la única dimensión

def p_dimension(t):
    '''dimension : ENTERO'''
    t[0] = int(t[1])  # Convierte el valor de la dimensión a entero

def p_vectores(t):
    '''vectores : vectores COMA vector'''
    # SE AGREGA UN NUEVO VECTOR A LA LISTA DE VECTORES
    t[0] = t[1]
    t[0].append(t[3])  # Agrega el nuevo vector a la lista de vectores

def p_vectores_unico(t):
    '''vectores : vector'''
    # SE CREA UNA LISTA CON UN SOLO VECTOR
    t[0] = list()
    t[0].append(t[1])  # Crea una lista con el único vector

def p_vector(t):
    '''vector : CORCHETE_IZQ expresiones CORCHETE_DER'''
    # SE CREA UN NODO VECTOR CON LAS EXPRESIONES DENTRO DE LOS CORCHETES
    t[0] = Vector(t[2], t.lineno(1), find_column(t, 1))  # Crea un nodo Vector con las expresiones dentro de los corchetes

def p_vector_vectores(t):
    '''vector : CORCHETE_IZQ vectores CORCHETE_DER'''
    # SE CREA UN NODO VECTOR CON LAS EXPRESIONES DENTRO DE LOS CORCHETES
    t[0] = Vector(t[2], t.lineno(1), find_column(t, 1))  # Crea un nodo Vector con las expresiones dentro de los corchetes

def p_vector_asignacion(t):
    '''asignacion_vector : IDENTIFICADOR indices IGUAL expresion PUNTO_Y_COMA'''
    t[0] = AsignacionVector(t[1], t[2], t[4], t.lineno(1), find_column(t, 4))

def p_expresiones(t):
    '''expresiones : expresiones COMA expresion'''
    # SE AGREGA UNA NUEVA EXPRESION A LA LISTA DE EXPRESIONES
    t[0] = t[1]
    t[0].append(t[3])  # Agrega la nueva expresión a la lista de expresiones

def p_expresiones_unico(t):
    '''expresiones : expresion'''
    # SE CREA UNA LISTA CON UNA SOLA EXPRESION
    t[0] = list()
    t[0].append(t[1])  # Crea una lista con la única expresión

def p_sentencia_declaracion(t):
    '''sentencia : declaracion'''
    t[0] = t[1]  # La sentencia es una declaración, se asigna directamente

def p_sentencia_asignacion(t):
    '''sentencia : asignacion'''
    t[0] = t[1]  # La sentencia es una asignación, se asigna directamente

def p_sentencia_asignacion_vector(t):
    '''sentencia : asignacion_vector'''
    # SE CREA UN NODO ASIGNACION VECTOR CON EL IDENTIFICADOR Y LA EXPRESION
    t[0] = t[1]  # La sentencia es una asignación de vector, se asigna directamente

def p_sentencia_if(t):
    '''sentencia : sentenciaIf'''
    t[0] = t[1]  # La sentencia es una sentencia If, se asigna directamente

def p_sentencia_bucle_break(t):
    '''sentencia : BREAK PUNTO_Y_COMA'''
    # SE CREA UN NODO BREAK PARA SALIR DEL BUCLE
    t[0] = Break(t[1], t.lineno(1), find_column(t, 1))  # Crea una lista con el nodo Break

def p_sentencia_bucle_continue(t):
    '''sentencia : CONTINUE PUNTO_Y_COMA'''
    # SE CREA UN NODO CONTINUE PARA SALTAR A LA SIGUIENTE ITERACION DEL BUCLE
    t[0] = Continue(t[1], t.lineno(1), find_column(t, 1))  # Crea una lista con el nodo Continue

def p_sentencia_while(t):
    '''sentencia : WHILE PARENTESIS_IZQ condicion PARENTESIS_DER LLAVE_IZQ sentencias LLAVE_DER'''
    # SE CREA UN NODO WHILE CON LA CONDICION Y LAS INSTRUCCIONES
    t[0] = While(t[3], t[6], t.lineno(1), find_column(t, 1))  # Crea un nodo While con la condición y las sentencias

def p_sentencia_for(t):
    '''sentencia : FOR PARENTESIS_IZQ inicio_for condicion PUNTO_Y_COMA actualizacion PARENTESIS_DER LLAVE_IZQ sentencias LLAVE_DER'''
    # SE CREA UN NODO FOR CON LA DECLARACION, CONDICION, ACTUALIZACION Y LAS INSTRUCCIONES
    t[0] = For(t[3], t[4], t[6], t[9], t.lineno(1), find_column(t, 1))  # Crea un nodo For con la declaración, condición, actualización y sentencias

def p_sentencia_do_while(t):
    '''sentencia : DO LLAVE_IZQ sentencias LLAVE_DER WHILE PARENTESIS_IZQ condicion PARENTESIS_DER'''
    # SE CREA UN NODO DO WHILE CON LAS INSTRUCCIONES Y LA CONDICION
    t[0] = DoWhile(t[3], t[7], t.lineno(1), find_column(t, 1))  # Crea un nodo While con la condición y las sentencias, indicando que es un do-while

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
    t[0] = Incremento(t[1], t.lineno(2), find_column(t, 2))  # Crea un nodo Incremento con el identificador

def p_actualizacion_decremento(t):
    '''actualizacion : IDENTIFICADOR DECREMENTO'''
    # SE CREA UN NODO ASIGNACION CON EL IDENTIFICADOR Y LA EXPRESION DE DECREMENTO
    t[0] = Decremento(t[1], t.lineno(2), find_column(t, 2))  # Crea un nodo Decremento con el identificador

def p_actualizacion_asignacion(t):
    '''actualizacion : IDENTIFICADOR IGUAL expresion'''
    # SE CREA UN NODO ASIGNACION CON EL IDENTIFICADOR Y LA EXPRESION
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(t, 1))  # Crea un nodo Asignacion con el identificador y la expresión

def p_sentencia_incremento(t):
    '''sentencia : IDENTIFICADOR INCREMENTO PUNTO_Y_COMA'''
    # SE CREA UN NODO ASIGNACION CON EL IDENTIFICADOR Y LA EXPRESION DE INCREMENTO
    t[0] = Incremento(t[1], t.lineno(2), find_column(t, 2))

def p_sentencia_decremento(t):
    '''sentencia : IDENTIFICADOR DECREMENTO PUNTO_Y_COMA'''
    # SE CREA UN NODO ASIGNACION CON EL IDENTIFICADOR Y LA EXPRESION DE DECREMENTO
    t[0] = Decremento(t[1], t.lineno(2), find_column(t, 2))

def p_asignacion(t):
    '''asignacion : IDENTIFICADOR IGUAL expresion PUNTO_Y_COMA'''
    # SE CREA UN NODO ASIGNACION CON EL IDENTIFICADOR Y LA EXPRESION
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(t, 1))

def p_declaracion_init(t):
    '''declaracion : declaracion_valor'''
    t[0] = t[1]

def p_declaracion_no_init(t):
    '''declaracion : declaracion_sin_valor'''
    t[0] = t[1]

def p_declaracion_op_igual(t):
    '''declaracion_valor : tipo IDENTIFICADOR IGUAL expresion PUNTO_Y_COMA'''
    t[0] = Declaracion(t[1], t[2], t[4], None, t.lineno(2), find_column(t, 2))

def p_declaracion_op_pto_y_coma(t):
    '''declaracion_sin_valor : tipo IDENTIFICADOR PUNTO_Y_COMA'''
    t[0] = Declaracion(t[1], t[2], None, None, t.lineno(2), find_column(t, 2))  # Declaración sin inicialización

def p_expresion_menos_int(t):
    'expresion : MENOS expresion %prec UMENOS'
    # SE CREA UN NODO RESTA CON EL VALOR 0 Y EL HIJO t[2]
    t[0] = Umenos(t[2], t.lineno(1), find_column(t, 1))  # Aplicar el signo negativo

def p_expresion_potencia(t):
    '''expresion : expresion POTENCIA expresion'''
    # SE CREA UN NODO POTENCIA CON LOS HIJOS t[1] Y t[3]
    t[0] = Potencia(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_expresion_multiplicacion(t):
    '''expresion : expresion MULTIPLICACION expresion'''
    # SE CREA UN NODO MULTIPLICACION CON LOS HIJOS t[1] Y t[3]
    t[0] = Multiplicacion(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_expresion_division(t):
    '''expresion : expresion DIVISION expresion'''
    # SE CREA UN NODO DIVISION CON LOS HIJOS t[1] Y t[3]
    t[0] = Division(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_expresion_suma(t):
    '''expresion : expresion MAS expresion'''
    #SE CREA UN NODO SUMA CON LOS HIJOS t[1] Y t[3]
    t[0] = Suma(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_expresion_resta(t):
    '''expresion : expresion MENOS expresion'''
    #SE CREA UN NODO RESTA CON LOS HIJOS t[1] Y t[3]
    t[0] = Resta(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_relacional_igualque(t):
    '''relacional : expresion IGUALQUE expresion'''
    # SE CREA UN NODO IGUALQUE CON LOS HIJOS t[1] Y t[3]
    t[0] = IgualQue(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_relacional_diferenteque(t):
    '''relacional : expresion DIFERENTEQUE expresion'''
    # SE CREA UN NODO DIFERENTEQUE CON LOS HIJOS t[1] Y t[3]
    t[0] = DiferenteQue(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_relacional_mayorque(t):
    '''relacional : expresion MAYORQUE expresion'''
    # SE CREA UN NODO MAYORQUE CON LOS HIJOS t[1] Y t[3]
    t[0] = MayorQue(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_relacional_mayorigualque(t):
    '''relacional : expresion MAYORIGUALQUE expresion'''
    # SE CREA UN NODO MAYORIGUALQUE CON LOS HIJOS t[1] Y t[3]
    t[0] = MayorIgualQue(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_relacional_menorque(t):
    '''relacional : expresion MENORQUE expresion'''
    # SE CREA UN NODO MENORQUE CON LOS HIJOS t[1] Y t[3]
    t[0] = MenorQue(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_relacional_menorigualque(t):
    '''relacional : expresion MENORIGUALQUE expresion'''
    # SE CREA UN NODO MENORIGUALQUE CON LOS HIJOS t[1] Y t[3]
    t[0] = MenorIgualQue(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_logica_not(t):
    '''logica : NOT expresion'''
    # SE CREA UN NODO NOT CON EL HIJO t[2]
    t[0] = Not(t[2], t.lineno(1), find_column(t, 1))

def p_logica_xor(t):
    '''logica : expresion XOR expresion'''
    # SE CREA UN NODO XOR CON LOS HIJOS t[1] Y t[3]
    t[0] = Xor(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_logica_and(t):
    '''logica : expresion AND expresion'''
    # SE CREA UN NODO AND CON LOS HIJOS t[1] Y t[3]
    t[0] = And(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_logica_or(t):
    '''logica : expresion OR expresion'''
    # SE CREA UN NODO OR CON LOS HIJOS t[1] Y t[3]
    t[0] = Or(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_expresion_modulo(t):
    '''expresion : expresion MODULO expresion'''
    # SE CREA UN NODO MODULO CON LOS HIJOS t[1] Y t[3]
    t[0] = Modulo(t[1], t[3], t.lineno(2), find_column(t, 2))

def p_expresion_relacionales(t):
    '''expresion : relacional'''
    t[0] = t[1] # SE ASIGNA LA COMPARACION RELACIONAL A t[0]

def p_expresion_logica(t):
    '''expresion : logica'''
    t[0] = t[1]  # SE ASIGNA LA EXPRESION LOGICA A t[0]

def p_expresion_id_k(t):
    '''expresion : acceso_vector'''
    # SE CREA UN NODO ACCESO VECTOR CON EL IDENTIFICADOR Y LA EXPRESION
    t[0] = t[1]

def p_expresion_seno(t):
    '''expresion : SENO PARENTESIS_IZQ expresion PARENTESIS_DER'''
    # SE CREA UN NODO SENO CON LA EXPRESION DENTRO DE LOS PARÉNTESIS
    t[0] = Seno(t[3], Tipos.FLOAT ,t.lineno(1), find_column(t, 1))  # Retorna el seno de la expresión

def p_expresion_coseno(t):
    '''expresion : COSENO PARENTESIS_IZQ expresion PARENTESIS_DER'''
    # SE CREA UN NODO COSENO CON LA EXPRESION DENTRO DE LOS PARÉNTESIS
    t[0] = Coseno(t[3], Tipos.FLOAT ,t.lineno(1), find_column(t, 1))  # Retorna el coseno de la expresión

def p_expresion_inversion(t):
    '''expresion : INVERSION PARENTESIS_IZQ expresion PARENTESIS_DER'''
    # SE CREA UN NODO INVERSION CON LA EXPRESION DENTRO DE LOS PARÉNTESIS
    t[0] = Inversion(t[3], Tipos.INT ,t.lineno(1), find_column(t, 1))  # Retorna la inversion de la expresión

def p_expresion_vector_sort(t):
    '''sort : SORT PARENTESIS_IZQ IDENTIFICADOR PARENTESIS_DER'''
    # SE CREA UN NODO VECTOR SORT CON EL ACCESO AL VECTOR
    t[0] = Sort(t[3], t.lineno(1), find_column(t, 4))  # Retorna el acceso al vector con la expresión de índice

def p_expresion_vector_shuffle(t):
    '''shuffle : SHUFFLE PARENTESIS_IZQ IDENTIFICADOR PARENTESIS_DER'''
    # SE CREA UN NODO VECTOR SHUFFLE CON EL ACCESO AL VECTOR
    t[0] = Shuffle(t[3], t.lineno(1), find_column(t, 4))  # Retorna el acceso al vector con la expresión de índice

def p_acceso_vector(t):
    '''acceso_vector : IDENTIFICADOR indices'''
    # SE CREA UN NODO ACCESO VECTOR CON EL IDENTIFICADOR Y LA EXPRESION
    t[0] = AccesoVector(t[1], t[2], t.lineno(1), find_column(t, 1))  # Retorna el acceso al vector con la expresión de índice

def p_indices(t):
    '''indices : indices indice'''
    # SE CREA UNA LISTA CON LOS ÍNDICES
    t[0] = t[1]
    t[0].append(t[2])  # Agrega el nuevo índice a la lista

def p_indices_unico(t):
    '''indices : indice'''
    # SE CREA UNA LISTA CON UN SOLO INDICE
    t[0] = list()
    t[0].append(t[1])  # Crea una lista con el único índice

def p_indice(t):
    '''indice : CORCHETE_IZQ expresion CORCHETE_DER'''
    # SE CREA UN NODO INDICE CON LA EXPRESION DENTRO DE LOS CORCHETES
    t[0] = t[2]  # Retorna la expresión dentro de los corchetes como índice

def p_expresion_identificador(t):
    '''expresion : IDENTIFICADOR'''
    # SE CREA UN NODO ACCESO VARIABLE CON EL IDENTIFICADOR
    t[0] = AccesoVariable(t[1], t.lineno(1), find_column(t, 1))

def p_logica_true(t):
    '''logica : TRUE'''
    # SE ASIGNA EL VALOR TRUE A t[0]
    t[0] = Nativo(Tipos.BOOL, True, t.lineno(1), find_column(t, 1))

def p_logica_false(t):
    '''logica : FALSE'''
    # SE ASIGNA EL VALOR FALSE A t[0]
    t[0] = Nativo(Tipos.BOOL, False, t.lineno(1), find_column(t, 1))

def p_logica_identificador(t):
    '''logica : IDENTIFICADOR'''
    # SE CREA UN NODO ACCESO VARIABLE CON EL IDENTIFICADOR
    t[0] = AccesoVariable(t[1], t.lineno(1), find_column(t, 1))  # Retorna el acceso a la variable

def p_expresion_entero(t):
    '''expresion : ENTERO'''
    # SE ASIGNA EL VALOR ENTERO A t[0]
    t[0] = Nativo(Tipos.INT, int(t[1]), t.lineno(1), find_column(t, 1))

def p_expresion_flotante(t):
    '''expresion : FLOTANTE'''
    # SE ASIGNA EL VALOR FLOTANTE A t[0]
    t[0] = Nativo(Tipos.FLOAT, float(t[1]), t.lineno(1), find_column(t, 1))

def p_expresion_true(t):
    '''expresion : TRUE'''
    t[0] = Nativo(Tipos.BOOL, True, t.lineno(1), find_column(t, 1))

def p_expresion_false(t):
    '''expresion : FALSE'''
    t[0] = Nativo(Tipos.BOOL, False, t.lineno(1), find_column(t, 1))

def p_expresion_cadena(t):
    '''expresion : CADENA'''
    t[0] = Nativo(Tipos.STRING, str(t[1]), t.lineno(1), find_column(t, 1))

def p_expresion_caracter(t):
    '''expresion : CARACTER'''
    # SE ASIGNA EL VALOR CARACTER A t[0]
    t[0] = Nativo(Tipos.CHAR, str(t[1]), t.lineno(1), find_column(t, 1))

def p_expresion_agrupada_exp(t):
    'expresion : expresion_agrupada'
    t[0] = t[1]  # Retorna la expresión agrupada

def p_expresion_agrupada(t):
    'expresion_agrupada : PARENTESIS_IZQ expresion PARENTESIS_DER'
    t[0] = t[2]  # Retorna la expresión dentro de los paréntesis

def p_sentencia_if_simple(t):
    '''sentenciaIf : IF PARENTESIS_IZQ condicion PARENTESIS_DER LLAVE_IZQ sentencias LLAVE_DER'''
    t[0] = If(t[3], t[6], t.lineno(1), find_column(t, 1))

def p_sentencia_if_else(t):
    '''sentenciaIf : IF PARENTESIS_IZQ condicion PARENTESIS_DER LLAVE_IZQ sentencias LLAVE_DER ELSE LLAVE_IZQ selse LLAVE_DER'''
    # SE CREA UN NODO IF CON LA CONDICION Y LAS INSTRUCCIONES
    t[0] = IfElse(t[3], t[6], t[10], t.lineno(1), find_column(t, 1))

def p_sentencia_else(t):
    '''selse : sentencias'''
    t[0] = Else(t[1], t.lineno(1), find_column(t, 1))

def p_sentencia_if_else_if(t):
    '''sentenciaIf : IF PARENTESIS_IZQ condicion PARENTESIS_DER LLAVE_IZQ sentencias LLAVE_DER ELSE sentenciaIf'''
    t[0] = IfElseIf(t[3], t[6], t[9], t.lineno(1), find_column(t, 1))

def p_sentencia_switch(t):
    '''sentencia : SWITCH PARENTESIS_IZQ expresion PARENTESIS_DER LLAVE_IZQ cases LLAVE_DER'''
    # SE CREA UN NODO SWITCH CON LA EXPRESION Y LAS INSTRUCCIONES
    t[0] = Switch(t[3], t[6], t.lineno(1), find_column(t, 1))  # Crea un nodo Switch con la expresión y las sentencias

def p_cases(t):
    '''cases : cases case'''
    # SE AGREGA UN NUEVO CASE A LA LISTA DE CASES
    t[0] = t[1]
    t[0].append(t[2])  # Agrega el nuevo case a la lista de cases

def p_cases_unico(t):
    '''cases : case'''
    # SE CREA UNA LISTA CON UN SOLO CASE
    t[0] = list()
    t[0].append(t[1])  # Crea una lista con el único case

def p_case(t):
    '''case : CASE expresion DOS_PUNTOS sentencias BREAK PUNTO_Y_COMA'''
    # SE CREA UN NODO CASE CON LA EXPRESION Y LAS INSTRUCCIONES
    t[0] = Case(t[2], t[4], t.lineno(1), find_column(t, 1))  # Crea un nodo Case con la expresión y las sentencias

def p_case_default(t):
    '''case : DEFAULT DOS_PUNTOS sentencias BREAK PUNTO_Y_COMA'''
    # SE CREA UN NODO CASE CON LA EXPRESION DEFAULT Y LAS INSTRUCCIONES
    t[0] = Case(Nativo(Tipos.STRING, t[1]), t[3], t.lineno(1), find_column(t, 1))  # Crea un nodo Case con la expresión None (default) y las sentencias

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

def find_column(p, i):
    last_cr = p.lexer.lexdata.rfind('\n', 0, p.lexpos(i))
    if last_cr < 0:
        last_cr = 0
    column = (p.lexpos(i) - last_cr) + 1
    return column

def find_column_error(token):
    """
    Calcula la columna del token de error.
    Recibe un token (t) y retorna la columna donde ocurrió el error.
    """
    if not token:
        return 1  # Si no hay token, retorna columna 1
    # token.lexpos es la posición absoluta en el texto fuente
    line_start = token.lexer.lexdata.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def p_error(p):
    global parser
    
    # Contador para evitar bucles infinitos
    contador_error = getattr(parser, '_error_counter', 0)
    parser._error_counter = contador_error + 1
    
    # Si hemos tenido demasiados errores consecutivos, descartamos el token actual y continuamos
    if contador_error > 10:
        parser._error_counter = 0
        parser.errok()
        return

    if not p:
        print("Fin de entrada inesperado")
        return None

    # Si el token actual ya es un token de sincronización, solo continúa
    if p.type in ['PUNTO_Y_COMA', 'LLAVE_DER']:
        parser.errok()
        parser._error_counter = 0  # Reiniciar contador
        return

    print(f"Error de sintaxis: token inesperado '{p.value}' en línea {p.lineno}")
    try:
        columna = find_column_error(p)
        nuevo_error = Error('sintactico', f"token inesperado '{p.value}'", int(p.lineno), columna)
        errores.append(nuevo_error)
    except Exception as e:
        print(f"Error al agregar a la lista de errores: {e}")

    # Ampliar tokens de sincronización para incluir palabras clave que inician sentencias
    tokens_sincronizacion = ['PUNTO_Y_COMA', 'LLAVE_DER', 'PRINTLN', 'IF', 'WHILE', 'FOR', 'SWITCH', 'BREAK', 'CONTINUE', 'RETURN']
    
    # Buscar un token de sincronización y retornarlo
    while True:
        tok = parser.token()
        if not tok:
            break
        
        if tok.type in tokens_sincronizacion:
            parser.errok()
            parser._error_counter = 0  # Reiniciar contador
            
            # Si encontramos un token que es inicio de sentencia (no punto y coma o llave),
            # lo devolvemos para que el parser lo procese como inicio de una nueva sentencia
            if tok.type in ['PRINTLN', 'IF', 'WHILE', 'FOR', 'SWITCH', 'BREAK', 'CONTINUE', 'RETURN']:
                return tok
            
            # Si es punto y coma o llave, lo retornamos para sincronizar
            return tok
    
    # Si no encontramos un token de sincronización
    parser.errok()
    return
    
    # Si llegamos aquí, encontramos un punto y coma o llave, o llegamos al final
    parser.errok()
    
    # Intento agresivo de recuperación: descarta el estado de pila actual
    # y fuerza al parser a reiniciar desde una producción de nivel superior
    # Este es un último recurso y podría causar problemas, pero evitará bucles infinitos
    parser.restart()  # Nota: este método es conceptual, PLY no lo tiene así
    
    return

# def p_error(p):
#     if not p:
#         print("Fin de entrada inesperado")
#         return

#     print(f"Error de sintaxis: token inesperado '{p.value}'")
#     try:
#         columna = find_column_error(p)
#         nuevoError = Error('sintactico', f"token inesperado '{p.value}'", int(p.lineno), columna)
#         errores.append(nuevoError)
#     except Exception as e:
#         print(f"Error al agregar a la lista de errores: {e}")

#     # Sincroniza: avanza hasta encontrar un token seguro (por ejemplo, ';' o '}')
#     # while True:
#     #     tok = parser.token()  # Obtiene el siguiente token
#     #     if not tok or tok.type == 'newLine' or tok.type == 'PUNTO_Y_COMA' or tok.type == 'LLAVE_DER':
#     #         break
#     return recuperar_error(p)


# def p_error(t):
#     if t:
#         print(f"Error de sintaxis: token inesperado '{t.value}' en línea {t.lineno}")
#         errores.append("sintáctico",  f"token inesperado '{t.value}' en", t.lineno, find_column(t, 1))
#     else:
#         print("Error de sintaxis: fin de entrada inesperado")
#         errores.append("sintáctico", "fin de entrada inesperado", t.lineno, find_column(t, 1))


print("Construyendo el analizador sintáctico...\n")
parser = yacc.yacc(debug=True)

def parse(input_text):
    lexer_instance = build_lexer()  # Nueva instancia por cada análisis
    return parser.parse(input_text, lexer=lexer_instance)