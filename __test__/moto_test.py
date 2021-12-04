import unittest
from moto import Moto

class TestMoto(unittest.TestCase):
    def setUp(self):
        self.moto = Moto()

    def test_DistanciaMaximaQuePuedeRecorrerUnaMoto(self):
        """ Test del método distanciaMaxima() """

        self.assertEqual(self.moto.distanciaMaxima(), 220)
    
    def test_ConsumoDeNaftaCada100Kms(self):
        """ Test del método consumoNaftaDistancia() """

        self.assertEqual(self.moto.consumoNaftaDistancia(), 2.2)
