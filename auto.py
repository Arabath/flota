""" 
 ✅ Las motos poseen un tanque de 11 litros y tienen una autonomía de 20 km por litro. Pueden llevar
        cargas de hasta 2 kg.

"""
from vehiculo import Vehiculo

class Auto(Vehiculo):
    """ 
        Clase Auto
        
        Metodos:
            ✅ velocidad: representa la velocidad que tiene el auto.
            ✅ acelerar: se puede acelerar el auto.
            ✅ detenerse: detiene el auto a 0km/h.
            ✅ estaEnMovimiento?: responde si el vehiculo se encuentra en movimiento.
            ✅ distanciaMaxima: devuelve la distancia maxima que puede recorrer
                con el tanque lleno.
            ✅ consumoCada100: retorna el consumo cada 100 km.
    """
    def __init__(self) -> None:
        super().__init__(45,10,250)
        self.__velocidad = 0


    @property
    def velocidad(self): return self.__velocidad
    
    def acelerar(self, una_velocidad: int) -> None: 
        """ Acelera el vehicula la velocidad especificada """
        self.__velocidad += una_velocidad
        
    def detenerse(self) -> None:
        """ Detiene el vehiculo """
        self.__velocidad = 0
        
    def estaEnMovimiento(self) -> bool:
        """ Estara en movimiento si su velocidad es mayor a 0 """
        return self.velocidad > 0


  


