# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on noppapeli Yatzyn digitaalinen versio. Sovelluksessa käyttäjä voi pelata Yatzy peliä ystäväänsä vastaan.

## Käyttäjät
Ainakin alkuun pelissä tulee olemaan vain yhden tasoisa käyttäjiä; normaaleja pelaajia. Sovellukseen ei kirjauduta erikseen sisään käyttäjätunnuksella.

## Perusversion tarjoama toiminnalisuus  

Huom! GUI merkintä tarkoittaa, että kyseinen toiminnalisuus toimii myös graafisessa käyttöliittymässä

- [x] Kaksi käyttäjää voi aloittaa uuden pelin
    - [x] GUI
- [x] Käyttäjät syöttävät pelikohtaiset nimimerkit
    - [x] GUI
- Peli noudattaa pääsääntöisesti näitä Yatzyn sääntöjä: https://en.wikipedia.org/wiki/Yahtzee#Rules
    - [x] Poikkeuksena ensimmäisessä versiossa edetään pöytäkirjaa järjestyksessä rivi riviltä
        - [x] GUI
- Pelissä voi:
    - [x] Pelata pöytäkirjan "yläkerrassa" olevia rivejä
        - [x] GUI
    - [x] Saada bonouspisteet "yläkerran" pelaamisen jälkeen
        - [x] GUI
    - [x] Pelata pöytäkirjan "alakerrassa" olevia rivejä
        - [x] GUI
- [x] Omalla vuorollaan pelaaja valitsee mitkä nopat haluaa pitää ja mitkä heittää uudestaan
    - [ ] GUI
- [x] Jokaisen vuoron jälkeen pelaajille näytetään päivitetty pistetilanne
    - [x] GUI
- [x] Pelin lopuksi näytetään lopullinen pistetilanne
    - [ ] GUI
- [x] Pelin lopuksi julistetaan voittaja
    - [x] GUI
- [ ] Pelillä on selkeä graafinen käyttöliittymä, jolla edellä mainitut toiminnallisuudet toteutetaan
    - Graafisessa käyttöliittymässä kolme näkymää
        - [x] Start
        - [x] Game
        - [x] End
        - [ ] Ja siirtyminen näiden välillä toimii


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