import unittest
from auto import Auto

class TestMoto(unittest.TestCase):
    def setUp(self):
        self.auto = Auto()

    def test_DistanciaMaximaQuePuedeRecorrerUnaMoto(self):
        """ Test del método distanciaMaxima() """

        self.assertEqual(self.auto.distanciaMaxima(), 450)
    
    def test_ConsumoDeNaftaCada100Kms(self):
        """ Test del método consumoNaftaDistancia() """

        self.assertEqual(self.auto.consumoNaftaDistancia(), 4.5)
