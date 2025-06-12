
class Arbol:
    def __init__(self, instrucciones):
        self.__instrucciones = instrucciones
        self.__consola = ""
        self.__errores = []

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

    def setErrores(self, errores):
        self.__errores = errores

    def Print(self, mensaje: str):
        self.__consola += mensaje + "\n"

    def AddErrores(self, errores):
        self.__errores.append(errores)