# Arkkitehtuuri

## Luokkakaavio
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/luokkakaavio.png?raw=true" width="500">

## Pakkauskaavio
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/pakkauskaavio.png?raw=true" width="500">

## Käyttöliittymä
Sovelluksen ja käyttäjän vuorovaikutus tapahtuu graafisen käyttöliittymän avulla. Sovelluslogiikka on eriytetty käyttöliittymästä joten luokka käyttöliittymä käyttää [GameService](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/services/game_service.py) luokan (sovelluslogiikka tässä luokassa) funktioita ja metodeja.  
Käyttöliittymä koostuu kolmesta näkymästä ja luokka [UI](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/ui/ui.py) on vastuussa niiden näyttämisestä/vaihtamisesta:
- [Aloitusnäkymä](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/ui/start_view.py)
    - Näkymässä pelaajat (1-4) syöttävät omat nimimerkkinsä jonka jälkeen peli voidaan käynnistää kyseisestä näkymästä.  
    - Näkymässä näytetään myös top 5 korkeimmat pisteet, mitä pelaajat ovat saavuttaneet.
- [Pelinäkymä](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/ui/game_view.py)
    - Pelaaminen tapahtuu tässä näkymässä. Pelaajat pelaavat peliä tässä näkymässä ja pelaajille näytetään sen hetkinen pelin tilanne (pisteet, kenen vuoro, heittojen määrä jne.)
- [Loppunäkymä](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/ui/end_view.py)
    - Kun peli on loppunut siirrytään tähä näkymään.  
    - Voittaja ja hänen pisteet julistetaan sekä näytetään lopullinen pistetilanne.

Näiden näkymien lisäksi on vielä luokka [Scoreboard](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/ui/scoreboard.py), jota käytetään pistetilanteen/taulukon näyttämiseen. Eriytetty omaksi luokaseen, koska sitä käytetään useammassa kuin yhdessä näkymässä.  

## Sovelluslogiikka
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/luokkakaavio.png?raw=true" width="500">

## Toiminnallisuudet
### Pelin käynnistäminen  
Alla oleva sekvenssikaavio kuvaa kuinka kaksi pelaajaa lisätään uuteen peliin.
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/start_game_sekvenssi.png?raw=true" width="500">