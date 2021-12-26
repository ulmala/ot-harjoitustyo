# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on noppapeli Yatzyn digitaalinen versio. Sovelluksessa käyttäjä voi pelata Yatzy peliä ystäviään vastaan.

## Käyttäjät
Sovelluksessa on vain yhdentasoisisa käyttäjiä; normaaleja pelaajia. Sovellukseen ei kirjauduta erikseen sisään käyttäjätunnuksella.

## Perusversion tarjoama toiminnalisuus  

- 1-4 pelaajaa voi aloittaa uuden pelin
- Käyttäjät syöttävät pelikohtaiset nimimerkit
- Peli noudattaa pääsääntöisesti näitä Yatzyn sääntöjä: https://en.wikipedia.org/wiki/Yahtzee#Rules
    - Poikkeuksena, että tässä sovelluksessa pistetaulua pelataan järjestyksessä rivi riviltä
    - Käyttöliittyymässä on linkki, joka avaa kyseisen sivun selaimeen
- Sovelluksen pistetaulu sisältää pistetaulun "yläkerran", "alakerran" sekä bonuskierroksen
- Pelissä näytetään koko ajan mitä riviä milläkin hetkellä heitetään
- Omalla vuorollaan pelaaja valitsee mitkä nopat haluaa pitää ja mitkä heittää uudestaan
- Pelaajalle näytetään koko ajan monta heittoa hänellä on jäljellä
- Pelaajille näytetään koko ajan päivittyvä pistetilanne
- Pelin lopuksi julistetaan voittaja ja näytetään lopullinen pistetilanne
- Pelin tulokset (pistetaulu, voittaja, voittajan pisteet) tallennetaan pelin lopuksi tietokantaan
    - Pelin aloitusnäkymässä näkyy top 5 korkeimmat pisteet ja pelaajat
- Edellä kuvatut toiminnallisuudet toteutettu graafisella käyttöliittymällä, jolla kolme perusnäkymää:
    - Aloitusnäkymä
    - Pelinäkymä
    - Loppunäkymä
  
## Käyttöliittymä

### Aloitusnäkymä
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/käyttöohje/start_view_2.png?raw=true" width="500">

### Pelinäkymä

<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/käyttöohje/in_game.png?raw=true" width="500">

### Loppunäkymä
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/käyttöohje/game_end.png?raw=true" width="500">

## Jatkokehitysideoita
- pelaaja voi valita mitä pöytäkirjan riviä heittää
- käyttäjien rekisteröiminen
- mahdollisuus selata omaa pelihistoriaa ja tilastoja
- mahdollisuus pelata tekoälyä vastaan