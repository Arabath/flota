import unittest
from flota import Flota
from moto import Moto
from auto import Auto
from utilitario import Utilitario


class TestFlota(unittest.TestCase):
    def setUp(self):
        self.flota = Flota()
        self.moto = Moto()
        self.auto = Auto()
        self.utilitario = Utilitario()


    def test_seAgregaUnVehiculoAUnaFlotaVacia(self):
        """ Se agrega un vehiculo a la flota vacia """
    
        self.assertListEqual(self.flota.vehiculos, [])
        
        self.flota.agregar = self.moto
        
        self.assertListEqual(self.flota.vehiculos, [self.moto])

    def test_seAgregaUnVehiculoAUnaFlotaConVehiculos(self):
        """ Se agrega un vehiculo a la flota vacia """
      
        self.flota.agregar = self.moto

        self.assertListEqual(self.flota.vehiculos, [self.moto])
        
        self.flota.agregar = self.auto
        
        self.assertListEqual(self.flota.vehiculos, [self.moto, self.auto])

    def test_unVehiculoEsAdmisibleParaCarga(self):
        """ Se verifica el método admisiblesParaCarga """

        self.flota.agregar = self.moto
        self.flota.agregar = self.auto
        self.flota.agregar = self.utilitario

        self.assertListEqual(self.flota.vehiculos, [self.moto,self.auto,self.utilitario])
        
        self.assertListEqual(self.flota.paraTransportar(1), [self.moto,self.auto,self.utilitario])

        self.assertListEqual(self.flota.paraTransportar(5), [self.auto,self.utilitario])
        
        self.assertListEqual(self.flota.paraTransportar(260), [self.utilitario])

        # self.assertListEqual(self.flota.paraTransportar(450), [])

    def test_vehiculosAptosParaRecorrerUnaDistanciaDe220km(self):
        """ Vehiculos para una distancia de 220km  """
        self.flota.agregar = self.moto
        self.flota.agregar = self.auto
        self.flota.agregar = self.utilitario

        vehiculos = self.flota.paraRecorrer(220)
        
        self.assertListEqual(vehiculos, [self.moto, self.auto, self.utilitario])

if __name__ == '__main__':
    unittest.main()