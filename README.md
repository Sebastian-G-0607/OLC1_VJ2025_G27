# 🌟 Proyecto  - Lenguaje Obj-C 🚀

## 🏫 Universidad de San Carlos de Guatemala  
**Facultad de Ingeniería**  
**Escuela de Ciencias y Sistemas**  
**Curso:** Organización de Lenguajes y Compiladores 1  
**Vacaciones Primer Semestre 2025**  
**Catedrático:** Ing. Mario Bautista  

---

## 👨‍💻 Participantes del Proyecto 
### 📌 GRUPO # 27 

- 👨‍🎓 Eduardo Sebastián Gutiérrez de Felipe  `Coordinador`
- 👨‍🎓 Carlos Eduardo Lau López  
- 👨‍🎓 Sebastián Antonio Romero Tzitizmit  
- 👨‍🎓 Christian David Chinchilla Santos  

---

## Instrucciones de instalación y ejecución
1. **Clonar el repositorio:**

    ```bash
    # con HTTPS
    git clone https://github.com/Sebastian-G-0607/OLC1_VJ2025_G27.git

    # con SSH
    git clone git@github.com:Sebastian-G-0607/OLC1_VJ2025_G27.git
    ```

2. **Revisa que tengas instalado Python 3:**

    ```bash
    python --version
    ```
    Deberías ver la versión de Python 3 instalada. Si no lo tienes, puedes descargarlo desde [python.org](https://www.python.org/downloads/).

3. **Navega al directorio del proyecto y crea un entorno virtual:**

    ```bash
    cd OLC1_VJ2025_G27
    python -m venv venv
    ```

4. **Activa el entorno virtual:**

  - En Windows cmd:
    ```bash
    .\venv\Scripts\activate
    ```
  - En PowerShell:
    ```bash
    .\venv\Scripts\Activate.ps1
    ```
  - En macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

5. **Verifica que el entorno virtual esté activo y verifica la ruta del pip:**

    El entorno virtual debería cambiar tu prompt de terminal para mostrar que está activo. Puedes verificar que estás usando el pip correcto ejecutando:

    ```bash
    which pip
    ```

    Deberías ver la ruta del pip dentro del entorno virtual, algo como `tu_ruta/OLC1_VJ2025_G27/venv/bin/pip` o `tu_ruta/OLC1_VJ2025_G27/venv\Scripts\pip.exe`.

6. **Instala las dependencias necesarias:**
    ```bash
    pip install -r requirements.txt
    ```

7. **Ejecuta el proyecto backend:**
    
    El archivo principal del proyecto es `backend/src/app.py`. Puedes ejecutarlo con ayuda de tu IDE o directamente desde la terminal con:

    ```bash
    python3 tu_ruta/OLC1_VJ2025_G27/backend/src/app.py
    ```

    Puedes ver tu ruta absoluta con el comando `pwd` en macOS/Linux o `cd` en Windows. Cambia `tu_ruta` por la primera parte de la ruta que obtuviste.

8. **Instala las dependencias del frontend:**
    
    Primero revisa que tengas instalado **Node.js** y **pnpm**. Puedes verificarlo con:

    ```bash
    node -v
    pnpm -v
    ```
    Si no tienes Node.js, puedes descargarlo desde [nodejs.org](https://nodejs.org/).
    Si no tienes pnpm, puedes instalarlo con:

    ```bash
    npm install -g pnpm
    ```

    Ahora puedes instalar las dependencias del frontend:

    ```bash
    cd frontend # Verifica que estás en OLC1_VJ2025_G27/frontend
    pnpm install
    ```

9. **Ejecuta el proyecto frontend:**
    
    Una vez instaladas las dependencias, puedes iniciar el servidor de desarrollo del frontend:

    ```bash
    pnpm run dev
    ```

10. **Prueba el proyecto:**
    
    Abre tu navegador y ve a `http://localhost:5173/` para ver la interfaz del proyecto.
    Puedes consultar la sintaxis completa del lenguaje Obj-C y ejemplos de uso en la [`definición del lenguaje`](./Documentacion/Enunciados). El proyecto fue desarrollado en dos fases y cada pdf contiene ejemplos de código y explicaciones detalladas para cada aspecto del lenguaje.

## 🎯 Objetivo General

Aplicar los conocimientos sobre la fase de análisis léxico y sintáctico de un compilador y su importancia dentro del contexto de lenguajes de programación.

---

## 📌 Objetivos Específicos

- Aprender a generar analizadores léxicos y sintácticos utilizando la librería **PLY**.
- Comprender los conceptos de token, lexema, patrones y expresiones regulares.
- Manejar errores léxicos correctamente.
- Ejecutar acciones gramaticales con el lenguaje de programación **Python**.

---

## 🧠 Descripción General del Proyecto

Este proyecto guía a los estudiantes en el diseño e implementación de un **lenguaje de programación propio** denominado **Obj-C**, desde sus fundamentos léxicos y sintácticos.

Durante el desarrollo se construyen analizadores léxicos y sintácticos empleando la librería **PLY (Python Lex-Yacc)**. El objetivo es crear una **gramática robusta**, capaz de interpretar correctamente estructuras propias del lenguaje como:

- Declaración de variables.
- Control de flujo.
- Operaciones aritméticas y lógicas.
- Reportes de errores, símbolos y AST.

El sistema promueve también el **manejo adecuado de errores** y fomenta buenas prácticas de programación.

---

## 💻 Entorno de Trabajo

### 📝 Editor
Un editor personalizado permite al usuario ingresar, cargar y analizar código fuente `.objc`.

### 🔄 Flujo de la Aplicación

1. **Cargar Archivo:** Soporte para archivos con extensión `.objc`.
2. **Interpretar:** Se analiza el código en el backend con Python y se muestra la respuesta en la consola, incluyendo un resumen de errores.

---

## ⚙️ Funcionalidades

- 📂 Carga de archivos `.objc`
- 🔍 Interpretación de código y ejecución de análisis
- 📊 Reportes:
  - Tabla de Errores 🐞
  - AST (Árbol de Sintaxis Abstracta) 🌳
  - Tabla de Símbolos 📋

---

## 🧬 Características del Lenguaje Obj-C

- ✅ **Case Insensitive**
- 💬 **Comentarios:** Soporte para comentarios de una línea (`//`) y múltiples líneas (`/* */`)
- 🔢 **Tipos de Datos:** `INT`, `FLOAT`, `BOOL`, `CHAR`, `STR`
- 🔁 **Control de Flujo:** `IF`, `SWITCH`, `FOR`, `WHILE`, `DO-WHILE`
- ➕ **Operadores:** Aritméticos, Relacionales, Lógicos
- 📐 **Precedencia y Agrupación** de operaciones
- 💾 **Manejo de Errores**, incrementos (`++`) y decrementos (`--`)

---

## 📄 Reportes Generados

- 🐞 **Tabla de Errores:** Muestra errores léxicos, sintácticos y semánticos
- 📋 **Tabla de Símbolos:** Muestra variables, funciones y sus detalles
- 🌳 **AST:** Representación visual en forma de grafo del flujo del análisis

---

> 🛠️ Este proyecto representa la primera fase de implementación de un compilador para un lenguaje propio, integrando conocimientos teóricos y prácticos con Python y herramientas modernas como PLY.

---

¡Gracias por leer nuestro README! 😄