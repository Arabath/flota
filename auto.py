""" 
 ✅ Las motos poseen un tanque de 11 litros y tienen una autonomía de 20 km por litro. Pueden llevar
        cargas de hasta 2 kg.

"""

class Auto():
    """ 
    pass
    """
    def __init__(self) -> None:
        self.__tanque = 45
        self.__autonomia = 10
        self.__carga = 250

    @property
    def tanque(self): return self.__tanque
    @property
    def autonomia(self): return self.__autonomia
    @property
    def carga(self): return self.__carga


    def distanciaMaxima(self) -> int:
        """ Devuelve la distancia maxima que recorre el vehiculo """
        return self.tanque * self.autonomia

    def consumoNaftaDistancia(self) -> int:
        """ Devuelve cuanto consume el vehiculo cada 100 km """    
        return self.distanciaMaxima() / 100