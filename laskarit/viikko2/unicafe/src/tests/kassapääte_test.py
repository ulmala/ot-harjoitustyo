import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_konstruktori_asettaa_pohjakassan_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_alussa_maukkaita_nolla_kappaletta(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_alussa_edullisia_nolla_kappaletta(self):
        self.assertEqual(self.kassapaate.edulliset, 0)    

    def test_syo_edullisesti_kateisella_kasvattaa_kassaa_ja_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 240)

    def test_syo_maukkaasti_kateisella_kasvattaa_kassaa_ja_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 400)

    def test_edullisten_maara_kasvaa_jos_kateinen_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaiden_maara_kasvaa_jos_kateinen_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_toimii_oikein_jos_ei_riittavasti_rahaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_toimii_oikein_jos_ei_riittavasti_rahaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_osto_kortilla_toimii(self):
        onnistui = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(onnistui)
        self.assertEqual(self.maksukortti.saldo, 1000-240)

    def test_maukkaan_osto_kortilla_toimii(self):
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(onnistui)
        self.assertEqual(self.maksukortti.saldo, 1000-400)

    def test_edullisten_maara_kasvaa_jos_kortilla_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaiden_maara_kasvaa_jos_kortilla_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_toimii_oikein_jos_kortilla_ei_saldoa(self):
        maksukortti = Maksukortti(1)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertFalse(onnistui)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(maksukortti.saldo, 1)

    def test_maukas_toimii_oikein_jos_kortilla_ei_saldoa(self):
        maksukortti = Maksukortti(1)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertFalse(onnistui)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(maksukortti.saldo, 1)

    def test_kassan_rahamaara_ei_muutu_kun_ostaa_kortilla_edullisen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_rahamaara_ei_muutu_kun_ostaa_kortilla_maukkaan(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_saldo_muuttuu_kun_lataa_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 1100)
    
    def test_kassapaatteen_rahamaara_kasvaa_kun_lataa_kortille_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 100)

    def test_kassapaate_palauttaa_none_jos_lataa_kortille_negatiivisen(self):
        self.assertIsNone(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1))