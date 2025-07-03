from backend.src.Interprete.nodes.Nodo import Nodo

class Visitor:
    def default_visit(self):
        for atributo, valor in vars(nodo).items():
            if isinstance(valor, Nodo):
                valor.accept(self)
            elif isinstance(valor, list):
                for item in valor:
                    if isinstance(item, Nodo):
                        item.accept(self)
