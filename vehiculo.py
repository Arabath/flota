from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """ """
    @abstractmethod
    def __init__(self, tanque:int, autonomia:int, carga:int) -> None:
        self.__tanque = tanque
        self.__autonomia = autonomia
        self.__carga = carga

    @property
    def tanque(self): return self.__tanque
    @property
    def autonomia(self): return self.__autonomia
    @property
    def carga(self): return self.__carga


    def distanciaMaxima(self) -> int:
        """ Devuelve la distancia maxima que recorre el vehiculo """
        return self.tanque * self.autonomia

    def consumoCada100(self) -> int:
        """ Devuelve cuantos litros consume el vehiculo cada 100 km """    
        return 100 / self.__autonomia

if __name__ == '__main__':
    vehiculo = Vehiculo(2,4,6)
    