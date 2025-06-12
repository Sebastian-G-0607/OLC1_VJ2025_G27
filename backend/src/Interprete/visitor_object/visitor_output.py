from backend.src.Interprete.semanticas.semanticaSuma import validar_suma
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
        valorDer = nodo.derecha.accept(self)
        return valorIzq == valorDer
    
    def visit_DiferenteQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return valorIzq != valorDer
    
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
        valorDer = nodo.derecha.accept(self)
        return valorIzq < valorDer
    
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
        valorDer = nodo.derecha.accept(self)
        return valorIzq and valorDer
    
    def visit_Or(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return valorIzq or valorDer
    
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
        return None