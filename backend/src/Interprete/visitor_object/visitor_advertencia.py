from backend.src.Interprete.nodes.Nodo import Nodo
from backend.src.Interprete.nodes.expresiones.AccesoVariable import AccesoVariable
from backend.src.Interprete.simbol.RaizArbol import Arbol
from backend.src.Interprete.visitor_object.visitorBase import Visitor


class Visitor_Advertencia(Visitor):
    def __init__(self, Arbol: Arbol, id):
        self.Arbol = Arbol
        self.id = id

    def visit_Nativo(self, nodo: Nodo):
        return False

    def visit_Argumento(self, nodo: Nodo):
        resultado = nodo.valor.accept(self)
        if resultado is True:
            return True
        return False

    def visit_Asignacion(self, nodo: Nodo):
        if nodo.id == self.id:
            return True
        resultado = nodo.valor.accept(self)
        if resultado is True:
            return True
        return False

    def visit_AsignacionVector(self, nodo: Nodo):
        resultado = nodo.valor.accept(self)
        if resultado is True:
            return True
        return False

    def visit_Break(self, nodo: Nodo):
        return False

    def visit_Case(self, nodo: Nodo):
        resultado = nodo.condicion.accept(self)
        if resultado is True:
            return True
        for instruccion in nodo.instrucciones_case:
            resultado = instruccion.accept(self)
            if resultado is True:
                return True
        return False

    def visit_Continue(self, nodo: Nodo):
        return False

    def visit_Declaracion(self, nodo: Nodo):
        resultado = nodo.valor.accept(self)
        if resultado is True:
            return True
        return False

    def visit_DeclaracionVector(self, nodo: Nodo):
        return False

    def visit_Decremento(self, nodo: Nodo):
        resultado = nodo.variable.accept(self)
        if resultado is True:
            return True
        return False

    def visit_DoWhile(self, nodo: Nodo):
        for instruccion in nodo.instrucciones:
            resultado = instruccion.accept(self)
            if resultado is True:
                return True
        resultado = nodo.condicion.accept(self)
        if resultado is True:
            return True
        return False

    def visit_Else(self, nodo: Nodo):
        for instruccion in nodo.instrucciones:
            resultado = instruccion.accept(self)
            if resultado is True:
                return True
        return False

    def visit_Execute(self, nodo: Nodo):
        for arg in nodo.args:
            resultado = arg.accept(self)
            if resultado is True:
                return True
        return False

    def visit_For(self, nodo: Nodo):
        resultado = nodo.declaracion.accept(self)
        if resultado is True:
            return True
        resultado = nodo.condicion.accept(self)
        if resultado is True:
            return True
        resultado = nodo.actualizacion.accept(self)
        if resultado is True:
            return True
        for instruccion in nodo.instrucciones:
            resultado = instruccion.accept(self)
            if resultado is True:
                return True
        return False

    def visit_If(self, nodo: Nodo):
        resultado = nodo.condicion.accept(self)
        if resultado is True:
            return True
        for instruccion in nodo.instrucciones:
            resultado = instruccion.accept(self)
            if resultado is True:
                return True
        return False

    def visit_IfElse(self, nodo: Nodo):
        resultado = nodo.condicion.accept(self)
        if resultado is True:
            return True
        for instruccion in nodo.instrucciones_if:
            resultado = instruccion.accept(self)
            if resultado is True:
                return True
        for instruccion in nodo.instrucciones_else:
            resultado = instruccion.accept(self)
            if resultado is True:
                return True
        return False

    def visit_IfElseIf(self, nodo: Nodo):
        resultado = nodo.condicion.accept(self)
        if resultado is True:
            return True
        for instruccion in nodo.instrucciones_if:
            resultado = instruccion.accept(self)
            if resultado is True:
                return True
        resultado = nodo.elseif.accept(self)
        if resultado is True:
            return True
        return False

    def visit_Incremento(self, nodo: Nodo):
        resultado = nodo.variable.accept(self)
        if resultado is True:
            return True
        return False

    def visit_ParametroDefinicion(self, nodo: Nodo):
        return False

    def visit_Println(self, nodo: Nodo):
        resultado = nodo.expresion.accept(self)
        return resultado

    def visit_Procedimiento(self, nodo: Nodo):
        return False

    def visit_Switch(self, nodo: Nodo):
        resultado = nodo.expresion.accept(self)
        if resultado is True:
            return True
        for caso in nodo.lista_casos:
            resultado = caso.accept(self)
            if resultado is True:
                return True
        return False

    def visit_While(self, nodo: Nodo):
        resultado = nodo.condition.accept(self)
        if resultado is True:
            return True
        for instruccion in nodo.instructions:
            resultado = instruccion.accept(self)
            if resultado is True:
                return True
        return False

    def visit_AccesoVariable(self, nodo: Nodo):
        if nodo.id == self.id:
            return True
        return False

    def visit_AccesoVector(self, nodo: Nodo):
        return False

    def visit_And(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado

    def visit_Coseno(self, nodo: Nodo):
        resultado = nodo.expresion.accept(self)
        return resultado

    def visit_DiferenteQue(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado

    def visit_Division(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado

    def visit_IgualQue(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado

    def visit_Inversion(self, nodo: Nodo):
        return False

    def visit_MayorIgualQue(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado

    def visit_MayorQue(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado

    def visit_MenorIgualQue(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado

    def visit_MenorQue(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado

    def visit_Modulo(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado

    def visit_Multiplicacion(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado

    def visit_Not(self, nodo: Nodo):
        resultado = nodo.expresion.accept(self)
        return resultado

    def visit_Or(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado

    def visit_Potencia(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado

    def visit_Resta(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado

    def visit_Seno(self, nodo: Nodo):
        resultado = nodo.expresion.accept(self)
        return resultado

    def visit_Shuffle(self, nodo: Nodo):
        return False

    def visit_Sort(self, nodo: Nodo):
        return False

    def visit_Suma(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado

    def visit_Umenos(self, nodo: Nodo):
        resultado = nodo.expresion.accept(self)
        return resultado

    def visit_Xor(self, nodo: Nodo):
        resultado = nodo.izquierda.accept(self)
        if resultado is True:
            return True
        resultado = nodo.derecha.accept(self)
        return resultado