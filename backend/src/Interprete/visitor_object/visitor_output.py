from backend.src.Interprete.visitor_object.visitorBase import Visitor
from backend.src.Interprete.nodes.Nodo import Nodo
from backend.src.Interprete.simbol.RaizArbol import Arbol

class Visitor_Output(Visitor):
    def __init__(self, Arbol: Arbol):
        self.Arbol = Arbol
    
    # VISITA UN NÚMERO Y DEVUELVE SU VALOR
    def visit_Numero(self, nodo: Nodo):
        return nodo.valor

    def visit_Suma(self, nodo: Nodo):
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        return valorIzq + valorDer

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

    def visit_Println(self, nodo: Nodo):
        valor = nodo.expresion.accept(self)
        self.Arbol.Print(str(valor))
        return None