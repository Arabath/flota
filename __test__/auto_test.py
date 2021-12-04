import unittest
from auto import Auto

class TestMoto(unittest.TestCase):
    def setUp(self) -> None:
        self.auto = Auto()
        
    def test_alCrearUnAutoSuVelocidadEsCero(self):
        """ Al instanciar la clase auto el mismo se encuentra parado """
        self.assertEqual(self.auto.velocidad, 0)
        
    def test_elAutoPuedeAcelerarUnaVelocidad(self):
        """ El auto puede ser acelerado """
        self.assertEqual(self.auto.velocidad, 0)
        
        self.auto.acelerar(100)
        
        self.assertEqual(self.auto.velocidad, 100)
        
    def test_alAcelerarElAutoLaVelocidadSeSuma(self):
        """ La velocidad de aceleración se suma a la velocidad actual del auto """
        self.auto.acelerar(20)
        
        self.assertEqual(self.auto.velocidad, 20)
        
        self.auto.acelerar(100)
        
        self.assertEqual(self.auto.velocidad, 120)
     
    def test_elAutoPuedeDetenerse(self):
        """ El auto puede ser detenido, se velocidad se reducira a 0 """
        self.auto.acelerar(100)
        
        self.assertEqual(self.auto.velocidad, 100)
        
        self.auto.detenerse()
     
        self.assertEqual(self.auto.velocidad, 0)
        
    def test_elAutoEstaEnMovimiento(self):
        """ El auto se encuentra en movimiento """  
        self.assertFalse(self.auto.estaEnMovimiento())
        self.assertEqual(self.auto.velocidad, 0)
        
        self.auto.acelerar(10)
        
        self.assertTrue(self.auto.estaEnMovimiento())
        self.assertEqual(self.auto.velocidad, 10)

    def test_DistanciaMaximaQuePuedeRecorrerUnaMoto(self):
        """ Test del método distanciaMaxima() """

        self.assertEqual(self.auto.distanciaMaxima(), 450)
    
    def test_ConsumoDeNaftaCada100Kms(self):
        """ Test del método consumoNaftaDistancia() """

        self.assertEqual(self.auto.consumoCada100(), 10)
