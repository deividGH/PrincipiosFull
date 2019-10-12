import abc
from abc import ABCMeta

#sustitucion de liscov
#open/close
#reponsabilidad unica


class CasaBD(object):
    nombre = ""
    def GuardarDato(self, nombre):
        self.nombre = nombre

    def EliminarDato(self):
        self.nombre = ""


class Casa(object):
    __metaclass__ = ABCMeta
    __nombre = ""

    def __init__(self,nombre):
        self.__marca = nombre

    def getNombre(self):
        return  self.__nombre


    @abc.abstractmethod
    def precioMedioCasa(self):
        pass


class CasaQuinta(Casa):
    def __init__(self):
        super().__init__('Casa Quinta')

    def precioMedioCasa(self):
        return 700000000


class Finca(Casa):
    def __init__(self):
        super().__init__('Finca')

    def precioMedioCasa(self):
        return 300000000


class Apartamento(Casa):
    def __init__(self):
        super().__init__('Apartamento')

    def precioMedioCasa(self):
        return 200000000

def imprimirCasa(arrayCasas):
    for i in arrayCasas:
        print(str(i.precioMedioCasa())+" "+i.getNombre())

arrayCasas = [ CasaQuinta(), Finca(), Apartamento() ]
imprimirCasa(arrayCasas);




