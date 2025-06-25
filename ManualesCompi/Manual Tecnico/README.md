# Manual Técnico  
## Proyecto - Lenguaje OBJ-C  
**Curso:** Organización de Lenguajes y Compiladores 1  
**Sección P**  
**Universidad de San Carlos de Guatemala**    

**Integrantes:**  
- Eduardo Sebastián Gutiérrez de Felipe 
- Carlos Eduardo Lau López
- Sebastián Antonio Romero Tzitizmit
- Christian David Chinchilla Santos

---

## Índice

1. [Introducción](#introducción)  
2. [Arquitectura del Sistema](#arquitectura-del-sistema)   
3. [Frontend](#frontend)    
    1. [Componentes y funcionalidades](#componentes-y-funcionalidades)  
    2. [Comunicación con el Backend](#comunicación-con-el-backend)  
4. [Backend](#backend)   
    1. [Explicación de los analizadores (léxico y sintáctico)](#explicación-de-los-analizadores-léxico-y-sintáctico)  
    2. [Construcción del AST](#construcción-del-ast)  
    3. [Generación de reportes](#generación-de-reportes)  
5. [Librerías y Dependencias](#librerías-y-dependencias)  

---
## Introducción

El presente Manual Técnico documenta el diseño, desarrollo e implementación del **Proyecto Fase I y Fase II - Lenguaje OBJ-C**, elaborado como parte del curso **Organización de Lenguajes y Compiladores 1**, Sección P, de la Facultad de Ingeniería de la Universidad de San Carlos de Guatemala.

El objetivo del proyecto es la creación de un compilador parcial para el lenguaje OBJ-C, un lenguaje propio definido en el enunciado del proyecto, el cual permite realizar análisis léxico, sintáctico, construcción de Árbol de Sintaxis Abstracta (AST), generación de reportes (errores, tabla de símbolos, memoria) y visualización interactiva del proceso de compilación.

El sistema está compuesto por dos módulos principales:

- **Frontend**: una interfaz gráfica amigable, desarrollada con **React + Vite**, que permite a los usuarios escribir, cargar e interpretar código en OBJ-C, así como visualizar los reportes generados por el backend.
- **Backend**: un servidor en **Python** que utiliza la librería **PLY (Python Lex-Yacc)** para realizar el análisis léxico y sintáctico del código fuente, validar semántica, construir el AST y generar los reportes necesarios. El backend expone una API REST que es consumida por el frontend.

Este manual técnico describe en detalle la arquitectura de la solución, la estructura de los componentes, la implementación del compilador parcial, el flujo de ejecución y las consideraciones técnicas que permitirán comprender y mantener el sistema a futuro.

El documento está dirigido a desarrolladores que deseen comprender el funcionamiento interno del compilador OBJ-C, a tutores académicos y al catedrático del curso.

---

## Arquitectura del Sistema

El sistema del compilador parcial para el lenguaje OBJ-C ha sido diseñado bajo una arquitectura **cliente-servidor**, que separa claramente las responsabilidades entre la interfaz de usuario (frontend) y el procesamiento del código (backend).

### Componentes principales

1. **Frontend**  
    - Implementado con **React** y el framework de desarrollo rápido **Vite**.  
    - Proporciona la interfaz gráfica para que el usuario pueda:  
        - Escribir o cargar archivos de código fuente `.objc`.  
        - Enviar el código al backend para ser interpretado.  
        - Visualizar la salida de la interpretación.  
        - Consultar los reportes generados: reporte de errores, tabla de símbolos, AST, memoria, advertencias.

2. **Backend**  
    - Implementado en **Python**.  
    - Utiliza la librería **PLY (Python Lex-Yacc)** para realizar el análisis léxico y sintáctico del código OBJ-C.  
    - Expone una **API REST** desarrollada con **Flask**, que permite al frontend enviar código y recibir resultados en formato JSON.  
    - Realiza las siguientes tareas:  
        - Tokenización (análisis léxico)  
        - Parsing (análisis sintáctico)  
        - Validación semántica  
        - Construcción del Árbol de Sintaxis Abstracta (AST)  
        - Generación de reportes (errores, símbolos, memoria, advertencias)

### Flujo de datos

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

## Frontend

El frontend de la aplicación fue desarrollado utilizando **React**, junto con el framework de desarrollo rápido **Vite**, que permite tiempos de carga reducidos y una configuración optimizada para proyectos modernos de JavaScript.

El objetivo del frontend es proporcionar una interfaz gráfica amigable que permita al usuario:

- Escribir o cargar código fuente en el lenguaje OBJ-C.
- Interpretar el código.
- Visualizar la salida de la ejecución.
- Consultar los reportes generados por el backend (errores, AST, tabla de símbolos, memoria, advertencias).

---
### Componentes y funcionalidades

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
const handleCargarArchivo = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = (e) => {
        setCodigo(e.target.result);  //codigo cargado
    };

    if (file) {
        reader.readAsText(file);
    }
};
```
#### *Interpretar Codigo*
``` jsx
const handleInterpretar = async () => {
    try {
        const response = await fetch("http://localhost:5000/interpret", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: codigo }),
        });

        const data = await response.json();
        setSalidaConsola(data.salida);
        setErrores(data.errores);

    } catch (error) {
        console.error("Error al interpretar el código:", error);
    }
};
```

### Comunicación con el Backend

La comunicación entre el **frontend** y el **backend** se realiza mediante peticiones HTTP bajo el patrón **API REST**.

El backend, implementado en Python con Flask, expone los siguientes endpoints principales:

| Endpoint             | Método | Descripción                                 |
|----------------------|--------|---------------------------------------------|
| `/interpret`         | POST   | Recibe el código fuente, lo analiza y devuelve el resultado (salida, errores, AST) |
| `/getErrors`         | GET    | Devuelve el reporte de errores |
| `/getSymbols`        | GET    | Devuelve la tabla de símbolos |
| `/getAST`            | GET    | Devuelve el AST generado |
| `/getMemory`         | GET    | Devuelve el reporte de memoria |
| `/getWarnings`       | GET    | Devuelve las advertencias |

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

En el archivo `/src/services/apiService.js` se define la función:

```js
// apiService.js

export async function interpretarCodigo(codigoFuente) {
    const response = await fetch("http://localhost:5000/interpret", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: codigoFuente }),
    });

    const data = await response.json();
    return data;  //contiene salida, errores, estado
}
```
## Backend

El backend de la aplicación fue desarrollado en **Python 3.x**.  
Su objetivo principal es procesar el código fuente escrito en el lenguaje OBJ-C mediante las siguientes fases:

- Análisis léxico
- Análisis sintáctico
- Construcción del Árbol de Sintaxis Abstracta (AST)
- Validación semántica
- Generación de reportes
- Exposición de una API REST que consume el frontend

El backend utiliza las siguientes tecnologías principales:

- **PLY (Python Lex-Yacc)**: librería que permite definir analizadores léxicos y sintácticos.
- **Flask**: framework ligero para exponer una API REST.

---

## Explicación de los analizadores (léxico y sintáctico)

El backend del proyecto implementa dos analizadores principales:

1. **Analizador Léxico** → definido en `lexer.py`  
2. **Analizador Sintáctico** → definido en `parser.py`

Ambos trabajan en conjunto para procesar el código OBJ-C que escribe el usuario.

---

### Analizador Léxico (lexer.py)

El **analizador léxico** transforma el código fuente en una **secuencia de tokens**.  
Cada token corresponde a una palabra clave, símbolo, número o identificador válido en el lenguaje OBJ-C.

Se implementa usando **PLY (Python Lex)**, que permite definir tokens con expresiones regulares.

---

#### Definición de tokens

```python
# lexer.py

# Lista de tokens válidos
tokens = [
    'ID',           # Identificadores
    'INT',          # Números enteros
    'FLOAT',        # Números decimales
    'STRING',       # Cadenas de texto
    'PLUS',         # +
    'MINUS',        # -
    'TIMES',        # *
    'DIVIDE',       # /
    'EQUALS',       # =
    'LPAREN',       # (
    'RPAREN',       # )
    'SEMICOLON',    # ;
    'LBRACE',       # {
    'RBRACE',       # }
]
```
---
# Operadores
```
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
```
---
# Delimitadores
```
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
```
---
# Tokens con funciones
```python
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t
```
---
# Manejo de errores léxicos
```python
def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)
```
---
# Analizador Sintáctico (parser.py)

El **analizador sintáctico** recibe la secuencia de tokens producida por el lexer y verifica que la estructura del código cumpla con la gramática definida para el lenguaje OBJ-C.

El parser está implementado en el archivo `parser.py` usando la librería **PLY (Python Yacc)**.

Además de validar la sintaxis, el parser construye el **Árbol de Sintaxis Abstracta (AST)** que representa la estructura del programa.

---

#### Estructura del parser

```python
import ply.yacc as yacc
from lexer import tokens
from ast import ASTNode

# Asociación de precedencias (opcional)
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)
```

### Ejemplo: asignación de variable
```python
def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = ASTNode('PLUS', None, [p[1], p[3]])

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = ASTNode('MINUS', None, [p[1], p[3]])

def p_expression_times(p):
    'expression : expression TIMES expression'
    p[0] = ASTNode('TIMES', None, [p[1], p[3]])
```
### Ejemplo: expresión numérica
```python
def p_expression_number(p):
    'expression : INT'
    p[0] = ASTNode('INT', p[1], [])
```
### Manejo de errores Sintacticos
```python
def p_error(p):
    if p:
        print(f"Syntax error at token {p.type} ({p.value}) on line {p.lineno}")
    else:
        print("Syntax error at EOF")
```
---
## Construcción del AST 

El **Árbol de Sintaxis Abstracta (AST)** es una representación estructurada del programa en forma de árbol.

Cada nodo del AST representa una construcción del lenguaje (por ejemplo: una asignación, una operación aritmética, un número, etc.).

El AST es **más simple que el árbol sintáctico completo**, ya que omite tokens redundantes y conserva únicamente la estructura semántica del programa.

---

### Implementación del AST

La construcción del AST se realiza en el archivo `ast.py`.

Se define una clase `ASTNode` que representa cada nodo del árbol.

---

#### Clase ASTNode

```python
# ast.py

class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type            # Tipo de nodo (ej: 'ASSIGN', 'PLUS', 'INT')
        self.value = value          # Valor del nodo (por ejemplo, el nombre de la variable o el número)
        self.children = children if children is not None else []

    def to_dict(self):
        # Convierte el nodo en un diccionario para exportarlo como JSON
        return {
            "type": self.type,
            "value": self.value,
            "children": [child.to_dict() for child in self.children]
        }
```
### Ejemplo: asignación de variable
```py
def p_statement_assign(p):
    'statement : ID EQUALS expression SEMICOLON'
    p[0] = ASTNode('ASSIGN', p[1], [p[3]])
```
### Ejemplo: operacion aritmetica
```py
def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = ASTNode('PLUS', None, [p[1], p[3]])
```
### Visualizacion del AST
```py
{
    "type": "ASSIGN",
    "value": "a",
    "children": [
        {
            "type": "PLUS",
            "value": null,
            "children": [
                { "type": "INT", "value": 5, "children": [] },
                { "type": "INT", "value": 3, "children": [] }
            ]
        }
    ]
}
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
# errors.py

errores = []

def agregar_error(tipo, descripcion, linea, columna):
    error = {
        "tipo": tipo,
        "descripcion": descripcion,
        "linea": linea,
        "columna": columna
    }
    errores.append(error)

def generar_reporte_errores():
    import json
    with open("reports/errores.json", "w") as f:
        json.dump(errores, f, indent=4)
```
### Reporte de Tabla de Símbolos
```py
tabla_simbolos = []

def agregar_simbolo(nombre, tipo, valor, linea, columna):
    simbolo = {
        "nombre": nombre,
        "tipo": tipo,
        "valor": valor,
        "linea": linea,
        "columna": columna
    }
    tabla_simbolos.append(simbolo)

def generar_reporte_simbolos():
    import json
    with open("reports/symbols.json", "w") as f:
        json.dump(tabla_simbolos, f, indent=4)
```
### Reporte de AST
```py
with open("reports/ast.json", "w") as f:
    json.dump(ast_root.to_dict(), f, indent=4)
```
### Reporte de Memoria
```py
memoria = {}

def set_variable(nombre, valor):
    memoria[nombre] = valor

def generar_reporte_memoria():
    import json
    with open("reports/memory.json", "w") as f:
        json.dump(memoria, f, indent=4)
```
### Reporte de Advertencias
```py
warnings = []

def agregar_advertencia(mensaje, linea):
    warnings.append({
        "mensaje": mensaje,
        "linea": linea
    })

def generar_reporte_warnings():
    import json
    with open("reports/warnings.json", "w") as f:
        json.dump(warnings, f, indent=4)
```
## Librerías y Dependencias

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
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "vite": "^4.0.0"
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