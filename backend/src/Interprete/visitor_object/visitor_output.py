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
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        #SE COMPRUEBA SI EL VALOR DERECHO ES UN ERROR
        if isinstance(valorDer, Error):
            return valorDer
        resultado, tipo = validar_suma(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado

    def visit_Resta(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            return valorDer
        resultado, tipo = validar_resta(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        nodo.tipo = tipo 
        return resultado
    
    def visit_Multiplicacion(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            return valorDer
        resultado, tipo = validar_multiplicacion(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        nodo.tipo = tipo
        return resultado

    def visit_Division(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            return valorDer
        if valorDer == 0:
            raise ZeroDivisionError("División por cero no permitida.")
        resultado, tipo = validar_division(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        nodo.tipo = tipo
        return resultado
    
    def visit_Potencia(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        #SE COMPRUEBA SI EL VALOR IZQUIERDO ES UN ERROR
        if isinstance(valorIzq, Error):
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        #SE COMPRUEBA SI EL VALOR DERECHO ES UN ERROR
        if isinstance(valorDer, Error):
            return valorDer
        resultado, tipo = validar_potencia(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado
    
    def visit_Umenos(self, nodo: Nodo):
        valor = nodo.expresion.accept(self)
        #SE COMPRUEBA SI EL VALOR ES UN ERROR
        if isinstance(valor, Error):
            return valor
        resultado, tipo = validar_Umenos(nodo.expresion, valor)
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado
    
    def visit_Modulo(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        #SE COMPRUEBA SI EL VALOR IZQUIERDO ES UN ERROR
        if isinstance(valorIzq, Error):
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        #SE COMPRUEBA SI EL VALOR DERECHO ES UN ERROR
        if isinstance(valorDer, Error):
            return valorDer
        if valorDer == 0:
            raise ZeroDivisionError("División por cero no permitida.")
        resultado, tipo = validar_modulo(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado
    
    def visit_IgualQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            return valorDer
        resultado, tipo = validar_igual(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        nodo.tipo = tipo
        return resultado
    
    def visit_DiferenteQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq. Error):
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            return valorDer
        resulatado, tipo = validar_diferenciacion(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        nodo.tipo = tipo
        return resulatado
    
    def visit_MayorQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        #SE COMPRUEBA SI EL VALOR IZQUIERDO ES UN ERROR
        if isinstance(valorIzq, Error):
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        #SE COMPRUEBA SI EL VALOR DERECHO ES UN ERROR
        if isinstance(valorDer, Error):
            return valorDer
        resultado, tipo = validar_Mayorque(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado
    
    def visit_MayorIgualQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        #SE COMPRUEBA SI EL VALOR IZQUIERDO ES UN ERROR
        if isinstance(valorIzq, Error):
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        #SE COMPRUEBA SI EL VALOR DERECHO ES UN ERROR
        if isinstance(valorDer, Error):
            return valorDer
        resultado, tipo = validar_Mayorigualque(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado
    
    def visit_MenorQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            return valorDer
        resultado, tipo = validar_menor(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        nodo.tipo = tipo
        return resultado
    
    def visit_MenorIgualQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        #SE COMPRUEBA SI EL VALOR IZQUIERDO ES UN ERROR
        if isinstance(valorIzq, Error):
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        #SE COMPRUEBA SI EL VALOR DERECHO ES UN ERROR
        if isinstance(valorDer, Error):
            return valorDer
        resultado, tipo = validar_Menorigualque(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado
    
    def visit_And(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            return valorDer
        resultado, tipo = validar_AND(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        nodo.tipo = tipo
        return resultado
    
    def visit_Or(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        if isinstance(valorIzq, Error):
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        if isinstance(valorDer, Error):
            return valorDer
        resultado, tipo = validar_OR(nodo.izquierda, nodo.derecha , valorIzq, valorDer)
        nodo.tipo = tipo 
        return resultado
    
    def visit_Not(self, nodo: Nodo):
        valor = nodo.expresion.accept(self)
        if isinstance(valor, Error):
            return valor
        resultado, tipo = validar_Not(nodo.expresion, valor)
        nodo.tipo = tipo
        return resultado
    
    def visit_Xor(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        #SE COMPRUEBA SI EL VALOR IZQUIERDO ES UN ERROR
        if isinstance(valorIzq, Error):
            return valorIzq
        valorDer = nodo.derecha.accept(self)
        #SE COMPRUEBA SI EL VALOR DERECHO ES UN ERROR
        if isinstance(valorDer, Error):
            return valorDer
        resultado, tipo = validar_Xor(nodo.izquierda, nodo.derecha, valorIzq, valorDer)
        nodo.tipo = tipo  # Actualiza el tipo del nodo
        return resultado

    def visit_Println(self, nodo: Nodo):
        valor = nodo.expresion.accept(self)
        self.Arbol.Print(str(valor))
    
    def visit_Asignacion(self, nodo: Nodo):
        valor = nodo.valor.accept(self)
        if isinstance(valor, Error):
            return valor
        #OBTENGO EL TIPO DE LA VARIABLE
        tipoVariable = st.get_variable(nodo.id)[1]
        #VERIFICO SI EL TIPO DE LA VARIABLE ES EL MISMO QUE EL DEL VALOR
        if nodo.valor.tipo == tipoVariable:
            st.update_variable(nodo.id, valor)
            return
        else:
            error = Error("semántico", f'Se intentó asignar un valor de tipo {nodo.valor.tipo} al una variable de tipo {tipoVariable}',)
            print(error)
            return error

    def visit_AccesoVariable(self, nodo: Nodo):
        # OBTENGO EL SIMBOLO DE LA VARIABLE
        try:
            simbolo, tipo = st.get_variable(nodo.id)
            nodo.tipo = tipo # Actualizar el tipo del nodo
        except KeyError:
            error = Error("semántico", f'La variable {nodo.id} no está declarada')
            print(error)
            return error
        nativo = Nativo(tipo, simbolo)
        return nativo.accept(self)
    
    def visit_Declaracion(self, nodo: Nodo):
        # VERIFICAR SI LA DECLARACIÓN CONTIENE O NO VALOR
        if nodo.valor is None:
            valor, tipo = validarDeclaracion(nodo)
            nodo.tipo = tipo  # Actualizar el tipo del nodo
            st.add_variable(nodo.id, tipo, nodo.valor)
            return
        
        #SI NO TIENE VALOR, SE ACEPTA EL VALOR Y SE VERIFICA SU TIPO
        valor = nodo.valor.accept(self)
        if isinstance(valor, Error):
            return valor
        tipoVariable = validarDeclaracion(nodo)[1]
        nodo.tipo = tipoVariable # Actualizar el tipo del nodo        
        #VERIFICO SI EL TIPO DE LA VARIABLE ES EL MISMO QUE EL DEL VALOR
        if nodo.tipo == nodo.valor.tipo:
            st.add_variable(nodo.id, tipoVariable, valor)
            return
        else:
            error = Error("semántico", f'Se intentó asignar un valor de tipo {nodo.tipo} al una variable de tipo {tipoVariable}',)
            print(error)
            return error
        
    def visit_If(self, nodo: Nodo):
        st.new_scope(f'if_{nodo.id}')
        condicion = nodo.condicion.accept(self)
        
        #SE COMPRUEBA SI LA CONDICIÓN ES UN ERROR O SI NO ES BOOLEANA
        if isinstance(condicion, Error):
            return condicion
        if nodo.condicion.tipo != Tipos.BOOL:
            error = Error("semántico", f'La condición de un If debe ser de tipo booleano')
            print(error)
            return error
        
        if condicion:
            for instruccion in nodo.instrucciones:
                resultado = instruccion.accept(self)
                if isinstance(resultado, Error):
                    return resultado
        st.exit_scope()
    
    def visit_Else(self, nodo: Nodo):
        st.new_scope(f'else_{nodo.id}')
        for instruccion in nodo.instrucciones:
            resultado = instruccion.accept(self)
            if isinstance(resultado, Error):
                return resultado
        st.exit_scope()

    def visit_IfElse(self, nodo: Nodo):
        st.new_scope(f'if_else_{nodo.id}')
        condicion = nodo.condicion.accept(self)
        #SE COMPRUEBA SI LA CONDICIÓN ES UN ERROR
        if isinstance(condicion, Error):
            return condicion
        #SE COMPRUEBA SI EL TIPO DE LA CONDICIÓN ES BOOLEANO
        if nodo.condicion.tipo != Tipos.BOOL:
            error = Error("semántico", f'La condición de un If debe ser de tipo booleano')
            print(error)
            return error
        
        if condicion:
            for instruccion in nodo.instrucciones_if:
                resultado = instruccion.accept(self)
                if isinstance(resultado, Error):
                    return resultado
        else:
            nodo.instrucciones_else.accept(self)
        st.exit_scope()

    def visit_IfElseIf(self, nodo: Nodo):
        st.new_scope(f'if_else_if_{nodo.id}')
        condicion = nodo.condicion.accept(self)
        #SE COMPRUEBA SI LA CONDICIÓN ES UN ERROR
        if isinstance(condicion, Error):
            return condicion
        #SE COMPRUEBA SI EL TIPO DE LA CONDICIÓN ES BOOLEANO
        if nodo.condicion.tipo != Tipos.BOOL:
            error = Error("semántico", f'La condición de un If debe ser de tipo booleano')
            print(error)
            return error
        
        if condicion:
            for instruccion in nodo.instrucciones_if:
                resultado = instruccion.accept(self)
                if isinstance(resultado, Error):
                    return resultado
        else:
            nodo.elseif.accept(self)
        st.exit_scope()

    
    def visit_While(self, nodo: Nodo):
        st.new_scope(f'while_{nodo.id}')
        condicion = nodo.condition.accept(self)
        #SE COMPRUEBA SI LA CONDICIÓN ES UN ERROR O SI NO ES BOOLEANA
        if isinstance(condicion, Error):
            return condicion
        if nodo.condition.tipo != Tipos.BOOL:
            error = Error("semántico", f'La condición de un While debe ser de tipo booleano')
            print(error)
            return error
        
        while condicion:
            for instruccion in nodo.instructions:
                resultado = instruccion.accept(self) # Ejecutar cada instrucción del ciclo
                if isinstance(resultado, Error):
                    return resultado
            condicion = nodo.condition.accept(self) # Re-evaluar la condición al inicio del ciclo
        st.exit_scope()