# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on noppapeli Yatzyn digitaalinen versio. Sovelluksessa käyttäjä voi pelata Yatzy peliä ystäväänsä vastaan.

## Käyttäjät
Ainakin alkuun pelissä tulee olemaan vain yhden tasoisa käyttäjiä; normaaleja pelaajia. Sovellukseen ei kirjauduta erikseen sisään käyttäjätunnuksella.

## Perusversion tarjoama toiminnalisuus  

- Kaksi käyttäjää voi aloittaa uuden pelin
- Käyttäjät syöttävät pelikohtaiset nimimerkit
- Peli noudattaa pääsääntöisesti näitä Yatzyn sääntöjä: https://en.wikipedia.org/wiki/Yahtzee#Rules
    - Poikkeuksena ensimmäisessä versiossa edetään pöytäkirjaa järjestyksessä rivi riviltä
- Omalla vuorollaan pelaaja valitsee mitkä nopat haluaa pitää ja mitkä heittää uudestaan
- Jokaisen vuoron jälkeen pelaajille näytetään päivitetty pistetilanne
- Pelin lopuksi näytetään lopullinen pistetilanne
- Pelin lopuksi julistetaan voittaja
- Pelillä on graafinen käyttöliittymä, jolla edellä mainitut toiminnallisuudet toteutetaan

## Käyttöliittymäluonnos

### Aloitusnäkymä
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/start.png?raw=true" width="500">

### Pelinäkymä

<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/play.png?raw=true" width="500">

### Loppunäkymä
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/end.png?raw=true" width="500">

## Jatkokehitysideoita
- tuki N pelaajalle
- käyttäjien rekisteröiminen
- mahdollisuus selata omaa pelihistoriaa ja tilastoja
- tilasto parhaista pelaajista
- mahdollisuus pelata tekoälyä vastaan