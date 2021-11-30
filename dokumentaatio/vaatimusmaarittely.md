# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on noppapeli Yatzyn digitaalinen versio. Sovelluksessa käyttäjä voi pelata Yatzy peliä ystäväänsä vastaan.

## Käyttäjät
Ainakin alkuun pelissä tulee olemaan vain yhden tasoisa käyttäjiä; normaaleja pelaajia. Sovellukseen ei kirjauduta erikseen sisään käyttäjätunnuksella.

## Perusversion tarjoama toiminnalisuus  

- [x] Kaksi käyttäjää voi aloittaa uuden pelin
- [x] Käyttäjät syöttävät pelikohtaiset nimimerkit
- Peli noudattaa pääsääntöisesti näitä Yatzyn sääntöjä: https://en.wikipedia.org/wiki/Yahtzee#Rules
    - [x] Poikkeuksena ensimmäisessä versiossa edetään pöytäkirjaa järjestyksessä rivi riviltä
- Pelissä voi:
    - [x] Pelata pöytäkirjan "yläkerrassa" olevia rivejä
    - [x] Saada bonouspisteet "yläkerran" pelaamisen jälkeen
    - [x] Pelata pöytäkirjan alakerrassa olevia rivejä
- [x] Omalla vuorollaan pelaaja valitsee mitkä nopat haluaa pitää ja mitkä heittää uudestaan
- [x] Jokaisen vuoron jälkeen pelaajille näytetään päivitetty pistetilanne
- [x] Pelin lopuksi näytetään lopullinen pistetilanne
- [x] Pelin lopuksi julistetaan voittaja
- [ ] Pelillä on graafinen käyttöliittymä, jolla edellä mainitut toiminnallisuudet toteutetaan

## Käyttöliittymäluonnos

### Aloitusnäkymä
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/start.png?raw=true" width="500">

### Pelinäkymä

<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/play.png?raw=true" width="500">

### Loppunäkymä
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/end.png?raw=true" width="500">

## Jatkokehitysideoita
- pelaaja voi valita mitä pöytäkirjan riviä heittää
- tuki N pelaajalle
- käyttäjien rekisteröiminen
- mahdollisuus selata omaa pelihistoriaa ja tilastoja
- tilasto parhaista pelaajista
- mahdollisuus pelata tekoälyä vastaan