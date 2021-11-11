import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kortille_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_rahan_ottaminen_kortilta_toimii_oikein(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_saldo_ei_muutu_jos_kortilla_ei_katetta(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_ota_rahaa_palauttaa_true_jos_rahat_riittaa(self):
        self.assertTrue(self.maksukortti.ota_rahaa(5))

    def test_ota_rahaa_palauttaa_false_jos_rahat_riittaa(self):
        self.assertFalse(self.maksukortti.ota_rahaa(100))