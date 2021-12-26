# Yatzy
 Sovellus on Yatzy peli, jossa pelaajat voivat pelata Yatzya toisiaan vastaan. Pelaaminen tapahtuu graafisen käyttöliittymän kautta. Peli tukee tällä hetkellä 1-4 pelaajaa.  
 ## Releaset
 Viimeisimmän version voi ladata [täältä](https://github.com/ulmala/ot-harjoitustyo/releases/tag/viikko6)  
 Kaikki aikaisemmat releaset löytyvät [täältä](https://github.com/ulmala/ot-harjoitustyo/releases)

 ## Python versio
 Sovellus on testattu toimivaksi Python 3.8 versiolla.


## Dokumentaatio
- [Käyttöohje](https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/käyttöohje.md)
- [Vaatimusmäärittely](https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)  
- [Tuntikirjanpito](https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)  
- [Arkkitehtuuri](https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti]((https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md))  


## Asennusohjeet

1. Riippuvuuksien asennus

```bash
poetry install
```

2. Alusta sovelluksen tarvitsema tietokanta

```bash
poetry run invoke init-db
```

3. Sovelluksen käynnistäminen

```bash
poetry run invoke start
```

## Komentorivitoiminnot

Sovelluksen käynnistäminen (kun edellämainitut asennustoimenpiteet on tehty)

```bash
poetry run invoke start
```

Olemassa olevat testit voidaan suorittaa komennolla  

```bash
poetry run invoke test
```

Ja testikattavuusraportti voidaan luoda (kansio /htmlcov) komennolla  

```bash
poetry run invoke coverage-report
```

Pylint laatutarkistukset voidaan suorittaa komennolla

```bash
poetry run invoke lint
```