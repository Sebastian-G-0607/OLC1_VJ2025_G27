from backend.src.Interprete.nodes.Nodo import Nodo

class While(Nodo):
    _contador = 0  # Contador de instancias de While

    def __init__(self, condition, instructions, line = None, column = None):
        super().__init__(line, column)
        self.condition = condition  # Condición del while
        self.instructions = instructions  # Instrucciones a ejecutar en el bucle
        While._contador += 1
        self.id = While._contador