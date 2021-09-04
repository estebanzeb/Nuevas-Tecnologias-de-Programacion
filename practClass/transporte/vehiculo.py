class Vehiculo:
    __nromotor = ""
    __nroruedas = 0
    __nroasientos = 0 

    def __init__(self, nromotor, nroruedas, nroasientos):
        self.__nromotor = nromotor
        self.__nroruedas = nroruedas
        self.__nroasientos = nroasientos

    def GetNromotor(self):
        return self.__nromotor

    def SetNromotor(self, nromotor):
        self.__nromotor = nromotor

    def GetNroruedas(self):
        return self.__nroruedas

    def SetNroruedas(self, nroruedas):
        self.__nroruedas = nroruedas

    def GetNroasientos(self):
        return self.__nroasientos

    def SetNromasientos(self, nroasientos):
        self.__nroasientos = nroasientos

    def arrancar(self):
        if self.__nroruedas<=2:
            print("El vehiculo ha arrancado")
        else:
            print("El vehiculo no puede arrancar")

    def acelerar(self):
        print("Acelerando el vehiculo")