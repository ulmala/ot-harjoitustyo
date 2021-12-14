# Yatzy
 Sovellus on Yatzy peli, jossa pelaajat voivat pelata Yatzya toisiaan vastaan.  
 Viimeisimmän version voi ladata [täältä](https://github.com/ulmala/ot-harjoitustyo/releases/tag/viikko6)  
 Aikaisemmat releaset:
 - [Viikko 5](https://github.com/ulmala/ot-harjoitustyo/releases/tag/viikko5)

 ## Python versio
 Sovellus on testattu toimivaksi Python 3.8 versiolla.


## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)  
- [Tuntikirjanpito](https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)  
- [Arkkitehtuuri](https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)  


## Asennusohjeet

1. Riippuvuuksien asennus

```bash
poetry install
```

2. Sovelluksen käynnistäminen

```bash
poetry run invoke start
```

## Testaus

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