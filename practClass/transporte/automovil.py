from transporte.vehiculo import Vehiculo

class Automovil(Vehiculo):
    __guantera = True
    __nropuertas = 0

    def __init__(self, nromotor, nroruedas, nroasientos, guantera, nropuertas):
        Vehiculo.__init__(self, nromotor, nroruedas, nroasientos)
        self.__guantera = guantera
        self.__nropuertas = nropuertas

    def Getguantera(self):
        return self.__guantera

    def SetNromotor(self, guantera):
        self.__guantera = guantera

    def GetNropuertasa(self):
        return self.__nropuertas

    def SetNropuertas(self, nropuertas):
        self.__nropuertas = nropuertas

