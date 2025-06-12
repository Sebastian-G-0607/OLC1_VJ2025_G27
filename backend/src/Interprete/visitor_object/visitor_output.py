from backend.src.Interprete.semanticas.semanticaSuma import validar_suma
from backend.src.Interprete.semanticas.semanticaResta import validar_resta
from backend.src.Interprete.semanticas.semanticaMultiplicacion import validar_multiplicacion
from backend.src.Interprete.semanticas.semanticaDivision import validar_division
from backend.src.Interprete.semanticas.semanticaIgual import validar_igual
from backend.src.Interprete.semanticas.semanticaDiferente import validar_diferenciacion
from backend.src.Interprete.semanticas.semanticaMenor import validar_menor
from backend.src.Interprete.semanticas.semanticaOR import validar_OR
from backend.src.Interprete.semanticas.semanticaAND import validar_AND
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
        valorDer = nodo.derecha.accept(self)
        return valorIzq > valorDer
    
    def visit_MayorIgualQue(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return valorIzq >= valorDer
    
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
        valorDer = nodo.derecha.accept(self)
        return valorIzq <= valorDer
    
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
        return not valor
    
    def visit_Xor(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return (valorIzq and not valorDer) or (not valorIzq and valorDer)

    def visit_Println(self, nodo: Nodo):
        valor = nodo.expresion.accept(self)
        self.Arbol.Print(str(valor))
        return None