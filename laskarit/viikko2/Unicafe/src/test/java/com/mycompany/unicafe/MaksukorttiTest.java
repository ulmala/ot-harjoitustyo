package com.mycompany.unicafe;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class MaksukorttiTest {

    Maksukortti kortti;

    @Before
    public void setUp() {
        kortti = new Maksukortti(1000);
    }

    @Test
    public void luotuKorttiOlemassa() {
        assertTrue(kortti!=null);      
    }
    
    @Test
    public void kortinSaldoAlussaOikein() {
        assertEquals("saldo: 10.0", kortti.toString());
    }
    
    @Test
    public void rahanLataaminenKasvattaaSaldoaOikein() {
        kortti.lataaRahaa(100);
        assertEquals("saldo: 11.0", kortti.toString());
    }
    
    @Test
    public void otaRahaaToimiiJosTarpeeksiSaldoa() {
        kortti.otaRahaa(5);
        assertEquals("saldo: 9.95", kortti.toString());
    }
    
    @Test
    public void saldoEiMuutuJosRahaaEiOleTarpeeksi() {
        kortti.otaRahaa(2000);
        assertEquals("saldo: 10.0", kortti.toString());
    }
    
    @Test
    public void palauttaaTrueJosRahanOttaminenOnnistui() {
        assertTrue(kortti.otaRahaa(5));
    }
    
    @Test
    public void palauttaaFalseJosEiRiittävästiRahaa() {
        assertFalse(kortti.otaRahaa(2000));
    }
    
    @Test
    public void palauttaaOikeanSaldon() {
        assertEquals(1000, kortti.saldo());
    }
}
