#SE DEFINE LA CLASE BASE NODO
class Nodo:
    #ESTE CLASE ES LA BASE PARA TODOS LOS NODOS DEL AST
    def __init__(self, tipo=None):
        self.tipo = tipo
    
    #PROPORCIONA EL MÉTODO ACCEPT(self, visitor) QUE PERMITE A LOS VISITANTES RECORRER EL AST
    #BASICAMENTE, EL accept RECIBE LA VISITA DEL OBJETO visitor
    def accept(self, visitor):
        metodo_visitor = 'visit_' + self.__class__.__name__
        visitar = getattr(visitor, metodo_visitor, None)
        if visitar is None:
            visita = visitor.default_visit
            raise Exception(f"El visitante no tiene un método para visitar {self.__class__.__name__}")
        return visitar(self)