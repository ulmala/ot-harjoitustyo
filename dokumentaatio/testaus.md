# Testausdokumentti

## Yksikkö- ja integraatiotestaus

Sovellus- ja pelilogiikan testaamisesta on vastuussa luokka `GameServiceTest`, jolle injektoidaan testauksen alussa luokka `Game` ja peliin lisätään kaksi pelaajaa. Joissain testeissä pelin pelaaja määrää muokataan testiä varten. Kun halutaan testata tiettyä pelin tilannetta, `Game`luokan oliota muokataan kyseisessä testissä testattavaa tilannetta varten.  

Pisteiden tarkistuksen testaamisesta vastuussa on luokka `PointCheckerTest`, jolle injektoidaan testaamista varten luokkien `GameService` ja `Game`oliot.  

### Testauskattavuus

Sovelluksen testauksen haaraumakattavuus on 91% (poislukien käyttöliittymä).  

<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/coverage_report.png?raw=true" width="500">

Täysi testaaminen puuttuu vielä `GameRepository`luokalta sekä `initialize_db`tiedostolta.  

## Järjestelmätestaus

Sovelluksen asennus on testattu macOS- ja Linux ympäristössä. Asennus on tehty noudattaen sovelluksen [käyttöohjeita](https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/käyttöohje.md).  

Kaikkia sovelluksen toiminnallisuuksia on testattu manuaalisesti ja yritetty löytää käyttöliittymästä bugeja. Tällä hetkellä käyttöliittymän kautta ei pitäisi pystyä syöttämään mitään sellaista mikä kaataisi sovelluksen.