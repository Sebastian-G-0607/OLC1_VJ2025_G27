import math
from backend.src.Interprete.nodes.expresiones.Shuffle import Shuffle
from backend.src.Interprete.nodes.expresiones.Sort import Sort
from backend.src.Interprete.nodes.instrucciones.Break import Break
from backend.src.Interprete.nodes.instrucciones.Continue import Continue
from backend.src.Interprete.nodes.instrucciones.Execute import Execute
from backend.src.Interprete.nodes.instrucciones.Procedimiento import Procedimiento
from backend.src.Interprete.nodes.nativos.Nativo import Nativo
from backend.src.Interprete.semanticas.semanticaDeclaracion import validarDeclaracion
from backend.src.Interprete.semanticas.semanticaSuma import validar_suma
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.simbol.Simbolo import Symbol
from backend.src.Interprete.semanticas.semanticaResta import validar_resta
from backend.src.Interprete.semanticas.semanticaMultiplicacion import validar_multiplicacion
from backend.src.Interprete.semanticas.semanticaDivision import validar_division
from backend.src.Interprete.semanticas.semanticaIgual import validar_igual
from backend.src.Interprete.semanticas.semanticaDiferente import validar_diferenciacion
from backend.src.Interprete.semanticas.semanticaMenor import validar_menor
from backend.src.Interprete.semanticas.semanticaOR import validar_OR
from backend.src.Interprete.semanticas.semanticaAND import validar_AND
from backend.src.Interprete.semanticas.semanticaPotencia import validar_potencia
from backend.src.Interprete.semanticas.semanticaMayorIgualQue import validar_Mayorigualque
from backend.src.Interprete.semanticas.semanticaMenorIgualQue import validar_Menorigualque
from backend.src.Interprete.semanticas.semanticaModulo import validar_modulo
from backend.src.Interprete.semanticas.semanticaMayorQue import validar_Mayorque
from backend.src.Interprete.semanticas.semanticaNot import validar_Not
from backend.src.Interprete.semanticas.semanticaXor import validar_Xor
from backend.src.Interprete.semanticas.semanticaUmenos import validar_Umenos
from backend.src.Interprete.visitor_object.visitorBase import Visitor
from backend.src.Interprete.nodes.Nodo import Nodo
from backend.src.Interprete.simbol.RaizArbol import Arbol
from backend.src.Interprete.errors.Error import Error
from backend.src.Interprete.simbol.InstanciaTabla import st
from backend.src.Interprete.simbol.ListaErrores import errores
from backend.src.Interprete.semanticas.semanticaDimensiones import recorrer_dimensiones, save_row_major, validar_tipos
import re
import numpy as np

class Visitor_Output(Visitor):
    def __init__(self, Arbol: Arbol):
        self.Arbol = Arbol
    
    # VISITA UN NÚMERO Y DEVUELVE SU VALOR
    def visit_Nativo(self, nodo: Nodo):
        return nodo.valor

    def visit_Suma(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        #SE COMPRUEBA SI EL VALOR IZQUIERDO ES UN ERROR
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        #SE COMPRUEBA SI EL VALOR DERECHO ES UN ERROR
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        resultado, tipo = validar_suma(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado

    def visit_Resta(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        resultado, tipo = validar_resta(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo
        return resultado

    def visit_Multiplicacion(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        resultado, tipo = validar_multiplicacion(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo
        return resultado

    def visit_Division(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        if valorDer == 0:
            error = Error("semántico", "División por cero no permitida.", nodo.linea, nodo.columna)
            errores.append(error)
            return error
        resultado, tipo = validar_division(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo
        return resultado
    
    def visit_Potencia(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        #SE COMPRUEBA SI EL VALOR IZQUIERDO ES UN ERROR
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        #SE COMPRUEBA SI EL VALOR DERECHO ES UN ERROR
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        resultado, tipo = validar_potencia(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado
    
    def visit_Umenos(self, nodo: Nodo):
        valor = nodo.expresion.accept(self)
        #SE COMPRUEBA SI EL VALOR ES UN ERROR
        if isinstance(valor, Error):
            errores.append(valor)
            return
        resultado, tipo = validar_Umenos(nodo.expresion, valor)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado
    
    def visit_Modulo(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        #SE COMPRUEBA SI EL VALOR IZQUIERDO ES UN ERROR
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        #SE COMPRUEBA SI EL VALOR DERECHO ES UN ERROR
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        if valorDer == 0:
            error = Error("semántico", "División por cero no permitida.", nodo.linea, nodo.columna)
            errores.append(error)
            return error
        resultado, tipo = validar_modulo(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado
    
    def visit_IgualQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        resultado, tipo = validar_igual(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo
        return resultado
    
    def visit_DiferenteQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        resultado, tipo = validar_diferenciacion(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo
        return resultado

    def visit_MayorQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        #SE COMPRUEBA SI EL VALOR IZQUIERDO ES UN ERROR
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        #SE COMPRUEBA SI EL VALOR DERECHO ES UN ERROR
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        resultado, tipo = validar_Mayorque(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado
    
    def visit_MayorIgualQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        #SE COMPRUEBA SI EL VALOR IZQUIERDO ES UN ERROR
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        #SE COMPRUEBA SI EL VALOR DERECHO ES UN ERROR
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        resultado, tipo = validar_Mayorigualque(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado
    
    def visit_MenorQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        resultado, tipo = validar_menor(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo
        return resultado
    
    def visit_MenorIgualQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        #SE COMPRUEBA SI EL VALOR IZQUIERDO ES UN ERROR
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        #SE COMPRUEBA SI EL VALOR DERECHO ES UN ERROR
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        resultado, tipo = validar_Menorigualque(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado
    
    def visit_And(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        resultado, tipo = validar_AND(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo
        return resultado
    
    def visit_Or(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        resultado, tipo = validar_OR(nodo.izquierda, nodo.derecha , valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo
        return resultado

    def visit_Not(self, nodo: Nodo):
        valor = nodo.expresion.accept(self)
        if isinstance(valor, Error):
            errores.append(valor)
            return
        resultado, tipo = validar_Not(nodo.expresion, valor)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo
        return resultado
    
    def visit_Xor(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        #SE COMPRUEBA SI EL VALOR IZQUIERDO ES UN ERROR
        if isinstance(valorIzq, Error):
            errores.append(valorIzq)
            return
        valorDer = nodo.derecha.accept(self)
        #SE COMPRUEBA SI EL VALOR DERECHO ES UN ERROR
        if isinstance(valorDer, Error):
            errores.append(valorDer)
            return
        resultado, tipo = validar_Xor(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        if isinstance(resultado, Error):
            errores.append(resultado)
            return resultado
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado

    def visit_Println(self, nodo: Nodo):
        if nodo is None:
            return
        valor = nodo.expresion.accept(self)
        if(isinstance(valor, Error)):
            return
        self.Arbol.Print(str(valor))
    
    def visit_Asignacion(self, nodo: Nodo):
        valor = nodo.valor.accept(self)
        if isinstance(valor, Error):
            errores.append(valor)
            return valor
        #OBTENGO EL TIPO DE LA VARIABLE
        try:
            tipoVariable = st.get_variable(nodo.id)[1]
        except KeyError:
            error = Error("semántico", f'La variable {nodo.id} no está declarada', nodo.linea, nodo.columna)
            errores.append(error)
            return error
        #VERIFICO SI EL TIPO DE LA VARIABLE ES EL MISMO QUE EL DEL VALOR
        if nodo.valor.tipo == tipoVariable:
            try:
                st.update_variable(nodo.id, valor)
                return
            except KeyError:
                error = Error("semántico", f'La variable {nodo.id} no está declarada', nodo.linea, nodo.columna)
                errores.append(error)
                return error
        else:
            error = Error("semántico", f'Se intentó asignar un valor de tipo {nodo.valor.tipo} a una variable de tipo {tipoVariable}', nodo.linea, nodo.columna)
            errores.append(error)
            return error

    def visit_AccesoVariable(self, nodo: Nodo):
        # OBTENGO EL SIMBOLO DE LA VARIABLE
        try:
            simbolo, tipo = st.get_variable(nodo.id)
            nodo.tipo = tipo # Actualizar el tipo del nodo
        except KeyError:
            error = Error("semántico", f'La variable {nodo.id} no está declarada', nodo.linea, nodo.columna)
            print(error)
            errores.append(error)
            return error
        nativo = Nativo(tipo, simbolo)
        return nativo.accept(self)
    
    def visit_Declaracion(self, nodo: Nodo):
        # VERIFICAR SI LA DECLARACIÓN CONTIENE O NO VALOR
        if nodo.valor is None:
            try:
                valor, tipo = validarDeclaracion(nodo)
            except ValueError as e:
                errores.append(Error("semántico", str(e), nodo.linea, nodo.columna))
                return e
            nodo.tipo = tipo  # Actualizar el tipo del nodo
            st.add_variable(nodo.id, tipo, valor, nodo.linea, nodo.columna)
            return
        
        #SI NO TIENE VALOR, SE ACEPTA EL VALOR Y SE VERIFICA SU TIPO
        valor = nodo.valor.accept(self)
        if isinstance(valor, Error):
            return valor
        try:
            tipoVariable = validarDeclaracion(nodo)[1]
        except ValueError as e:
            errores.append(Error("semántico", str(e), nodo.linea, nodo.columna))
            return e
        nodo.tipo = tipoVariable # Actualizar el tipo del nodo

        #VERIFICO SI ES ENTERO, SI ES ENTERO PUEDE RECIBIR ENTERO O BOOLEAN
        if nodo.tipo == Tipos.INT and nodo.valor.tipo == Tipos.BOOL:
            valor = int(valor)
            st.add_variable(nodo.id, tipoVariable, valor, nodo.linea, nodo.columna)
            return

        #VERIFICO SI EL TIPO DE LA VARIABLE ES EL MISMO QUE EL DEL VALOR
        if nodo.tipo == nodo.valor.tipo:
            st.add_variable(nodo.id, tipoVariable, valor, nodo.linea, nodo.columna)
            return
        else:
            error = Error("semántico", f'Se intentó asignar un valor de tipo {nodo.valor.tipo} al una variable de tipo {tipoVariable}', nodo.linea, nodo.columna)
            errores.append(error)
            return error
        
    def visit_Incremento(self, nodo: Nodo):
        try:
            valor, tipo = st.get_variable(nodo.variable)
        except KeyError:
            error = Error("semántico", f'La variable {nodo.variable} no está declarada', nodo.linea, nodo.columna)
            errores.append(error)
            return error
        if isinstance(valor, Error):
            return valor
        if tipo not in [Tipos.INT, Tipos.FLOAT]:
            error = Error("semántico", f'La variable {nodo.variable} debe ser de tipo entero o flotante para poder incrementarla', nodo.linea, nodo.columna)
            errores.append(error)
            return error
        try:
            st.update_variable(nodo.variable, valor + 1)
            return
        except KeyError:
            error = Error("semántico", f'La variable {nodo.variable} no está declarada', nodo.linea, nodo.columna)
            errores.append(error)
            return error

    def visit_Decremento(self, nodo: Nodo):
        try:
            valor, tipo = st.get_variable(nodo.variable)
        except KeyError:
            error = Error("semántico", f'La variable {nodo.variable} no está declarada', nodo.linea, nodo.columna)
            errores.append(error)
            return error
        if isinstance(valor, Error):
            return valor
        if tipo not in [Tipos.INT, Tipos.FLOAT]:
            error = Error("semántico", f'La variable {nodo.variable} debe ser de tipo entero o flotante para poder decrementarla', nodo.linea, nodo.columna)
            errores.append(error)
            return error
        try:
            st.update_variable(nodo.variable, valor - 1)
            return
        except KeyError:
            error = Error("semántico", f'La variable {nodo.variable} no está declarada', nodo.linea, nodo.columna)
            errores.append(error)
            return error

    def visit_If(self, nodo: Nodo):
        st.new_scope(f'if_{nodo.id}')
        condicion = nodo.condicion.accept(self)
        
        #SE COMPRUEBA SI LA CONDICIÓN ES UN ERROR O SI NO ES BOOLEANA
        if isinstance(condicion, Error):
            st.exit_scope()
            return
        if nodo.condicion.tipo != Tipos.BOOL:
            error = Error("semántico", f'La condición de un If debe ser de tipo booleano', nodo.linea, nodo.columna)
            errores.append(error)
            st.exit_scope()
            print(error)
            return error
        
        if condicion:
            if nodo.instrucciones is None:
                st.exit_scope()
                return
            for instruccion in nodo.instrucciones:
                resultado = instruccion.accept(self)
                if isinstance(resultado, Error):
                    st.exit_scope()
                    return resultado
                if isinstance(resultado, Break):
                    st.exit_scope()
                    return resultado
                if isinstance(resultado, Continue):
                    st.exit_scope()
                    return resultado
        st.exit_scope()
    
    def visit_Else(self, nodo: Nodo):
        st.new_scope(f'else_{nodo.id}')
        if nodo.instrucciones is None:
            st.exit_scope()
            return
        
        for instruccion in nodo.instrucciones:
            resultado = instruccion.accept(self)
            if isinstance(resultado, Error):
                    st.exit_scope()
                    return resultado
            if isinstance(resultado, Break):
                st.exit_scope()
                return resultado
            if isinstance(resultado, Continue):
                st.exit_scope()
                return resultado
        st.exit_scope()

    def visit_IfElse(self, nodo: Nodo):
        st.new_scope(f'if_else_{nodo.id}')
        condicion = nodo.condicion.accept(self)
        #SE COMPRUEBA SI LA CONDICIÓN ES UN ERROR
        if isinstance(condicion, Error):
            st.exit_scope()
            return condicion
        #SE COMPRUEBA SI EL TIPO DE LA CONDICIÓN ES BOOLEANO
        if nodo.condicion.tipo != Tipos.BOOL:
            error = Error("semántico", f'La condición de un If debe ser de tipo booleano', nodo.linea, nodo.columna)
            st.exit_scope()
            print(error)
            errores.append(error)
            return error
        
        if condicion:
            if nodo.instrucciones_if is None:
                st.exit_scope()
                return
            for instruccion in nodo.instrucciones_if:
                resultado = instruccion.accept(self)
                if isinstance(resultado, Error):
                    st.exit_scope()
                    return resultado
                if isinstance(resultado, Break):
                    st.exit_scope()
                    return resultado
                if isinstance(resultado, Continue):
                    st.exit_scope()
                    return resultado
        else:
            nodo.instrucciones_else.accept(self)
        st.exit_scope()

    def visit_IfElseIf(self, nodo: Nodo):
        st.new_scope(f'if_else_if_{nodo.id}')
        condicion = nodo.condicion.accept(self)
        #SE COMPRUEBA SI LA CONDICIÓN ES UN ERROR
        if isinstance(condicion, Error):
            st.exit_scope()
            return condicion
        #SE COMPRUEBA SI EL TIPO DE LA CONDICIÓN ES BOOLEANO
        if nodo.condicion.tipo != Tipos.BOOL:
            error = Error("semántico", f'La condición de un If debe ser de tipo booleano', nodo.linea, nodo.columna)
            errores.append(error)
            st.exit_scope()
            print(error)
            return error
        
        if nodo.instrucciones_if is None:
            st.exit_scope()
            return
        if condicion:
            for instruccion in nodo.instrucciones_if:
                resultado = instruccion.accept(self)
                if isinstance(resultado, Error):
                    st.exit_scope()
                    return resultado
                if isinstance(resultado, Break):
                    st.exit_scope()
                    return resultado
                if isinstance(resultado, Continue):
                    st.exit_scope()
                    return resultado
        else:
            nodo.elseif.accept(self)
        st.exit_scope()

    def visit_Switch(self, nodo: Nodo):
        if nodo.expresion is None:
            error = Error("semántico", f'La expresión del Switch no puede ser nula', nodo.linea, nodo.columna)
            print(error)
            errores.append(error)
            return

        valorComparado = nodo.expresion.accept(self)
        if nodo.expresion.tipo != Tipos.INT:
            error = Error("semántico", f'La expresión del Switch debe ser de tipo entero', nodo.linea, nodo.columna)
            print(error)
            errores.append(error)
            return
        #SE OBTIENE EL VALOR DE LA EXPRESIÓN DEL SWITCH

        #RECORRO LA LISTA DE CASOS DEL SWITCH
        for caso in nodo.lista_casos:
            valor = caso.condicion.accept(self)
            if isinstance(valor, Error):
                return valor
            if valorComparado == valor:
                st.new_scope(f'switch_case_{caso.id}')
                for instruccion in caso.instrucciones_case:
                    resultado = instruccion.accept(self)
                st.exit_scope()
                return
            if valor == 'default':
                st.new_scope(f'switch_default_{caso.id}')
                for instruccion in caso.instrucciones_case:
                    resultado = instruccion.accept(self)
                st.exit_scope()
                return

    def visit_Case(self, nodo: Nodo):
        if not isinstance(nodo.condicion, Nativo):
            error = Error("semántico", f'La condición del Case debe ser un valor primitivo', nodo.linea, nodo.columna)
            errores.append(error)
            return
        return nodo.condicion.accept(self)

    def visit_While(self, nodo: Nodo):
        st.new_scope(f'while_{nodo.id}')
        condicion = nodo.condition.accept(self)
        #SE COMPRUEBA SI LA CONDICIÓN ES UN ERROR O SI NO ES BOOLEANA
        if isinstance(condicion, Error):
            st.exit_scope()
            return condicion
        if nodo.condition.tipo != Tipos.BOOL:
            error = Error("semántico", f'La condición de un While debe ser de tipo booleano', nodo.linea, nodo.columna)
            errores.append(error)
            st.exit_scope()
            return

        if nodo.instructions is None:
            st.exit_scope()
            return
        
        while condicion:
            for instruccion in nodo.instructions:
                #SI ES BREAK, SE SALE DEL BUCLE
                resultado = instruccion.accept(self) # Ejecutar cada instrucción del ciclo
                if isinstance(resultado, Error):
                    st.exit_scope()
                    return resultado
                if isinstance(resultado, Break):
                    st.exit_scope()
                    return
                if isinstance(resultado, Continue):
                    break
            condicion = nodo.condition.accept(self) # Re-evaluar la condición al inicio del ciclo
        st.exit_scope()

    def visit_For(self, nodo: Nodo):
        st.new_scope(f'for_{nodo.id}')

        #PRIMERO, SE ACEPTA LA DECLARACIÓN O ASIGNACIÓN DE LA VARIABLE DE CONTROL
        incio = nodo.declaracion.accept(self)
        if isinstance(incio, Error):
            st.exit_scope()
            return incio
        
        #SE ACEPTA LA CONDICIÓN DEL BUCLE Y SE COMPRUEBA SI ES UN ERROR O NO ES BOOLEANA
        condicion = nodo.condicion.accept(self)
        if isinstance(condicion, Error):
            st.exit_scope()
            return condicion
        
        if nodo.condicion.tipo != Tipos.BOOL:
            error = Error("semántico", f'La condición de un For debe ser de tipo booleano', nodo.linea, nodo.columna)
            errores.append(error)
            st.exit_scope()
            return

        #SE RECORREN LAS INSTRUCCIONES DEL BUCLE MIENTRAS LA CONDICIÓN SEA VERDADERA
        while condicion:
            st.new_scope(f'for_instrucciones_{nodo.id}')
            if nodo.instrucciones is None:
                st.exit_scope() #se sale del scope de las instrucciones del for
                st.exit_scope() #se sale del scope del bucle for
                return
            
            for instruccion in nodo.instrucciones:
                #SI ES BREAK, SE SALE DEL BUCLE
                resultado = instruccion.accept(self)

                if isinstance(resultado, Error):
                    st.exit_scope()
                    st.exit_scope() #se sale del scope de las instrucciones del for
                    return resultado
                if isinstance(resultado, Break):
                    st.exit_scope() #se sale del scope de las declaraciones del for
                    st.exit_scope() #se sale del scope de las instrucciones del for
                    return
                if isinstance(resultado, Continue):
                    break

            # Actualizar la variable de control del bucle
            nodo.actualizacion.accept(self)
            # Re-evaluar la condición al final de cada iteración
            condicion = nodo.condicion.accept(self)
            st.exit_scope() #se sale del scope de las instrucciones del for
        
        #SE SALE DEL SCOPE DEL BUCLE FOR
        st.exit_scope()

    def visit_DoWhile(self, nodo: Nodo):
        st.new_scope(f'do_while_{nodo.id}')

        # Primero, ejecutamos las instrucciones al menos una vez
        for instruccion in nodo.instrucciones:
            resultado = instruccion.accept(self)
            if isinstance(resultado, Error):
                st.exit_scope()
                return resultado
            if isinstance(resultado, Break):
                st.exit_scope()
                return resultado
            if isinstance(resultado, Continue):
                break
            
        # Luego, evaluamos la condición
        condicion = nodo.condicion.accept(self)
        
        #SE COMPRUEBA SI LA CONDICIÓN ES UN ERROR O NO ES BOOLEANA
        if isinstance(condicion, Error):
            st.exit_scope()
            return condicion
        if nodo.condicion.tipo != Tipos.BOOL:
            error = Error("semántico", f'La condición de un DoWhile debe ser de tipo booleano', nodo.linea, nodo.columna)
            errores.append(error)
            st.exit_scope()
            return

        while condicion:
            for instruccion in nodo.instrucciones:
                resultado = instruccion.accept(self)
                if isinstance(resultado, Error):
                    st.exit_scope()
                    return resultado
                if isinstance(resultado, Break):
                    st.exit_scope()
                    return resultado
                if isinstance(resultado, Continue):
                    break
            condicion = nodo.condicion.accept(self)

        st.exit_scope()

    def visit_Break(self, nodo: Nodo):
            return nodo

    def visit_Continue(self, nodo: Nodo, ciclo = False):
        return nodo

    def visit_Vector(self, nodo: Nodo):
        lista = []
        for elemento in nodo.elementos:
            valor = elemento.accept(self)
            if isinstance(valor, Error):
                errores.append(valor)
                return valor
            lista.append(valor)
        return lista

    def visit_DeclaracionVector(self, nodo: Nodo):
        match nodo.tipo:
            case 'int':
                nodo.tipo = Tipos.INT
            case 'float':
                nodo.tipo = Tipos.FLOAT
            case 'bool':
                nodo.tipo = Tipos.BOOL
            case 'char':
                nodo.tipo = Tipos.CHAR
            case 'str':
                nodo.tipo = Tipos.STRING

        lista = []
        #SI VIENE UN VECTOR CON VALORES
        if isinstance(nodo.valores, list):
            if nodo.valores is None:
            # Si no hay valores, se crea un vector vacío
                return
            
            # PRIMERO VALIDO QUE EL NÚMERO DE ELEMENTOS SEA EL CORRECTO
            if len(nodo.valores) != nodo.dimensiones[0]:
                error = Error("semántico", f'El número de valores del vector {nodo.identificador} no coincide con el número de dimensiones', nodo.linea, nodo.columna)
                errores.append(error)
                return error

            for valor in nodo.valores:
                valorAceptado = valor.accept(self)
                if isinstance(valorAceptado, Error):
                    errores.append(valorAceptado)
                    return valorAceptado
                lista.append(valorAceptado)

            # VALIDAR LAS DIMENSIONES DEL VECTOR
            newlista = recorrer_dimensiones(lista, nodo.dimensiones, nodo.linea, nodo.columna, nodo.identificador)
            if isinstance(newlista, Error):
                errores.append(newlista)
                return newlista

            # VALIDAR TIPOS
            validacion_semantica = validar_tipos(nodo.identificador, lista, nodo.tipo, nodo.dimensiones, nodo.linea, nodo.columna)
            if validacion_semantica is not True:
                errores.append(validacion_semantica)
                return validacion_semantica

            # GUARDAR EL VECTOR EN LA TABLA DE SÍMBOLOS
            save_row_major(lista, nodo.dimensiones, nodo.identificador, nodo.tipo, nodo.linea, nodo.columna)

            return lista
        
        # SI VIENE UNA FUNCIÓN SORT
        elif isinstance(nodo.valores, Sort):
            vector_sort = nodo.valores.accept(self)
            if isinstance(vector_sort, Error):
                return vector_sort
            #VALIDAR QUE EL VECTOR ES UNIDIMENSIONAL
            if len(nodo.dimensiones) != 1:
                error = Error("semántico", f'El vector {nodo.identificador} debe ser unidimensional para poder ordenarlo', nodo.linea, nodo.columna)
                errores.append(error)
                return error
            
            # VALIDAR LAS DIMENSIONES DEL VECTOR
            newlista = recorrer_dimensiones(vector_sort, nodo.dimensiones, nodo.linea, nodo.columna, nodo.identificador)
            if isinstance(newlista, Error):
                errores.append(newlista)
                return newlista

            # VALIDAR TIPOS
            validacion_semantica = validar_tipos(nodo.identificador, vector_sort, nodo.tipo, nodo.dimensiones, nodo.linea, nodo.columna)
            if validacion_semantica is not True:
                errores.append(validacion_semantica)
                return validacion_semantica
            
            #GUARDAR EL VECTOR EN LA TABLA DE SÍMBOLOS
            save_row_major(vector_sort, nodo.dimensiones, nodo.identificador, nodo.tipo, nodo.linea, nodo.columna)
            return vector_sort

        elif isinstance(nodo.valores, Shuffle):
            vector_shuffle = nodo.valores.accept(self)
            print("VECTOR SHUFFLE")
            print(vector_shuffle)
            print("SU TIPO")
            print(type(vector_shuffle))
            if isinstance(vector_shuffle, Error):
                errores.append(vector_shuffle)
                return vector_shuffle
            
            # VALIDAR LAS DIMENSIONES DEL VECTOR
            newlista = recorrer_dimensiones(vector_shuffle, nodo.dimensiones, nodo.linea, nodo.columna, nodo.identificador)
            if isinstance(newlista, Error):
                errores.append(newlista)
                return newlista

            # VALIDAR TIPOS
            validacion_semantica = validar_tipos(nodo.identificador, vector_shuffle, nodo.tipo, nodo.dimensiones, nodo.linea, nodo.columna)
            if validacion_semantica is not True:
                errores.append(validacion_semantica)
                return validacion_semantica
            
            #GUARDAR EL VECTOR EN LA TABLA DE SÍMBOLOS
            save_row_major(vector_shuffle, nodo.dimensiones, nodo.identificador, nodo.tipo, nodo.linea, nodo.columna)
            return vector_shuffle
        
    
    def visit_AccesoVector(self, nodo: Nodo):

        pos = ""
        for indice in nodo.indices:
            resultado = indice.accept(self)
            if isinstance(resultado, Error):
                errores.append(resultado)
                return resultado
            if not isinstance(resultado, int):
                if resultado.tipo not in [Tipos.INT, Tipos.FLOAT]:
                    error = Error("semántico", f'El índice del vector {nodo.id} debe ser de tipo entero o flotante', nodo.linea, nodo.columna)
                    errores.append(error)
                    return error
            pos += f"[{resultado}]"

        # VERIFICO SI EL VECTOR EXISTE
        existe = st.vector_exists(nodo.id)
        if not existe:
            error = Error("semántico", f'El vector {nodo.id} no está declarado', nodo.linea, nodo.columna)
            errores.append(error)
            return error

        acceso = nodo.id + pos

        # OBTENGO EL SIMBOLO DEL VECTOR
        try:
            simbolo, tipo = st.get_vector_pos(acceso)
            nodo.tipo = tipo  # Actualizar el tipo del nodo
        except KeyError:
            error = Error("semántico", f'El índice del arreglo {nodo.id} está fuera de rango', nodo.linea, nodo.columna)
            errores.append(error)
            return error
        
        nativo = Nativo(tipo, simbolo)
        return nativo.accept(self)
    
    def visit_AsignacionVector(self, nodo: Nodo):
        pos = ""
        for indice in nodo.indices:
            resultado = indice.accept(self)
            if isinstance(resultado, Error):
                errores.append(resultado)
                return resultado
            if not isinstance(resultado, int):
                if resultado.tipo not in [Tipos.INT, Tipos.FLOAT]:
                    error = Error("semántico", f'El índice del vector {nodo.id} debe ser de tipo entero o flotante', nodo.linea, nodo.columna)
                    errores.append(error)
                    return error
            pos += f"[{resultado}]"

        acceso = nodo.id + pos
        valor = nodo.valor.accept(self)
        if isinstance(valor, Error):
            errores.append(valor)
            return valor
        #VERIFICO SI EL VECTOR EXISTE
        existe = st.vector_exists(nodo.id)
        if not existe:
            error = Error("semántico", f'El vector {nodo.id} no está declarado', nodo.linea, nodo.columna)
            errores.append(error)
            return error

        # OBTENGO EL TIPO DEL VECTOR
        try:
            tipo = st.get_vector_pos(acceso)[1]
        except KeyError:
            error = Error("semántico", f'El índice del arreglo {nodo.id} está fuera de rango', nodo.linea, nodo.columna)
            errores.append(error)
            return error
        # VERIFICO SI EL TIPO DEL VALOR ES EL MISMO QUE EL DEL VECTOR
        if tipo == nodo.valor.tipo:
            try:
                st.update_vector_pos(acceso, valor)
                return
            except KeyError:
                error = Error("semántico", f'El índice del arreglo {nodo.id} está fuera de rango', nodo.linea, nodo.columna)
                errores.append(error)
                return error
        else:
            error = Error("semántico", f'Se intentó asignar un valor de tipo {nodo.valor.tipo} a un arreglo de tipo {tipo}', nodo.linea, nodo.columna)
            errores.append(error)
            return error

    def visit_Seno(self, nodo: Nodo):
        valor = nodo.expresion.accept(self)
        if isinstance(valor, Error):
            errores.append(valor)
            return valor
        if nodo.expresion.tipo not in [Tipos.INT, Tipos.FLOAT]:
            error = Error("semántico", f'La expresión del Seno debe ser de tipo entero o flotante', nodo.linea, nodo.columna)
            errores.append(error)
            return error
        resultado = math.sin(valor)
        return resultado
    
    def visit_Coseno(self, nodo: Nodo):
        valor = nodo.expresion.accept(self)
        if isinstance(valor, Error):
            errores.append(valor)
            return valor
        if nodo.expresion.tipo not in [Tipos.INT, Tipos.FLOAT]:
            error = Error("semántico", f'La expresión del Coseno debe ser de tipo entero o flotante', nodo.linea, nodo.columna)
            errores.append(error)
            return error
        resultado = math.cos(valor)
        return resultado
    
    def visit_Inversion(self, nodo: Nodo):
        valor = nodo.expresion.accept(self)
        if isinstance(valor, Error):
            errores.append(valor)
            return valor
        if nodo.expresion.tipo not in [Tipos.INT]:
            error = Error("semántico", f'La expresión de la Inversión debe ser de tipo entero', nodo.linea, nodo.columna)
            errores.append(error)
            return error
        resultado = int(str(abs(valor))[::-1])
        if valor < 0:
            resultado = -resultado
        return resultado
    
    def visit_Sort(self, nodo: Nodo):
        try:
            vector, dimensiones, tipoVec = st.get_vector(nodo.vector)
        except KeyError:
            error = Error("semántico", f'El vector {nodo.vector} no está declarado', nodo.linea, nodo.columna)
            errores.append(error)
            return error

        if tipoVec != Tipos.INT and tipoVec != Tipos.FLOAT:
            error = Error("semántico", f'El vector {nodo.vector} debe ser de tipo entero o flotante para poder ordenarlo', nodo.linea, nodo.columna)
            errores.append(error)
            return error
        
        if dimensiones != 1:
            error = Error("semántico", f'El vector {nodo.vector} debe ser unidimensional para poder ordenarlo', nodo.linea, nodo.columna)
            errores.append(error)
            return error

        if isinstance(vector, Error):
            errores.append(vector)
            return vector
        
        if not vector:
            error = Error("semántico", f'El vector {nodo.vector} está vacío', nodo.linea, nodo.columna)
            errores.append(error)
            return error

        # Ordenar el vector de menor a mayor
        vector.sort()
        # Actualizar el vector en la tabla de símbolos si es necesario
        return vector
    
    def visit_Shuffle(self, nodo: Nodo):
        try:
            vector, dimensiones, ultimo = st.get_vector(nodo.vector, shuffle=True)
        except KeyError:
            error = Error("semántico", f'El vector {nodo.vector} no está declarado', nodo.linea, nodo.columna)
            errores.append(error)
            return error

        if isinstance(vector, Error):
            errores.append(vector)
            return vector

        if not vector:
            error = Error("semántico", f'El vector {nodo.vector} está vacío', nodo.linea, nodo.columna)
            errores.append(error)
            return error

        # Buscar todos los números entre corchetes
        dims = [int(x) + 1 for x in re.findall(r'\[(\d+)\]', ultimo)]
        # Ahora dims contiene las dimensiones incrementadas en 1
        try:
            # Calcular la representación column major como un arreglo multidimensional
            arr = np.array(vector).reshape(dims, order='F')  # reshape en column-major order
            column_major = arr.tolist()  # convertir a lista de Python conservando dimensiones
        except Exception as e:
            err = Error("semántico", f'Error al calcular la representación column major: {e}', nodo.linea, nodo.columna)
            errores.append(err)
            return err
        return column_major
    
    def visit_Procedimiento(self, nodo: Nodo):
        # PRIMERO REVISO SI DENTRO DE SUS INSTRUCCIONES NO TIENE UNA INSTRUCCIÓN INSTANCIA DE Procedimiento
        for instruccion in nodo.instrucciones:
            if isinstance(instruccion, Procedimiento):
                error = Error("semántico", f'No se puede declarar un procedimiento dentro de otro procedimiento', instruccion.linea, instruccion.columna)
                errores.append(error)
                return error
            if isinstance(instruccion, Execute):
                    error = Error("semántico", f'No se puede llamar al procedimiento "{nodo.id}" desde su propia definición', instruccion.linea, instruccion.columna)
                    errores.append(error)
                    return error 

        # AÑADO EL PROCEDIMIENTO A LA TABLA DE SÍMBOLOS
        params = []
        for param in nodo.parametros:
            params.append({'id': str(param.id), 'tipo': str(param.tipo)})
        try:
            st.add_function(nodo.id, params, nodo.linea, nodo.columna)
        except Exception as e:
            error = Error("semántico", f'Error al añadir el procedimiento {nodo.id} a la tabla de símbolos: {str(e)}', nodo.linea, nodo.columna)
            errores.append(error)
            return error
        
        # AÑADO EL PROCEDIMIENTO AL AST
        self.Arbol.addProcedimiento(nodo)
        return
    
    def visit_Execute(self, nodo: Nodo):
        # PRIMERO REVISO SI EL PROCEDIMIENTO ESTÁ DECLARADO
        try:
            nombre = st.get_function(nodo.identificador)
        except KeyError:
            error = Error("semántico", f'El procedimiento {nodo.identificador} no está declarado', nodo.linea, nodo.columna)
            errores.append(error)
            return error
        
        if isinstance(nombre, Error):
            errores.append(nombre)
            return nombre

        # LUEGO, BUSCO LA DEFINICIÓN DEL PROCEDIMIENTO EN EL AST
        procedimiento = self.Arbol.findProcedimiento(nodo.identificador)
        if procedimiento is None:
            error = Error("semántico", f'El procedimiento {nodo.identificador} no está definido en el AST', nodo.linea, nodo.columna)
            errores.append(error)
            return error

        # VERIFICAR SI VIENEN PARAMETROS
        if len(procedimiento.parametros) == 0:
            if len(nodo.args) != 0:
                error = Error("semántico", f'El procedimiento {nodo.identificador} no acepta parámetros', nodo.linea, nodo.columna)
                errores.append(error)
                return error

        # SI EL PROCEDIMIENTO TIENE PARÁMETROS, VERIFICO QUE EN CANTIDAD COINCIDAN
        elif len(procedimiento.parametros) != len(nodo.args):
            error = Error("semántico", f'El procedimiento {nodo.identificador} espera {len(procedimiento.parametros)} parámetros, pero recibió {len(nodo.args)}', nodo.linea, nodo.columna)
            errores.append(error)
            return error

        # SI EL PROCEDIMIENTO TIENE PARÁMETROS, SE VERIFICA QUE LOS TIPOS COINCIDAN        
        st.new_scope(f'proc_{nodo.identificador}_{nodo.id}')
        for i, arg in enumerate(nodo.args):
            if i < len(procedimiento.parametros):
                tipo_parametro = procedimiento.parametros[i].tipo
                valor = arg.accept(self)
                if arg.tipo != tipo_parametro:
                    error = Error("semántico", f'El argumento {i + 1} del procedimiento {nodo.identificador} debe ser de tipo {tipo_parametro}, pero recibió {arg.tipo}', nodo.linea, nodo.columna)
                    errores.append(error)
                    st.exit_scope()
                    return error
                #SI LOS TIPOS COINCIDEN, AÑADO EL PARÁMETRO A LA TABLA DE SÍMBOLOS
                st.add_variable(procedimiento.parametros[i].id, tipo_parametro, valor, arg.linea, arg.columna)

        #AÑADO UN CONTADOR DE EJECUCIÓN AL PROCEDIMIENTO
        for proc in self.Arbol.getProcedimientos():
            if proc.id == nodo.identificador:
                proc.addEjecucion(nodo.linea)
                break

        # EJECUTO LAS INSTRUCCIONES DEL PROCEDIMIENTO
        for instruccion in procedimiento.instrucciones:
            resultado = instruccion.accept(self)
            if isinstance(resultado, Error):
                st.exit_scope()
                return resultado
            if isinstance(resultado, Break):
                st.exit_scope()
                return resultado
            if isinstance(resultado, Continue):
                st.exit_scope()
                return resultado
        # SALGO DEL SCOPE DEL PROCEDIMIENTO
        st.exit_scope()
        return