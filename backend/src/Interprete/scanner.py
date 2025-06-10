import ply.lex as lex
import os

# DEFINICIÓN DE TODOS LOS TOKENS DEL LENGUAJE
tokens = (
    'IGUAL',
    'PUNTO_Y_COMA',
    'COMA',
    'TRUE',
    'FALSE',
    'MAS',
    'MENOS',
    'MULTIPLICACION',
    'DIVISION',
    'POTENCIA',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'TIPO_INT',
    'TIPO_FLOAT',
    'TIPO_BOOL',
    'TIPO_CHAR',
    'TIPO_STR',
    'PRINT',
    'IDENTIFICADOR',
    'COMENTARIOLINEA',
    'COMENTARIOMULTILINEA',
    'ENTERO',
    'FLOTANTE',
    'CADENA',
    'CARACTER',
    'INCREMENTO',
    'DECREMENTO',
    'IGUALQUE',
    'DIFERENTEQUE',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUALQUE',
    'MENORIGUALQUE',
    'NEGACION',
    'MODULO',
    'AND',
    'OR',
    'NOT',
    'XOR',
)

# EXPRESIONES REGULARES PARA PALABRAS Y SÍMBOLOS RESERVADOS DEL LENGUAJE
t_IGUALQUE = r'=='
t_IGUAL = r'='
t_INCREMENTO = r'\+\+'
t_MAS = r'\+'
t_DECREMENTO = r'--'
t_MENOS = r'-'
t_POTENCIA = r'\*\*'
t_MULTIPLICACION = r'\*'
t_DIFERENTEQUE = r'!='
t_NEGACION = r'!'
t_MAYORIGUALQUE = r'>='
t_MAYORQUE = r'>'
t_MENORIGUALQUE = r'<='
t_MENORQUE = r'<'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_XOR = r'\^'
t_PUNTO_Y_COMA = r';'
t_COMA = r','
t_DIVISION = r'/'
t_MODULO = r'%'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'

#PALABRAS RESERVADAS DEL LENGUAJE
def t_PRINT(t):
    r'[Pp][Rr][Ii][Nn][Tt][Ll][Nn]'
    t.value = str(t.value)
    return t

def t_TRUE(t):
    r'[Tt][Rr][Uu][Ee]\b'
    try:
        t.value = 'true'
    except ValueError:
        print(f"Valor inválido para TRUE: {t.value}")
        t.value = 'false'
    return t

def t_FALSE(t):
    r'[Ff][Aa][Ll][Ss][Ee]\b'
    try:
        t.value = 'false'
    except ValueError:
        print(f"Valor inválido para FALSE: {t.value}")
        t.value = 'false'
    return t

def t_TIPO_FLOAT(t):
    r'[Ff][Ll][Oo][Aa][Tt]\b'
    try:
        t.value = str(t.value)
    except ValueError:
        print(f"Valor inválido para TIPO_FLOAT: {t.value}")
        t.value = ""
    t.value = t.value.lower()
    return t

def t_TIPO_INT(t):
    r'[Ii][Nn][Tt]\b'
    try:
        t.value = str(t.value)
    except ValueError:
        print(f"Valor inválido para TIPO_INT: {t.value}")
        t.value = ""
    t.value = t.value.lower()
    return t

def t_TIPO_BOOL(t):
    r'[Bb][Oo][Oo][Ll]\b'
    try:
        t.value = str(t.value)
    except ValueError:
        print(f"Valor inválido para TIPO_BOOL: {t.value}")
        t.value = ""
    t.value = t.value.lower()
    return t

def t_TIPO_CHAR(t):
    r'[Cc][Hh][Aa][Rr]\b'
    try:
        t.value = str(t.value)
    except ValueError:
        print(f"Valor inválido para TIPO_CHAR: {t.value}")
        t.value = ""
    t.value = t.value.lower()
    return t

def t_TIPO_STR(t):
    r'[Ss][Tt][Rr]\b'
    try:
        t.value = str(t.value)
    except ValueError:
        print(f"Valor inválido para TIPO_STR: {t.value}")
        t.value = ""
    t.value = t.value.lower()
    return t

# EXPRESIONES REGULARES PARA TOKENS DEL LENGUAJE

def t_IDENTIFICADOR(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    try:
        t.value = str(t.value)
    except ValueError:
        print(f"Identificador inválido: {t.value}")
        t.value = ""
    t.value = t.value.lower()
    return t

def t_COMENTARIOLINEA(t):
    r'//.*'
    pass  # Ignorar comentarios de una línea

def t_COMENTARIOMULTILINEA(t):
    r'/\*(.|[\n])*\*/'
    #r'/\*(.*?)\*/'
    t.lexer.lineno += t.value.count("\n")
    pass  # Ignorar comentarios de varias líneas

def t_FLOTANTE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print(f"Valor flotante inválido: {t.value}")
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f"Valor entero inválido: {t.value}")
        t.value = 0
    return t

def t_CADENA(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value.replace('"', '')
    return t

def t_CARACTER(t):
    r"'[^']*'"
    t.value = t.value.replace("'", "")
    return t

def t_whitespace(t):
    r'[ \t]+'
    pass  # Ignorar espacios en blanco

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter no reconocido '%s'" % t.value[0])
    print("En la línea %d, columna %d" % (t.lineno, find_column(t.lexer.lexdata, t)))
    #raise Exception(f"Error léxico: caracter '{t.value[0]}' no reconocido en la línea {t.lineno}, columna {find_column(t.lexer.lexdata, t)}")

# Construir el analizador léxico
print("Construyendo el analizador léxico...")
lexer = lex.lex()
# print(os.getcwd())
# with open("./backend/src/Interprete/entrada.txt", "r", encoding="utf-8") as f:
#     data = f.read()
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)