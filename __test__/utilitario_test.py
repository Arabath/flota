import unittest
from utilitario import Utilitario

class TestMoto(unittest.TestCase):
    def setUp(self):
        self.utilitario = Utilitario()

    def test_DistanciaMaximaQuePuedeRecorrerUnaMoto(self):
        """ Test del método distanciaMaxima() """

        self.assertEqual(self.utilitario.distanciaMaxima(), 540)
    
    def test_ConsumoDeNaftaCada100Kms(self):
        """ Test del método consumoNaftaDistancia() """

        self.assertEqual(self.utilitario.consumoNaftaDistancia(), 5.4)
