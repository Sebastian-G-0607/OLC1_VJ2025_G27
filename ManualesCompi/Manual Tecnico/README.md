# 📚 Manual Técnico  
## 💻 Proyecto - Lenguaje OBJ-C  
**📔Curso:** Organización de Lenguajes y Compiladores 1  
**📍 Sección P**  
**🏛️ Universidad de San Carlos de Guatemala**    

**Integrantes:**  
- 📌 Eduardo Sebastián Gutiérrez de Felipe 
- 📌 Carlos Eduardo Lau López
- 📌 Sebastián Antonio Romero Tzitizmit
- 📌 Christian David Chinchilla Santos

---

##  📘Índice

1. [Introducción](#introducción)  
2. [Arquitectura del Sistema](#arquitectura-del-sistema)   
3. [Frontend](#frontend)    
    1. [Componentes y funcionalidades](#componentes-y-funcionalidades)  
    2. [Comunicación con el Backend](#comunicación-con-el-backend)  
4. [Backend](#backend)   
    1. [Explicación de los analizadores (léxico y sintáctico)](#explicación-de-los-analizadores-léxico-y-sintáctico) 
    2. [Gramatica BNF](#gramatica-bnf) 
    3. [Construcción del AST](#construcción-del-ast)  
    4. [Generación de reportes](#generación-de-reportes)  
5. [Librerías y Dependencias](#librerías-y-dependencias)  

---
## 📘 Introducción

📍 El presente Manual Técnico documenta el diseño, desarrollo e implementación del **Proyecto Fase I y Fase II - Lenguaje OBJ-C**, elaborado como parte del curso **Organización de Lenguajes y Compiladores 1**, Sección P, de la Facultad de Ingeniería de la Universidad de San Carlos de Guatemala.

El objetivo del proyecto es la creación de un compilador parcial para el lenguaje OBJ-C, un lenguaje propio definido en el enunciado del proyecto, el cual permite realizar análisis léxico, sintáctico, construcción de Árbol de Sintaxis Abstracta (AST), generación de reportes (errores, tabla de símbolos, memoria) y visualización interactiva del proceso de compilación.

📌 El sistema está compuesto por dos módulos principales:

- **Frontend**: una interfaz gráfica amigable, desarrollada con **React + Vite**, que permite a los usuarios escribir, cargar e interpretar código en OBJ-C, así como visualizar los reportes generados por el backend.
- **Backend**: un servidor en **Python** que utiliza la librería **PLY (Python Lex-Yacc)** para realizar el análisis léxico y sintáctico del código fuente, validar semántica, construir el AST y generar los reportes necesarios. El backend expone una API REST que es consumida por el frontend.

Este manual técnico describe en detalle la arquitectura de la solución, la estructura de los componentes, la implementación del compilador parcial, el flujo de ejecución y las consideraciones técnicas que permitirán comprender y mantener el sistema a futuro.

El documento está dirigido a desarrolladores que deseen comprender el funcionamiento interno del compilador OBJ-C, a tutores académicos y al catedrático del curso.

---

## 📘 Arquitectura del Sistema

El sistema del compilador parcial para el lenguaje OBJ-C ha sido diseñado bajo una arquitectura **cliente-servidor**, que separa claramente las responsabilidades entre la interfaz de usuario (frontend) y el procesamiento del código (backend).

### Componentes principales

1. **✨Frontend**  
    - Implementado con **React** y el framework de desarrollo rápido **Vite**.  
    - Proporciona la interfaz gráfica para que el usuario pueda:  
        - Escribir o cargar archivos de código fuente `.objc`.  
        - Enviar el código al backend para ser interpretado.  
        - Visualizar la salida de la interpretación.  
        - Consultar los reportes generados: reporte de errores, tabla de símbolos, AST, memoria, advertencias.

2. 🧠 **Backend**  
    - Implementado en **Python**.  
    - Utiliza la librería **PLY (Python Lex-Yacc)** para realizar el análisis léxico y sintáctico del código OBJ-C.  
    - Expone una **API REST** desarrollada con **Flask**, que permite al frontend enviar código y recibir resultados en formato JSON.  
    - Realiza las siguientes tareas:  
        - Tokenización (análisis léxico)  
        - Parsing (análisis sintáctico)  
        - Validación semántica  
        - Construcción del Árbol de Sintaxis Abstracta (AST)  
        - Generación de reportes (errores, símbolos, memoria, advertencias)

### 🌀 Flujo de datos

1. El usuario escribe o carga código fuente en el editor del frontend.  
2. Al presionar el botón **Interpretar**, el frontend envía una petición POST al endpoint `/interpret` del backend, con el código fuente en el cuerpo de la petición.  
3. El backend procesa el código:  
    - Realiza el análisis léxico.  
    - Construye el AST.  
    - Valida la semántica.  
    - Genera los reportes.  
4. El backend responde al frontend con:  
    - La cantidad de errores encontrados.  
    - Mensaje de estado de la interpretación.  
5. El usuario puede consultar los distintos reportes desde los botones habilitados en la interfaz.  

---

## 🌐 Frontend

El frontend de la aplicación fue desarrollado utilizando **React**, junto con el framework de desarrollo rápido **Vite**, que permite tiempos de carga reducidos y una configuración optimizada para proyectos modernos de JavaScript.

📌El objetivo del frontend es proporcionar una interfaz gráfica amigable que permita al usuario:

- Escribir o cargar código fuente en el lenguaje OBJ-C.
- Interpretar el código.
- Visualizar la salida de la ejecución.
- Consultar los reportes generados por el backend (errores, AST, tabla de símbolos, memoria, advertencias).

---
### ⚙️ Componentes y funcionalidades

A continuación se describen los principales componentes y funcionalidades implementadas en el frontend:

---

#### **Editor.jsx**

El componente **Editor.jsx** es un editor de texto (implementado como `<textarea>` o editor enriquecido como CodeMirror) donde el usuario puede:

- Escribir código manualmente en el lenguaje OBJ-C.
- Cargar código desde un archivo `.objc` (botón Cargar Archivo).
- Modificar el código antes de interpretarlo.

Ejemplo de estructura básica del editor:

```jsx
<textarea
    value={codigo}
    onChange={(e) => setCodigo(e.target.value)}
    rows="20"
    cols="80"
    placeholder="Escriba su código en OBJ-C aquí..."
></textarea>
```
---

#### *ButtonsPanel.jsx*

```jsx 
import React from "react";

function ButtonsPanel({ onInterpretar, onCargarArchivo, onMostrarReporte }) {
    return (
        <div className="buttons-panel">
            <button onClick={onInterpretar}>Interpretar</button>
            <input
                type="file"
                accept=".objc"
                onChange={onCargarArchivo}
                style={{ marginLeft: "10px" }}
            />
            <button onClick={() => onMostrarReporte("errores")}>Reporte de Errores</button>
            <button onClick={() => onMostrarReporte("simbolos")}>Tabla de Símbolos</button>
            <button onClick={() => onMostrarReporte("ast")}>AST</button>
            <button onClick={() => onMostrarReporte("vectores")}>Vectores</button>
            <button onClick={() => onMostrarReporte("memoria")}>Memoria</button>
            <button onClick={() => onMostrarReporte("advertencias")}>Advertencias</button>
        </div>
    );
}

export default ButtonsPanel; 
```
#### *Console.jxs*

``` jsx
import React from "react";

function Console({ salidaConsola }) {
    return (
        <div className="console">
            <h3>Consola de Salida</h3>
            <pre>{salidaConsola}</pre>
        </div>
    );
}

export default Console;
```
#### *Cargar Archivo*
``` jsx
    const handleFileButtonClick = () => {
        fileInputRef.current.value = ''; // Permite cargar el mismo archivo varias veces
        fileInputRef.current.click();
    };
```
#### *Interpretar Codigo*
``` jsx
const handleInterpretarClick = async () => {
        try {
            if (resultadoRef.current) {
                resultadoRef.current.value = '';
            }
            const codigo = textareaRef.current ? textareaRef.current.value : '';
            const data = {
                code: codigo,
            }
            const response = await getParse(data); // Envía el código al backend
            if (resultadoRef.current) {
                resultadoRef.current.value = response.consola; // Muestra la respuesta en el textarea de salida
            }
            console.log(response);
        } catch (error) {
            console.error('Error al interpretar el código:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Ocurrió un error al interpretar el código. Por favor, revisa tu código y vuelve a intentarlo.',
                footer: 'Consulta el reporte de errores para más detalles',
            });
        }
    };
```

### 📨 Comunicación con el Backend

La comunicación entre el **frontend** y el **backend** se realiza mediante peticiones HTTP bajo el patrón **API REST**.

El backend, implementado en Python con Flask, expone los siguientes endpoints principales:

| 📌 Endpoint               | 📌 Método | 📌 Descripción                                                                 |
|------------------------|--------|-----------------------------------------------------------------------------|
| `/parse`               | POST   | Recibe el código fuente y devuelve el análisis sintáctico                  |
| `/ast`                 | POST   | Recibe el código fuente y devuelve el AST (como blob)                      |
| `/reporte/memoria`     | POST   | Recibe el código fuente y devuelve el reporte de memoria (HTML)            |
| `/reporte/vectores`    | GET    | Devuelve el reporte de vectores                                             |
| `/reporte/advertencias`| POST   | Recibe el código fuente y devuelve el reporte de advertencias (HTML)       |

---

### Flujo de comunicación

1. El usuario escribe o carga código en el editor.  

2. Al presionar el botón **Interpretar**, el frontend realiza una petición POST al endpoint `/interpret`, enviando el código como JSON.  

3.El backend procesa el código y responde con un objeto JSON que contiene:
- La salida generada (consola)
- La cantidad de errores
- Estado del análisis

4. Los botones de reportes generan peticiones GET a los otros endpoints para mostrar la información específica (AST, símbolos, errores...).

---

### Ejemplo de implementación de la llamada desde React

En el archivo `/parse` se define la función:

```js
// api.js

export const getParse = async (input) => {
    try {
        const response = await axios.post('/parse', { input });
        return response.data;        
    } catch (error) {
        if (error.response.data) throw new Error(error.response.data.error)
        throw new Error(`Error al obtener el parse: ${error}`);
    }
}

```
## 🧠 Backend

📌 El backend de la aplicación fue desarrollado en **Python 3.x**.  
Su objetivo principal es procesar el código fuente escrito en el lenguaje OBJ-C mediante las siguientes fases:

- Análisis léxico
- Análisis sintáctico
- Construcción del Árbol de Sintaxis Abstracta (AST)
- Validación semántica
- Generación de reportes
- Exposición de una API REST que consume el frontend

📌 El backend utiliza las siguientes tecnologías principales:

- **PLY (Python Lex-Yacc)**: librería que permite definir analizadores léxicos y sintácticos.
- **Flask**: framework ligero para exponer una API REST.

---

## 👣 Explicación de los analizadores (léxico y sintáctico)

El backend del proyecto implementa dos analizadores principales:

1. **Analizador Léxico** → definido en `lexer.py`  
2. **Analizador Sintáctico** → definido en `parser.py`

Ambos trabajan en conjunto para procesar el código OBJ-C que escribe el usuario.

---

### Analizador Léxico (scanner.py)

El **analizador léxico** transforma el código fuente en una **secuencia de tokens**.  
Cada token corresponde a una palabra clave, símbolo, número o identificador válido en el lenguaje OBJ-C.

Se implementa usando **PLY (Python Lex)**, que permite definir tokens con expresiones regulares.

---

#### Definición de tokens

```python
# scanner.py

# DEFINICIÓN DE TODOS LOS TOKENS DEL LENGUAJE
tokens = (
    'IGUAL',
    'PUNTO_Y_COMA',
    'DOS_PUNTOS',
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
    'MODULO',
    'AND',
    'OR',
    'NOT',
    'XOR',
    'IF',
    'ELSE',
    'SWITCH',
    'CASE',
    'DEFAULT',
    'LLAVE_IZQ',
    'LLAVE_DER',
    'CORCHETE_IZQ',
    'CORCHETE_DER',
    'WHILE',
    'FOR',
    'DO',
    'BREAK',
    'CONTINUE',
    'PROC',
    'EXEC',
    'VECTOR',
    'SENO',
    'COSENO',
    'INVERSION',
    'SHUFFLE',
    'SORT',
)
```

####  EXPRESIONES REGULARES PARA PALABRAS Y SÍMBOLOS RESERVADOS DEL LENGUAJE
```CS
t_IGUALQUE = r'=='
t_IGUAL = r'='
t_INCREMENTO = r'\+\+'
t_MAS = r'\+'
t_DECREMENTO = r'--'
t_MENOS = r'-'
t_POTENCIA = r'\*\*'
t_MULTIPLICACION = r'\*'
t_DIFERENTEQUE = r'!='
t_NOT = r'!'
t_MAYORIGUALQUE = r'>='
t_MAYORQUE = r'>'
t_MENORIGUALQUE = r'<='
t_MENORQUE = r'<'
t_AND = r'&&'
t_OR = r'\|\|'
t_XOR = r'\^'
t_DOS_PUNTOS = r':'
t_PUNTO_Y_COMA = r';'
t_COMA = r','
t_DIVISION = r'/'
t_MODULO = r'%'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'

```
### Palabras reservadas del lenguaje
```python
#PALABRAS RESERVADAS DEL LENGUAJE
def t_PROC(t):
    r'[Pp][Rr][Oo][Cc]\b'
    t.value = str(t.value)
    t.value = t.value.lower()
    return t

def t_EXEC(t):
    r'[Ee][Xx][Ee][Cc]\b'
    t.value = str(t.value)
    t.value = t.value.lower()
    return t

def t_VECTOR(t):
    r'[Vv][Ee][Cc][Tt][Oo][Rr]\b'
    t.value = str(t.value)
    t.value = t.value.lower()
    return t

def t_PRINT(t):
    r'[Pp][Rr][Ii][Nn][Tt][Ll][Nn]'
    t.value = str(t.value)
    t.value = t.value.lower()
    return t

def t_IF(t):
    r'[Ii][Ff]'
    t.value = str(t.value)
    t.value = t.value.lower()
    return t

def t_ELSE(t):
    r'[Ee][Ll][Ss][Ee]'
    t.value = str(t.value)
    t.value = t.value.lower()
    return t

def t_SWITCH(t):
    r'[Ss][Ww][Ii][Tt][Cc][Hh]'
    t.value = str(t.value)
    t.value = t.value.lower()
    return t

def t_CASE(t):
    r'[Cc][Aa][Ss][Ee]'
    t.value = str(t.value)
    t.value = t.value.lower()
    return t

def t_DEFAULT(t):
    r'[Dd][Ee][Ff][Aa][Uu][Ll][Tt]'
    t.value = str(t.value)
    t.value = t.value.lower()
    return t

def t_WHILE(t):
    r'[Ww][Hh][Ii][Ll][Ee]'
    t.value = str(t.value)
    t.value = t.value.lower()
    return t

def t_FOR(t):
    r'[Ff][Oo][Rr]'
    t.value = str(t.value)
    t.value = t.value.lower()
    return t

def t_DO(t):
    r'[Dd][Oo]'
    t.value = str(t.value)
    t.value = t.value.lower()
    return t

def t_BREAK(t):
    r'[Bb][Rr][Ee][Aa][Kk]'
    t.value = str(t.value)
    t.value = t.value.lower()
    return t

def t_CONTINUE(t):
    r'[Cc][Oo][Nn][Tt][Ii][Nn][Uu][Ee]'
    t.value = str(t.value)
    t.value = t.value.lower()
    return t

def t_TRUE(t):
    r'[Tt][Rr][Uu][Ee]'
    t.value = 'true'
    return t

def t_FALSE(t):
    r'[Ff][Aa][Ll][Ss][Ee]'
    try:
        t.value = 'false'
    except ValueError:
        print(f"Valor inválido para FALSE: {t.value}")
        t.value = 'false'
    return t

def t_SENO(t):
    r'[Ss][Ee][Nn][Oo]'
    try:
        t.value = 'seno'
    except ValueError:
        print(f"Valor inválido para SENO: {t.value}")
        t.value = 'seno'
    return t

def t_COSENO(t):
    r'[Cc][Oo][Ss][Ee][Nn][Oo]'
    try:
        t.value = 'coseno'
    except ValueError:
        print(f"Valor inválido para COSENO: {t.value}")
        t.value = 'coseno'
    return t

def t_INVERSION(t):
    r'[Ii][Nn][Vv]'
    try:
        t.value = t.value.lower()
    except ValueError:
        print(f"Valor inválido para INVERSION: {t.value}")
        t.value = 'inv'
    return t

def t_SHUFFLE(t):
    r'[Ss][Hh][Uu][Ff][Ff][Ll][Ee]'
    try:
        t.value = t.value.lower()
    except ValueError:
        print(f"Valor inválido para SHUFFLE: {t.value}")
        t.value = 'shuffle'
    return t

def t_SORT(t):
    r'[Ss][Oo][Rr][Tt]'
    try:
        t.value = t.value.lower()
    except ValueError:
        print(f"Valor inválido para SORT: {t.value}")
        t.value = 'sort'
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
```

### EXPRESIONES REGULARES PARA TOKENS DEL LENGUAJE
```python
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
    t.value = t.value[1:-1]  # Quita las comillas
    # Solo reemplaza los escapes más comunes
    t.value = t.value.replace(r'\"', '"').replace(r'\\', '\\').replace(r'\n', '\n').replace(r'\t', '\t').replace(r'\'', '\'')
    return t

def t_CARACTER(t):
    r"'(\\.|[^'])'"
    t.value = t.value[1:-1]  # Quita las comillas
    t.value = t.value.replace(r'\"', '"').replace(r'\\', '\\').replace(r'\n', '\n').replace(r'\t', '\t').replace(r'\'', '\'')
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
    print("Caracter no reconocido '%s'" % t.value[0], "en la línea %d, columna %d" % (t.lineno, find_column(t.lexer.lexdata, t)))
    nuevoError = Error('lexico', f"caracter no reconocido", t.lineno, find_column(t.lexer.lexdata, t))
    errores.append(nuevoError)
    t.lexer.skip(1)  # Avanza al siguiente carácter
    #raise Exception(f"Error léxico: caracter '{t.value[0]}' no reconocido en la línea {t.lineno}, columna {find_column(t.lexer.lexdata, t)}")
```
---
# 🔨 Analizador Sintáctico (parser.py)

El **analizador sintáctico** recibe la secuencia de tokens producida por el lexer y verifica que la estructura del código cumpla con la gramática definida para el lenguaje OBJ-C.

El parser está implementado en el archivo `parser.py` usando la librería **PLY (Python Yacc)**.

Además de validar la sintaxis, el parser construye el **Árbol de Sintaxis Abstracta (AST)** que representa la estructura del programa.

---

#### Estructura del parser

```python
import ply.yacc as yacc
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

```

### Ejemplo: asignación de variable
```python
def p_sentencia_asignacion(t):
    '''sentencia : asignacion'''
    t[0] = t[1]  # La sentencia es una asignación, se asigna directamente

def p_asignacion(t):
    '''asignacion : IDENTIFICADOR IGUAL expresion PUNTO_Y_COMA'''
    # SE CREA UN NODO ASIGNACION CON EL IDENTIFICADOR Y LA EXPRESION
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(t, 1))
```
### Ejemplo: expresión numérica
```python
def p_tipo_int(t):
    'tipo : TIPO_INT'
    t[0] = t[1]

def p_tipo_float(t):
    'tipo : TIPO_FLOAT'
    t[0] = t[1]
```
---
## Gramatica BNF
🔷 1. PROGRAMA Y SENTENCIAS
```HTML
    <sentencia> ::= "PRINT" "(" <expresion> ")" ";"
             | <declaracion>
             | <asignacion>  
             | <incremento> 
             | <decremento>  
             | <asignacion_vector> 
             | <sentencia_if> 
             | "BREAK" ";"
             | "CONTINUE" ";"
             | <sentencia_while> 
             | <sentencia_for>
             | <sentencia_do_while>  
             | <declaracion_vector>  
             | <switch>
             | <proc> 
             | <exec> 
```

🔷2. DECLARACIONES, ASIGNACION, INCREMENTO Y DECREMENTO

```HTML
    <declaracion> ::= <declaracion_valor>
               | <declaracion_sin_valor>

        <declaracion_valor> ::= <tipo> IDENTIFICADOR "=" <expresion> ";"

        <declaracion_sin_valor> ::= <tipo> IDENTIFICADOR ";"

    <asignacion> ::= IDENTIFICADOR "=" <expresion> ";"

    <incremento> ::= IDENTIFICADOR "++" ";"

    <decremento> ::= IDENTIFICADOR "--" ";"
```
- 🖇️ 2.1 . TIPOS
```HTML
        <tipo> ::= "int"
            | "float"
            | "bool"
            | "char"
            | "str"
```

-  🖇️2.2 . EXPRESIONES 
```HTML
        <expresion> ::= <expresion> "+" <expresion>
                | <expresion> "-" <expresion>
                | <expresion> "*" <expresion>
                | <expresion> "/" <expresion>
                | <expresion> "%" <expresion>
                | <expresion> "^" <expresion>
                | "-" <expresion>
                | "(" <expresion> ")"
                | <relacional> 
                | <logica>  
                | <acceso_vector> 
                | IDENTIFICADOR
                | ENTERO
                | FLOTANTE
                | "TRUE"
                | "FALSE"
                | CADENA
                | CARACTER
                | <funcion_seno>
                | <funcion_coseno> 
                | <funcion_inversion>

        <expresiones> ::= <expresiones> "," <expresion>
                | <expresion>
```


- ⛓️‍💥 2.2.1.  RELACIONALES Y LÓGICAS

```HTML
            <relacional> ::= <expresion> "==" <expresion>
                    | <expresion> "!=" <expresion>
                    | <expresion> ">" <expresion>
                    | <expresion> ">=" <expresion>
                    | <expresion> "<" <expresion>
                    | <expresion> "<=" <expresion>

            <logica> ::= "!" <expresion>
                | <expresion> "AND" <expresion>
                | <expresion> "OR" <expresion>
                | <expresion> "XOR" <expresion>
                | "TRUE"
                | "FALSE"
                | IDENTIFICADOR
```
- ⛓️‍💥 2.2.2 FUNCIONES MATEMÁTICAS
```HTML
            <funcion_seno> ::= "SENO" "(" <expresion> ")"
            <funcion_coseno> ::= "COSENO" "(" <expresion> ")"
            <funcion_inversion> ::= "INVERSION" "(" <expresion> ")"
```

🔷 3. ASIGNACION Y DECLARACION DE VECTORES
```HTML
        <declaracion_vector> ::= <vector_valor>
                            | <vector_sin_valor>
                            | <vector_sort>
                            | <vector_shuffle>

        <vector_valor> ::= "VECTOR" "[" <tipo> "]" IDENTIFICADOR "(" <dimensiones> ")" "=" "[" <vectores> "]" ";"
                            | "VECTOR" "[" <tipo> "]" IDENTIFICADOR "(" <dimensiones> ")" "=" "[" <expresiones> "]" ";"

        <vector_sin_valor> ::= "VECTOR" "[" <tipo> "]" IDENTIFICADOR "(" <dimensiones> ")" ";"

        <vector_sort> ::= "VECTOR" "[" <tipo> "]" IDENTIFICADOR "(" <dimensiones> ")" "=" <sort> ";"

        <vector_shuffle> ::= "VECTOR" "[" <tipo> "]" IDENTIFICADOR "(" <dimensiones> ")" "=" <shuffle> ";"

        <dimensiones> ::= <dimensiones> "," <dimension>
                        | <dimension>

        <dimension> ::= ENTERO

        <vectores> ::= <vectores> "," <vector>
                    | <vector>

        <vector> ::= "[" <expresiones> "]"
                | "[" <vectores> "]"

        <asignacion_vector> ::= IDENTIFICADOR <indices> "=" <expresion> ";"

        <indices> ::= <indices> <indice>
                | <indice>

        <indice> ::= "[" <expresion> "]"

        <acceso_vector> ::= IDENTIFICADOR <indices>

        <sort> ::= "SORT" "(" IDENTIFICADOR ")"
        <shuffle> ::= "SHUFFLE" "(" IDENTIFICADOR ")"
```
🔷 4. SENTENCIA IF
```HTML
    <sentencia_if> ::= "IF" "(" <condicion> ")" "{" <sentencias> "}"
                    | "IF" "(" <condicion> ")" "{" <sentencias> "}" "ELSE" "{" <sentencias> "}"
                    | "IF" "(" <condicion> ")" "{" <sentencias> "}" "ELSE" <sentencia_if>

    <condicion> ::= <relacional>
                | <logica>
```
🔷 5. BUCLES
```HTML
    <sentencia_while> ::= "WHILE" "(" <condicion> ")" "{" <sentencias> "}"

    <sentencia_do_while> ::= "DO" "{" <sentencias> "}" "WHILE" "(" <condicion> ")"

    <sentencia_for> ::= "FOR" "(" <inicio_for> ";" <condicion> ";" <actualizacion> ")" "{" <sentencias> "}"

    <inicio_for> ::= <asignacion>
                | <declaracion_valor>

    <actualizacion> ::= IDENTIFICADOR "++"
                    | IDENTIFICADOR "--"
                    | IDENTIFICADOR "=" <expresion>
```
🔷 6. SWTICH
```HTML
    <switch> ::= "SWITCH" "(" <expresion> ")" "{" <cases> "}"

    <cases> ::= <cases> <case>
            | <case>

    <case> ::= "CASE" <expresion> ":" <sentencias> "BREAK" ";"
            | "DEFAULT" ":" <sentencias> "BREAK" ";"
```
🔷 7. PROCEDIMEINTO Y LLAMDAS
```HTML
    <proc> ::= "PROC" IDENTIFICADOR "(" <params> ")" "{" <sentencias> "}"

    <params> ::= <params> "," <param>
            | <param>
            | ε

    <param> ::= <tipo> ":" IDENTIFICADOR

    <exec> ::= "EXEC" IDENTIFICADOR "(" <args> ")" ";"

    <args> ::= <args> "," <arg>
            | <arg>
            | ε

    <arg> ::= IDENTIFICADOR
        | ENTERO
        | FLOTANTE
        | "TRUE"
        | "FALSE"
        | CADENA
        | CARACTER
        | <acceso_vector>
```

## 🌳 Construcción del AST 

📌 El **Árbol de Sintaxis Abstracta (AST)** es una representación estructurada del programa en forma de árbol.

Cada nodo del AST representa una construcción del lenguaje (por ejemplo: una asignación, una operación aritmética, un número, etc.).

El AST es **más simple que el árbol sintáctico completo**, ya que omite tokens redundantes y conserva únicamente la estructura semántica del programa.

---

### 📌 Implementación del AST

La construcción del AST se realiza en el archivo `ast.py`.

Se define una clase `ASTNode` que representa cada nodo del árbol.

---

#### Clase ASTNode

```python
# Nodo.py

class Nodo:
    #ESTE CLASE ES LA BASE PARA TODOS LOS NODOS DEL AST
    def __init__(self, tipo=None, linea=None, columna=None):
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
    
    #PROPORCIONA EL MÉTODO ACCEPT(self, visitor) QUE PERMITE A LOS VISITANTES RECORRER EL AST
    #BASICAMENTE, EL accept RECIBE LA VISITA DEL OBJETO visitor
    def accept(self, visitor):
        metodo_visitor = 'visit_' + self.__class__.__name__
        visitar = getattr(visitor, metodo_visitor, None)
        if visitar is None:
            visita = visitor.default_visit
            raise Exception(f"El visitante no tiene un método para visitar {self.__class__.__name__}")
        return visitar(self)
```
### Generar el AST:
Ejemplo de como genera un AST de una suma
```python

class VisitorGraph(Visitor):
    def __init__(self, Arbol):
        self.Arbol = Arbol
        self.dot = []
        self.counter = 0
        self.dot.append('digraph G {')
        self.dot.append('\tnode [shape=ellipse];')
        self.dot.append('\tordering="out";')
        self.dot.append('\tcompound=true;')
        self.dot.append('\tnodoRaiz [label="Programa"];')
        self.dot.append('\tnodoSentencias [label="Sentencias"];')
        self.dot.append('\tnodoRaiz -> nodoSentencias;')  # Conectar el nodo raíz al primer nodo

    def generar_dot(self, arbol):
        self.dot.append("}")
        return "\n".join(self.dot)
    
    def appendInstruccion(self, instruccion):
        self.dot.append(f'\tnodoSentencias -> {instruccion};')
        self.counter += 1
    # VISITA UN NÚMERO Y DEVUELVE SU VALOR
    def visit_Nativo(self, nodo: Nodo):
        #DEFINO EL NODO
        codigo = f'\tnode{self.counter} [label="{nodo.valor}"];'
        self.dot.append(codigo)

        #RETORNO EL NOMBRE DEL NODO
        retorno = f'node{self.counter}'
        self.counter += 1
        return retorno

    def visit_Suma(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DE LA SUMA
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="+"];')
        
        #SE RETORNA EL CÓDIGO DE LA SUMA
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
```

## Generación de Reportes
Una vez que el backend ha terminado de analizar el código fuente (léxico, sintáctico, semántico).

---

### Tipos de reportes generados

| Reporte                    | Archivo generado                    |
|----------------------------|-------------------------------------|
| Reporte de errores         | `/reports/errores.json`              |
| Tabla de símbolos          | `/reports/symbols.json`              |
| AST                        | `/reports/ast.json`                  |
| Memoria                    | `/reports/memory.json`               |
| Advertencias               | `/reports/warnings.json`             |

---

### Ejemplo de generación de un reporte en el backend

#### Reporte de errores

```python
# reporteErrores.py
def generar_reporteErrores():
    """
    Crear reporte html de errores
    """
    with open(errores_html_path, 'w') as file:
        file.write('''<html>
            <head>
                <title>Reporte de Errores</title>
                <style>
                    body {
                        font-family: 'Segoe UI', Arial, sans-serif;
                        background: #f7f9fb;
                        color: #222;
                        margin: 0;
                        padding: 0;
                    }
                    h1 {
                        text-align: center;
                        margin-top: 40px;
                        color: #2d6cdf;
                        letter-spacing: 1px;
                    }
                    table {
                        margin: 40px auto;
                        border-collapse: collapse;
                        width: 80%;
                        background: #fff;
                        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
                        border-radius: 8px;
                        overflow: hidden;
                    }
                    th, td {
                        padding: 14px 18px;
                        text-align: left;
                    }
                    th {
                        background: #2d6cdf;
                        color: #fff;
                        font-weight: 600;
                        border-bottom: 2px solid #e3eaf2;
                    }
                    tr:nth-child(even) {
                        background: #f1f6fb;
                    }
                    tr:hover {
                        background: #eaf1fb;
                    }
                    td {
                        border-bottom: 1px solid #e3eaf2;
                    }
                    .no-errores {
                        text-align: center;
                        color: #888;
                        font-style: italic;
                    }
                </style>
            </head>
            <body>
            '''
        )

        file.write('<h1>Reporte de Errores</h1>')
        file.write('<table><tr><th>Tipo</th><th>Descripción</th><th>Fila</th><th>Columna</th></tr>')
        
        # Valida si hay errores antes de generar el reporte
        if not errores:
            file.write('<tr><td class="no-errores" colspan="4">No hay errores registrados.</td></tr>')
            file.write('</table></body></html>')
        
        else:
            for error in errores:
                file.write(f'<tr><td>{error.tipo}</td><td>{error.descripcion}</td><td>{error.linea}</td><td>{error.columna}</td></tr>')
        
        file.write('</table></body></html>')
    return send_file(errores_html_path, mimetype='text/html')
```
### Reporte de Tabla de Símbolos
```py
#reporteTS
def generar_reporteTS():
    """
    Crear reporte html de la tabla de simbolos
    """
    css = """
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f7fafc;
            color: #22223b;
            margin: 0;
            padding: 0;
        }
        h1 {
            text-align: center;
            color: #3a5a40;
            margin-top: 32px;
            margin-bottom: 24px;
        }
        table {
            margin: 0 auto 40px auto;
            border-collapse: collapse;
            width: 90%;
            background: #fff;
            box-shadow: 0 2px 8px rgba(58, 90, 64, 0.08);
            border-radius: 8px;
            overflow: hidden;
        }
        th, td {
            padding: 12px 16px;
            text-align: left;
        }
        th {
            background: #a3b18a;
            color: #fff;
            font-weight: 600;
            border-bottom: 2px solid #588157;
        }
        tr:nth-child(even) {
            background: #f0efeb;
        }
        tr:nth-child(odd) {
            background: #fff;
        }
        tr:hover {
            background: #d8f3dc;
        }
        td {
            border-bottom: 1px solid #e9ecef;
        }
    </style>
    """

    with open(st_html_path, 'w') as file:
        file.write('<html><head><title>Reporte de Tabla de Símbolos</title>')
        file.write(css)
        file.write('</head><body>')

        file.write('<h1>Reporte de Tabla de Símbolos</h1>')
        file.write('<table border="0"><tr><th>Nombre</th><th>Tipo de Entidad</th><th>Tipo de Dato</th><th>Valor</th><th>Alcance</th><th>Fila</th><th>Columna</th></tr>')

        # Valida si hay simbolos antes de generar el reporte
        if not st.symbols:
            file.write('<tr><td colspan="7">No hay símbolos en la tabla.</td></tr>')
            file.write('</table></body></html>')
        
        else:
            # Si hay símbolos, se procede a generar el reporte
            for simbolo in st.symbols:
                file.write(f'<tr><td>{simbolo.name}</td><td>{simbolo.entity_type}</td><td>{simbolo.data_type}</td>')
                file.write(f'<td>{simbolo.value}</td><td>{simbolo.scope}</td><td>{simbolo.line}</td><td>{simbolo.column}</td></tr>')

        file.write('</table></body></html>')
    return send_file(st_html_path, mimetype='text/html')
```
### Reporte AST

```py
def reporte_ast():
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({'error': 'No input provided'}), 400

    input = data['input']

    try:
        instrucciones = parse(input['code'])
        ast = Arbol(instrucciones)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    visitor_gv = VisitorGraph(ast)
    # SE IMPRIME EL AST
    if ast.getInstrucciones() is None:
        print("El AST no contiene instrucciones.")
        return jsonify({'error': 'El AST no contiene instrucciones.'}), 500
    try:
        for nodo in ast.getInstrucciones():
            if nodo is None:
                print("Nodo es None, se ignora.")
                continue  # Ignora nodos None explícitamente
            try:
                codigo = nodo.accept(visitor_gv)
                visitor_gv.appendInstruccion(codigo)
            except TypeError as e:
                if "NoneType" in str(e):
                    continue  # Ignora y sigue con el siguiente nodo
                else:
                    raise  # Si es otro TypeError, relanza la excepción
    except Exception as e:
        print(f"Error al graficar el AST: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al visitar el AST'}), 500
    dot_ast = visitor_gv.generar_dot(ast)

    # Ruta absoluta a la carpeta backend/public
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend
    public_dir = os.path.join(base_dir, "public", "ast")
    os.makedirs(public_dir, exist_ok=True)

    dot_path = os.path.join(public_dir, "ast.dot")
    svg_path = os.path.join(public_dir, "ast.svg")

    # Guardar DOT en public/ast
    with open(dot_path, "w", encoding="utf-8") as f:
        f.write(dot_ast)

    # Generar SVG en public/ast
    src_graph = Source(dot_ast)
    src_graph.render(filename="ast", directory=public_dir, format='svg', cleanup=True)

    # Devuelve el archivo SVG
    return send_file(svg_path, mimetype='image/svg+xml', as_attachment=True, download_name='ast.svg')
```
### Reporte de Memoria
```py
def generar_reporteMemoria():

    #Limpiar la lista de errores antes de cada petición
    errores.clear()
    #Limpia la tabla de simbolos antes de cada petición
    global st
    st.clear()

    ast = None
    data = None
    instrucciones = None

    # Accede al contenido JSON enviado por el frontend
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({'error': 'No hay contenido para interpretar'}), 400

    input = data['input']

    # SE OBTIENE EL AST CREADO POR EL PARSER
    try:
        instrucciones = parse(input['code'])
        ast = Arbol(instrucciones)
    except Exception as e:
        print(f"Error al crear el árbol")
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al crear el AST durante el reporte de memoria'}), 500

    if ast is None: 
        print("Hubo un error al parsear la expresión durante el reporte de memoria.")
        return jsonify({'error': 'Error al parsear la expresión durante el reporte de memoria.'}), 500

    print("AST generado correctamente.")
    visitor = Visitor_Output(ast)

    # SE IMPRIME EL AST
    if ast.getInstrucciones() is None:
        print("El AST no contiene instrucciones.")
        return jsonify({'error': 'El AST no contiene instrucciones para el reporte de memoria.'}), 500
    try:
        for nodo in ast.getInstrucciones():
            try:
                nodo.accept(visitor)
            except TypeError as e:
                if "NoneType" in str(e):
                    continue  # Ignora y sigue con el siguiente nodo
                else:
                    raise  # Si es otro TypeError, relanza la excepción
    except Exception as e:
        print(f"Error al visitar el AST: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al visitar el AST'}), 500

    try:
        # CSS PARA EL REPORTE HTML
        css = """
<style>
    body {
        font-family: 'Arial', sans-serif;
        max-width: 1000px; /* Aumentado para acomodar tabla más ancha */
        margin: 0 auto;
        padding: 20px;
        background-color: #FFFCF8;
        color: #5A4A3A;
        line-height: 1.6;
    }
    h1 {
        text-align: center;
        margin-bottom: 30px;
        color: #D47D36;
        font-weight: 400;
        letter-spacing: 0.5px;
    }
    table {
        width: 105%; /* Tabla más ancha que el contenedor */
        margin-left: -2.5%; /* Compensa el aumento de ancho */
        border-collapse: collapse;
        margin-bottom: 30px;
        border: 1px solid #F0E6DC;
    }
    th, td {
        border: 1px solid #F0E6DC;
        padding: 12px 15px;
        text-align: left;
    }
    th {
        background-color: #FDF2E5;
        color: #D47D36;
        font-weight: 500;
    }
    tr:nth-child(even) {
        background-color: #FFF9F3;
    }
    tr:hover {
        background-color: #FDF2E5;
    }
    .execution-container {
        margin-top: 30px;
    }
    .execution-title {
        text-align: left;
        margin-bottom: 20px;
        color: #D47D36;
        font-weight: 400;
    }
    .content-row {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        padding: 0 20px;
        margin-bottom: 25px;
        position: relative; /* Para posicionar la flecha */
    }
    .stack-container {
        width: 240px;
        margin-right: 20px;
    }
    .stack-title {
        font-weight: 500;
        margin-bottom: 15px;
        font-size: 1em;
        color: #D47D36;
        padding-left: 2px;
        letter-spacing: 0.3px;
    }
    .stack {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    .stack-item {
        border: 1px solid #F0D9C5;
        padding: 12px 15px;
        background-color: #FFF9F3;
        text-align: center;
        border-radius: 3px;
        color: #5A4A3A;
        font-size: 0.95em;
        transition: all 0.15s ease;
    }
    .stack-item:hover {
        background-color: #FDF2E5;
        border-color: #E8C7A8;
    }
    .symbols-container {
        width: 380px;
        margin-left: 20px;
    }
    .symbols-title {
        font-weight: 500;
        margin-bottom: 15px;
        font-size: 1em;
        color: #D47D36;
        padding-left: 2px;
        visibility: hidden;
    }
    .symbols-table {
        width: 100%;
        border: 1px solid #F0E6DC;
    }
    .symbols-table th {
        background-color: #FDF2E5;
        color: #D47D36;
        font-weight: 500;
    }
    h2 {
        color: #D47D36;
        border-bottom: 1px solid #F0D9C5;
        padding-bottom: 5px;
        font-weight: 400;
        margin-top: 40px;
    }
    
    /* Flecha entre la pila y la tabla */
    .arrow-connector {
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        color: #D47D36;
        font-size: 90px;
        width: 200px;
    }
</style>
            """
        with open(memoria_html_path, 'w') as file:
            file.write('<html><head><title>Reporte de memoria</title>')
            file.write(css)
            file.write('</head><body>')
            file.write('<h1>Reporte de memoria</h1>')
            file.write('<h1>Procedimientos</h1>')

            #FOR PRINCIPAL QUE RECORRE CADA PROCEDIMIENTO EN EL AST
            for idx, nodo in enumerate(ast.getInstrucciones()):
                if not isinstance(nodo, Procedimiento):
                    continue  # Ignora nodos que no son Procedimiento o Execute
                if isinstance(nodo, Procedimiento):
                    try:
                        file.write('<table><thead><tr><th>Nombre</th><th>Atributos</th><th>No. de llamadas</th><th>Líneas de llamada</th></tr></thead>')
                        #TABLA QUE DEFINE EL PROCEDIMIENTO
                        tabla = f'''<tbody>
                                <tr>
                                    <td>{nodo.id}</td>
                                    <td>{', '.join([f"{param.id}: {param.tipo}" for param in nodo.parametros])}</td>
                                    
                                    <td>{str(len(nodo.lineas_llamada))}</td>
                                    <td>{', '.join([str(linea) for linea in nodo.lineas_llamada])}</td>
                                </tr>
                            </tbody>
                        </table>'''
                        file.write(tabla)
                        #EJECUCIONES DEL PROCEDIMIENTO
                        ejecuciones = f'''<div class="execution-container">
                                <h2 class="execution-title">Ejecuciones</h2>'''
                        file.write(ejecuciones)
                        
                        #LISTA PARA SABER DONDE RETORNA EL PROCEDIMIENTO
                        retornos = []
                        for idx_exec, instruccion in enumerate(ast.getInstrucciones()):
                            if isinstance(instruccion, Execute) and instruccion.identificador == nodo.id:
                                retornos.append(idx_exec)

                        # SE RECORRE CADA EXECUTE DEL PROCEDIMIENTO
                        for i, linea in enumerate(nodo.lineas_llamada):
                            #SE CREA LA PILA
                            ejecucion = f'<div class="content-row"><div class="stack-container"><div class="stack-title">Línea {linea}</div>'
                            # Obtener los ids de las declaraciones dentro del procedimiento
                            declaracion_ids = [
                                instr.id for instr in getattr(nodo, 'instrucciones', [])
                                if instr.__class__.__name__ == 'Declaracion'
                            ]
                            ejecucion += f'''<div class="stack">
                                    <div class="stack-item"><b style="font-size:1.2em;">Parámetros</b><br><br>{', '.join([f"{param.id}" for param in nodo.parametros])}</div>'''
                            if declaracion_ids:
                                ejecucion += f'''<div class="stack-item"><b style="font-size:1.1em;">Variables locales</b><br><br>{', '.join(declaracion_ids)}</div>'''
                            ejecucion += f'''<div class="stack-item">{nodo.id}()</div>'''
                            # Validar que el índice no esté fuera de rango
                            idx_retorno = retornos[i] + 1 if i < len(retornos) and retornos[i] + 1 < len(ast.getInstrucciones()) else None
                            if idx_retorno is not None:
                                linea_retorno = getattr(ast.getInstrucciones()[idx_retorno], 'linea', 'N/A')
                                classname = ast.getInstrucciones()[idx_retorno].__class__.__name__
                                ejecucion += f'<div class="stack-item">Retorno en linea {linea_retorno} {classname}</div>'
                            else:
                                ejecucion += f'<div class="stack-item">Retorno fin de programa</div>'
                            ejecucion += '</div></div>'
                            file.write(ejecucion)
                            # Obtener todas las instrucciones de tipo Execute para este procedimiento
                            executes = [
                                instr for instr in ast.getInstrucciones()
                                if isinstance(instr, Execute) and instr.identificador == nodo.id
                            ]
                            # Para la ejecución actual (índice i), obtener el ID correspondiente
                            if i < len(executes):
                                execute_actual = executes[i]
                                id_ejecucion = execute_actual.id
                                
                                # Obtener todos los símbolos del procedimiento
                                simbolos_proc = st.get_scope_proc(nodo.id)

                                # Filtrar símbolos cuyo scope termine con el ID de la ejecución actual
                                simbolos_filtrados = [
                                    s for s in simbolos_proc 
                                    if s.scope.endswith(f"_{id_ejecucion}")
                                ]
                            else:
                                simbolos_filtrados = []
                            
                            # Construir la tabla de símbolos
                            tabla_simbolos = f'''<div class="arrow-connector">→</div><div class="symbols-container">
                                <div class="symbols-title">Tabla de Símbolos</div>
                                    <table class="symbols-table">
                                        <thead>
                                            <tr>
                                                <th>Variable</th>
                                                <th>Valor</th>
                                                <th>Tipo</th>
                                            </tr>
                                        </thead>
                                        <tbody>'''
                            
                            # Agregar cada símbolo a la tabla
                            for simbolo in simbolos_filtrados:
                                tabla_simbolos += f'''
                                            <tr>
                                                <td>{simbolo.name}</td>
                                                <td>{simbolo.value}</td>
                                                <td>{simbolo.data_type}</td>
                                            </tr>'''
                            
                            # Si no hay símbolos, mostrar un mensaje o dejar vacío
                            if not simbolos_filtrados:
                                tabla_simbolos += f'''
                                            <tr>
                                                <td colspan="3">No hay símbolos para esta ejecución</td>
                                            </tr>'''
                            
                            # Cerrar la tabla
                            tabla_simbolos += '''
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            </div>'''
                            
                            file.write(tabla_simbolos)
                    except Exception as e:
                        print(f"Error al procesar el nodo {nodo}: {str(e)}")
                continue
            file.write('''</body></html>''')
        return send_file(memoria_html_path, mimetype='text/html')

    except Exception as e:
        print(f"Error al generar el reporte de memoria: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al generar el reporte de memoria.'}), 500

    # Devuelve el archivo html



    # for simbolo in st.symbols:
    #     print(f"Procesando símbolo")

    # with open(memoria_html_path, 'w') as file:
    #     file.write('<html><head><title>Reporte de memoria</title>')
    #     file.write(css)
    #     file.write('</head><body>')

    #     file.write('<h1>Reporte de memoria</h1>')
    #     file.write('<h1>Procedimientos</h1>')


    #     # Valida si hay simbolos antes de generar el reporte
    #     if not st.symbols:
    #         file.write('<tr><td colspan="7">No hay símbolos en la tabla.</td></tr>')
    #         file.write('</table></body></html>')
        
    #     else:
    #         # Si hay símbolos, se procede a generar el reporte
    #         for simbolo in st.symbols:
    #             file.write(f'<tr><td>{simbolo.name}</td><td>{simbolo.entity_type}</td><td>{simbolo.data_type}</td>')
    #             file.write(f'<td>{simbolo.value}</td><td>{simbolo.scope}</td><td>{simbolo.line}</td><td>{simbolo.column}</td></tr>')

    #     file.write('</table></body></html>')
    # return send_file(memoria_html_path, mimetype='text/html')
```
### Reporte de Advertencias
```py
def generar_reporteAdvertencias():

    #Limpiar la lista de errores antes de cada petición
    errores.clear()
    #Limpia la tabla de simbolos antes de cada petición
    global st
    st.clear()

    ast = None
    data = None
    instrucciones = None

    # Accede al contenido JSON enviado por el frontend
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({'error': 'No hay contenido para interpretar'}), 400

    input = data['input']

    # SE OBTIENE EL AST CREADO POR EL PARSER
    try:
        instrucciones = parse(input['code'])
        ast = Arbol(instrucciones)
    except Exception as e:
        print(f"Error al crear el árbol")
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al crear el AST durante el reporte de advertencias'}), 500

    if ast is None: 
        print("Hubo un error al parsear la expresión durante el reporte de advertencias.")
        return jsonify({'error': 'Error al parsear la expresión durante el reporte de advertencias.'}), 500

    print("AST generado correctamente.")
    visitor = Visitor_Output(ast)

    # SE IMPRIME EL AST
    if ast.getInstrucciones() is None:
        print("El AST no contiene instrucciones.")
        return jsonify({'error': 'El AST no contiene instrucciones para el reporte de advertencias.'}), 500
    try:
        for nodo in ast.getInstrucciones():
            try:
                nodo.accept(visitor)
            except TypeError as e:
                if "NoneType" in str(e):
                    continue  # Ignora y sigue con el siguiente nodo
                else:
                    raise  # Si es otro TypeError, relanza la excepción
    except Exception as e:
        print(f"Error al visitar el AST: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al visitar el AST'}), 500

    try:
        # CSS PARA EL REPORTE HTML
        css = """
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: #f7fafc;
                    color: #22223b;
                    margin: 0;
                    padding: 0;
                }
                h1 {
                    text-align: center;
                    color: #3a5a40;
                    margin-top: 32px;
                    margin-bottom: 24px;
                }
                table {
                    margin: 0 auto 40px auto;
                    border-collapse: collapse;
                    width: 90%;
                    background: #fff;
                    box-shadow: 0 2px 8px rgba(58, 90, 64, 0.08);
                    border-radius: 8px;
                    overflow: hidden;
                }
                th, td {
                    padding: 12px 16px;
                    text-align: left;
                }
                th {
                    background: #a3b18a;
                    color: #fff;
                    font-weight: 600;
                    border-bottom: 2px solid #588157;
                }
                tr:nth-child(even) {
                    background: #f0efeb;
                }
                tr:nth-child(odd) {
                    background: #fff;
                }
                tr:hover {
                    background: #d8f3dc;
                }
                td {
                    border-bottom: 1px solid #e9ecef;
                }
            </style>"""
        with open(advertencias_html_path, 'w') as file:
            file.write('<html><head><title>Reporte de Tabla de Advertencias</title>')
            file.write(css)
            file.write('</head><body>')

            file.write('<h1>Reporte de Tabla de Advertencias</h1>')
            file.write('<table border="0"><tr><th>Procedimiento</th><th>Mensaje</th><th>Linea</th><th>Columna</th>')

            # Valida si hay advertencias antes de generar el reporte
            if not any(adv for adv in ast.getAdvertencias()):
                file.write('<tr><td colspan="7">No hay advertencias en la tabla.</td></tr>')
                file.write('</table></body></html>')
            
            else:
                # Si hay advertencias, se procede a generar el reporte
                for adv in ast.getAdvertencias():
                    file.write(f'<tr><td>{adv.procedimiento}</td><td>{adv.mensaje}</td><td>{adv.linea}</td><td>{adv.columna}</td></tr>')

            file.write('</table></body></html>')
        
        return send_file(advertencias_html_path, mimetype='text/html')

    except Exception as e:
        print(f"Error al generar el reporte de advertencias: {str(e)}")
        return jsonify({'error': 'Ocurrió un error al generar el reporte de advertencias.'}), 500
```
## 📒Librerías y Dependencias

El proyecto utiliza un conjunto de herramientas modernas para su desarrollo, divididas en dos partes:

 **Frontend** → construido en React + Vite  
 **Backend** → construido en Python 3.x + Flask + PLY

A continuación se describen las principales dependencias utilizadas en cada módulo:

---

### Frontend

Ubicado en la carpeta `/frontend/`.

#### Principales librerías:

| Librería             | Uso principal                           |
|----------------------|-----------------------------------------|
| React                | Framework para construir la UI           |
| Vite                 | Empaquetador y servidor de desarrollo    |
| Axios o fetch        | Comunicación HTTP con el backend         |
| React CodeMirror     | (opcional) editor enriquecido de código  |

#### Ejemplo de `package.json` (fragmento):

```json
{
  "name": "frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "axios": "^1.9.0",
    "react": "^19.1.0",
    "react-dom": "^19.1.0",
    "react-router-dom": "^7.6.2",
    "sweetalert2": "^11.22.0"
  },
  "devDependencies": {
    "@eslint/js": "^9.25.0",
    "@types/react": "^19.1.2",
    "@types/react-dom": "^19.1.2",
    "@vitejs/plugin-react": "^4.4.1",
    "eslint": "^9.25.0",
    "eslint-plugin-react-hooks": "^5.2.0",
    "eslint-plugin-react-refresh": "^0.4.19",
    "globals": "^16.0.0",
    "vite": "^6.3.5"
  }
}

```
###  Backend 

Ubicado en la carpeta `/backend/`, el backend requiere las siguientes dependencias, definidas en `requirements.txt`.

#### Principales librerías utilizadas:

| Librería     | Versión sugerida | Función principal                                                |
|--------------|------------------|------------------------------------------------------------------|
| `Flask`      | 2.x               | Servidor web y creación de API REST                             |
| `PLY`        | 3.x               | Análisis léxico y sintáctico (Python Lex-Yacc)                  |
| `graphviz`   | Opcional          | Visualización del AST (si se genera el DOT desde Python)        |
| `json`       | Incluida en Python| Formato de salida para reportes                                 |
| `os`, `io`   | Incluidas         | Manejo de archivos y consola                                    |

#### Comandos útiles de desarrollo
```bash
npm install           # Instala dependencias
npm run dev           # Corre el servidor
```
```bash
 install -r requirements.txt
python app.py         # Ejecuta el backend en localhost:5000
```