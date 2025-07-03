class Error: 
    def __init__(self, tipo, descripcion, linea=None, columna = None):
        self.tipo = tipo
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna

    def __str__(self):
        return f"Error {self.tipo} en línea {self.linea}, columna {self.columna}: {self.descripcion}"

    def __repr__(self):
        return f"Error(tipo={self.tipo}, descripcion={self.descripcion}, linea={self.linea}, columna={self.columna})"