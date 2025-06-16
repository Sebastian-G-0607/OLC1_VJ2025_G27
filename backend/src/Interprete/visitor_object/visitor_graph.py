from backend.src.Interprete.visitor_object.visitorBase import Visitor
from backend.src.Interprete.nodes.Nodo import Nodo

class VisitorGraph(Visitor):
    def __init__(self, Arbol):
        self.Arbol = Arbol
        self.dot = []
        self.counter = 0

        self.dot.append('digraph G {')
        self.dot.append('node [shape=ellipse];')

    # VISITA UN NÚMERO Y DEVUELVE SU VALOR
    def visit_Nativo(self, nodo: Nodo):
        codigo = f'node{self.counter} [label="{nodo.valor}""];'
        self.counter += 1
        return codigo

    def visit_Suma(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)
        #SE DEFINE EL NODO RAIZ DE LA SUMA
        raiz = f'node{self.counter} [label="+"];'
        #SE RETORNA EL CÓDIGO DE LA SUMA
        codigo = raiz + '\n'
        codigo += f'node{self.counter} -> {valorIzq};\n'
        codigo += f'node{self.counter} -> {valorDer};\n'
        self.counter += 1
        return codigo
    
    def visit_Println(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DEL NODO
        valor = nodo.valor.accept(self)
        #SE DEFINE EL NODO RAIZ DEL PRINTLN
        raiz = f'node{self.counter} [label="Println"];'
        #SE RETORNA EL CÓDIGO DEL PRINTLN
        codigo = raiz + '\n'
        codigo += f'node{self.counter} -> {valor};\n'
        self.counter += 1
        return codigo