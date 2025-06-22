from backend.src.Interprete.simbol.Simbolo import Symbol

class Vector(Symbol):
    def __init__(self, name, entity_type, data_type, value, scope, dimensions, line, column):
        super().__init__(name, entity_type, data_type, value, scope, line, column)
        self.dimensions = dimensions
