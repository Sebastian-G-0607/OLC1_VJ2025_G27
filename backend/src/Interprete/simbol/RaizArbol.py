class Arbol:
    def __init__(self, instrucciones):
        self.__instrucciones = [inst for inst in instrucciones if inst is not None]
        self.__consola = ""
        self.__errores = []
        self.__procedimientos = []

    def getInstrucciones(self):
        return self.__instrucciones

    def setInstrucciones(self, instrucciones):
        self.__instrucciones = instrucciones

    def getConsola(self):
        return self.__consola

    def setConsola(self, consola):
        self.__consola = consola

    def getErrores(self):
        return self.__errores

    def getProcedimientos(self):
        return self.__procedimientos

    def addProcedimiento(self, procedimiento):
        self.__procedimientos.append(procedimiento)

    def findProcedimiento(self, id):
        for procedimiento in self.__procedimientos:
            if procedimiento.id == id:
                return procedimiento
        return None

    def setErrores(self, errores):
        self.__errores = errores

    def Print(self, mensaje: str):
        self.__consola += mensaje + "\n"

    def AddErrores(self, errores):
        self.__errores.append(errores)