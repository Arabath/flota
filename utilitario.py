""" 
 ✅ Las motos poseen un tanque de 11 litros y tienen una autonomía de 20 km por litro. Pueden llevar
        cargas de hasta 2 kg.

"""
from vehiculo import Vehiculo


class Utilitario(Vehiculo):
    """ 
    pass
    """
    def __init__(self) -> None:
        super().__init__(60,9,400)


        
if __name__ == '__main__':
    utilitario = Utilitario()
    print(utilitario.consumoCada100())

