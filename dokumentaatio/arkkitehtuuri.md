# Arkkitehtuuri

## Rakenne

Sovellus noudattattaa kolmitasoista kerrosarkkitehtuuria:  
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/rakenne.png?raw=true" width="500">

## Käyttöliittymä
Sovelluksen ja käyttäjän vuorovaikutus tapahtuu graafisen käyttöliittymän avulla. Sovelluslogiikka on eriytetty käyttöliittymästä joten luokka käyttöliittymä käyttää [GameService](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/services/game_service.py) luokan (sovelluslogiikka tässä luokassa) funktioita ja metodeja.  
Käyttöliittymä koostuu kolmesta näkymästä ja luokka [UI](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/ui/ui.py) on vastuussa niiden näyttämisestä/vaihtamisesta:
- [Aloitusnäkymä](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/ui/start_view.py)
    - Näkymässä pelaajat (1-4) syöttävät omat nimimerkkinsä jonka jälkeen peli voidaan käynnistää kyseisestä näkymästä.  
    - Näkymässä näytetään myös top 5 korkeimmat pisteet, mitä pelaajat ovat saavuttaneet.  
    - Aloitusnäkymästä pääsee vain ja ainoastaan pelinäkymään.
- [Pelinäkymä](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/ui/game_view.py)
    - Pelaaminen tapahtuu tässä näkymässä. Pelaajat pelaavat peliä tässä näkymässä ja pelaajille näytetään sen hetkinen pelin tilanne (pisteet, kenen vuoro, heittojen määrä jne.)
    - Pelinäkymästä pääsee vain ja ainoastaan loppunäkymään.
- [Loppunäkymä](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/ui/end_view.py)
    - Kun peli on loppunut siirrytään tähä näkymään.  
    - Voittaja ja hänen pisteet julistetaan sekä näytetään lopullinen pistetilanne.
    - Loppunäkymästä pääsee vain ja ainoastaa aloitusnäkymään.

Näiden näkymien lisäksi on vielä luokka [Scoreboard](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/ui/scoreboard.py), jota käytetään pistetilanteen/taulukon näyttämiseen. Eriytetty omaksi luokakseen, koska sitä käytetään useammassa kuin yhdessä näkymässä.  

## Sovelluslogiikka  
Sovelluksen tietomallin muodostavat kaksi luokkaa [Game](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/entities/game.py) ja [Player](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/entities/player.py). Game luokalla kuvataan Yatzy peliä; sisältää tiedon pistetaulusta, nopista, mikä vuoro on kyseessä (pistetaulun rivi), kuka pelaaja on vuorossa ja kuinka monta heittoa hänellä on jäljellä. Player luokalla kuvataan peliin osallistuvaa henkilöä, tällä hetkellä sisältää vain tiedon pelaajan nimestä.  

Sovelluksen luokkakaavio (tietomallin muodostavat luokat):  
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/luokkakaavio.png?raw=true" width="500">

Sovellus-/pelilogiikasta on vastuussa luokka [GameService](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/services/game_service.py). GameService luokka pystyy lukemaan ja muuttamaan luokkien Game ja Player attribuutteja. Luokan kautta käyttöliittymä voi käyttää pelin toiminnallisuukia, kuten:
- pelaajan lisääminen peliin `add_player(player_name)`
- noppien heittäminen `roll_dices(keep)`
- toiminnalisuus seuraavaan vuoroon siirtymisestä `new_turn()`
- tiedon palauttaminen pelin loppumisesta `game_ends()`

GameService luokalla on apuluokka [PointChecker](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/services/point_checker.py), joka sisältää toiminnallisuuden pisteiden tarkistamiselle. PointChecker luokalla on attribuutti `dispatcher` (lista), joka sisältää kaikki pisteiden tarkistukseen vaadittavat funktiot. Kun peli on vuorossa `idx` kutsutaan funktiota `dispatcher[idx]`:

| idx   | scoreboard | dispatcher            |
| :----:|:-----      | :-----                |
| 0     | Aces       | `check_combination()` |
| 1     | Twos       | `check_combination()` |
| 2     | Threes     | `check_combination()` |
| ...   | ...        |  ...                  |
| 12    | Yahtzee    | `check_yahtzee()`     |
| 13    | Chance     | `check_chance()`      |

GameService luokka voi tallentaa pelin tietoja (pistetaulu, voittaja, voittajan pisteet) tietokantaan käyttäen luokkaa [GameRepository](https://github.com/ulmala/ot-harjoitustyo/blob/master/src/repositories/game_repository.py). Kyseinen luokka on vastuussa kaikista tietokantaoperaatioista.  

Sovelluksen pakkauskaavio näyttää seuraavalta:  
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/pakkauskaavio.png?raw=true" width="500">

## Tietojen tallennus



## Toiminnallisuudet
Alla pari esimerkkiä kuinka käyttöliittyymästä käytetään sovellusta.   
### Pelin käynnistäminen  
Alla oleva sekvenssikaavio kuvaa kuinka kaksi pelaajaa lisätään uuteen peliin.
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/start_game_sekvenssi.png?raw=true" width="500">

## Vuoron pelaaminen
Alla oleva sekvenssikaavio kuvaa sovelluksen toiminnallisuuden, kun pelaaja heittää vuoronsa alussa nopat ja eikä heitä tämän jälkeen noppia uudestaan.
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/play_turn_sekvenssi.png?raw=true" width="500">