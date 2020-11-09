/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.unicafe;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author ulmaa
 */
public class KassapaateTest {
    
    Kassapaate kassapaate;
    Maksukortti kortti;
    
    public KassapaateTest() {
    }
    
    @Before
    public void setUp() {
        kassapaate = new Kassapaate();
        kortti = new Maksukortti(1000);
    }

    @Test
    public void alussaOikeaMaaraRahaa() {
        assertEquals(100000, kassapaate.kassassaRahaa());      
    }
    
    @Test
    public void alussaOikeaMaaraEdullisia() {
        assertEquals(0, kassapaate.edullisiaLounaitaMyyty());
    }
    
    @Test 
    public void alussaOikeaMaaraMaukkaita() {
        assertEquals(0, kassapaate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void edullisenLounaanKateisostoToimii() {
        int vaihtorahat = kassapaate.syoEdullisesti(240);
        assertEquals(0, vaihtorahat);
        assertEquals(1, kassapaate.edullisiaLounaitaMyyty());
        assertEquals(100240, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void maukkaanLounaanKateisostoToimii() {
        int vaihtorahat = kassapaate.syoMaukkaasti(400);
        assertEquals(0, vaihtorahat);
        assertEquals(1, kassapaate.maukkaitaLounaitaMyyty());
        assertEquals(100400, kassapaate.kassassaRahaa());
    }
    
    
    @Test
    public void eiRiittavastiRahaaEdulliseen() {
        int vaihtorahat = kassapaate.syoEdullisesti(100);
        assertEquals(100000, kassapaate.kassassaRahaa());
        assertEquals(100, vaihtorahat);
        assertEquals(0, kassapaate.edullisiaLounaitaMyyty());
    }
    
    @Test
    public void eiRiittavastiRahaaMaukkaaseen() {
        int vaihtorahat = kassapaate.syoMaukkaasti(100);
        assertEquals(100000, kassapaate.kassassaRahaa());
        assertEquals(100, vaihtorahat);
        assertEquals(0, kassapaate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void edullisenLounaanKorttiostoToimii() {
        assertTrue(kassapaate.syoEdullisesti(kortti));
        assertEquals(1, kassapaate.edullisiaLounaitaMyyty());
    }
    
    @Test
    public void kortillaEiRiittavastiEdulliseen() {
        kortti = new Maksukortti(100);
        assertFalse(kassapaate.syoEdullisesti(kortti));
        assertEquals(0, kassapaate.edullisiaLounaitaMyyty());
    }
    
    @Test
    public void kassaOikeinEdullisenKorttiostonJalkeen() {
        kassapaate.syoEdullisesti(kortti);
        assertEquals(100000, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void maukkaanLounaanKorttiostoToimii() {
        assertTrue(kassapaate.syoMaukkaasti(kortti));
        assertEquals(1, kassapaate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void kortillaEiRiittavastiMaukkaaseen() {
        kortti = new Maksukortti(100);
        assertFalse(kassapaate.syoMaukkaasti(kortti));
        assertEquals(0, kassapaate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void kassaOikeinMaukkaanKorttiostonJalkeen() {
        kassapaate.syoMaukkaasti(kortti);
        assertEquals(100000, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void kortinLatausToimii() {
        kassapaate.lataaRahaaKortille(kortti, 100);
        assertEquals(100100, kassapaate.kassassaRahaa());
    }
    
    @Test
    public void alaLataaNegatiivistaRahaaKortille() {
        kassapaate.lataaRahaaKortille(kortti, -1);
        assertEquals(100000, kassapaate.kassassaRahaa());
    }
}
/*

korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
    jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan true
    jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
    jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan false
    kassassa oleva rahamäärä ei muutu kortilla ostettaessa
kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
*/
