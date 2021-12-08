from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """ Clase abstracta de un vehiculo cualquiera """
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

    def vehiculoEconomico(self) -> 
if __name__ == '__main__':
    
    C:\Python39\Scripts
    