from backend.src.Interprete.nodes.instrucciones.Break import Break
from backend.src.Interprete.nodes.instrucciones.Continue import Continue
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
