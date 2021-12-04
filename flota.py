from moto import Moto
from vehiculo import Vehiculo
from excepcion import NoHayVehiculosDisponibles

class Flota():
    """ pass """
    def __init__(self): 
        self.__vehiculos = []

    @property
    def vehiculos(self): return self.__vehiculos 
    @vehiculos.setter
    def agregar(self, un_vehiculo):
        self.__vehiculos.append(un_vehiculo)

    
    def __filter(self, func) -> list[Vehiculo]:
        """ Filtra una coleccion por medio de un criterio """
        vehiculos = list(filter(func, self.vehiculos))
        if vehiculos: return vehiculos
        else: raise NoHayVehiculosDisponibles
    
    def paraTransportar(self, carga: int) -> list[Vehiculo]:
        """ Retornar la coleccion de vehiculos admisibles 
            para transportar una carga """
        return self.__filter(lambda vehiculo: vehiculo.carga >= carga)

    def paraRecorrer(self, una_distancia: int) -> list[Vehiculo]:
        """ Retornar la coleccion de vehiculos admisibles 
            para recorrer una distancia """
        return self.__filter(lambda vehiculo: vehiculo.distanciaMaxima() >= una_distancia)

    def laCantidadDeMotos(self) -> int:
        """ Devuelve la cantidad de motos que contiene """
        return len(self.__filter(lambda vehiculo: isinstance(vehiculo, Moto)))

    
    def vehiculoOptimo(self, una_carga: int, una_distancia: int) -> Vehiculo:
        """ pass """
        vehiculos_carga = self.paraTransportar(una_carga)
        vehiculos_distancia = self.paraRecorrer(una_distancia)
        vehiculos = set(vehiculos_carga) & set(vehiculos_distancia)
        vehiculo_optimo, *resto = tuple(sorted(vehiculos, key=Vehiculo.consumoCada100))     #  (auto, moto, utilitario)  => (moto, auto, utilitario)
        return vehiculo_optimo
        # vehiculos_ordenados = list(sorted(vehiculos, key=Vehiculo.consumoCada100))
        # return vehiculos_ordenados[0]



if __name__ == '__main__':
    flota = Flota()
    moto1 = Moto()
    moto2 = Moto()
    moto3 = Moto()

    flota.agregar = moto1
    flota.agregar = moto2
    flota.agregar = moto3

    print(flota.laCantidadDeMotos())
    # print(flota.vehiculos)