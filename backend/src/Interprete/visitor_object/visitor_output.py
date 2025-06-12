from backend.src.Interprete.semanticas.semanticaDeclaracion import validarDeclaracion
from backend.src.Interprete.semanticas.semanticaSuma import validar_suma
from backend.src.Interprete.simbol.ListaTipos import Tipos
from backend.src.Interprete.simbol.Simbolo import Symbol
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
        valorDer = nodo.derecha.accept(self)
        return valorIzq - valorDer
    
    def visit_Multiplicacion(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return valorIzq * valorDer

    def visit_Division(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        if valorDer == 0:
            raise ZeroDivisionError("División por cero no permitida.")
        return valorIzq / valorDer
    
    def visit_Potencia(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return valorIzq ** valorDer
    
    def visit_Umenos(self, nodo: Nodo):
        valor = nodo.expresion.accept(self)
        return -valor
    
    def visit_Modulo(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        if valorDer == 0:
            raise ZeroDivisionError("División por cero no permitida.")
        return valorIzq % valorDer
    
    def visit_IgualQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return valorIzq == valorDer
    
    def visit_DiferenteQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return valorIzq != valorDer
    
    def visit_MayorQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return valorIzq > valorDer
    
    def visit_MayorIgualQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return valorIzq >= valorDer
    
    def visit_MenorQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return valorIzq < valorDer
    
    def visit_MenorIgualQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return valorIzq <= valorDer
    
    def visit_And(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return valorIzq and valorDer
    
    def visit_Or(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return valorIzq or valorDer
    
    def visit_Not(self, nodo: Nodo):
        valor = nodo.expresion.accept(self)
        return not valor
    
    def visit_Xor(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return (valorIzq and not valorDer) or (not valorIzq and valorDer)

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
            st.update_variable(nodo.id, nodo.valor)
            return
        else:
            error = Error("semántico", f'Se intentó asignar un valor de tipo {nodo.valor.tipo} al una variable de tipo {tipoVariable}',)
            print(error)
            return error

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
            nodo.instrucciones_else_if.accept(self)
        st.exit_scope()