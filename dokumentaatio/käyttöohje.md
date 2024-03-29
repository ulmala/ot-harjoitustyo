# Käyttöohje
Lataa viimesin release [täältä](https://github.com/ulmala/ot-harjoitustyo/releases).

Pura ladatun kansion sisältö ja siirry kansion sisälle. Seuraavat komennot toteutetaan kansion sisällä.

## Sovelluksen käynnistäminen
Asenna sovelluksen riippuvuudet komennolla:  
```bash
poetry install
```

Alusta sovelluksen käyttämä tietokanta komennolla:  
```bash
poetry run invoke init-db
```

Käynnistä sovellus komennolla:  
```bash
poetry run invoke start
```

## Uden pelin aloittaminen

Pelaajat (esimerkissä kaksi) syöttävät nimimerkkinsä kenttiin ja painavat 'Start' painiketta. Sovellus lisää peliin vain ne pelaajat minkä nimimerkkikentässä on sisältöä. Vähintään yhdesssä kentässä pitää olla merkkejä jotta peli käynnistyy. Painamalla linkkiä "Click here to open game rules" sovellus avaa Wikipedian sivun missä kerrotaan pelin säännöt.  
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/käyttöohje/start_view.png?raw=true" width="500">   

Pistetaulukossa rivin oranssi väri kertoo, että tätä riviä heitetään nyt. Sarakkeissa näkyvät pelaajien livepisteet. Pelaaja voi pitää haluamansa nopat valitsemalla kyseisen nopan checkboxin. Roll dices painikkeella heitetään nopat. Painikkeen alapuolella lukee minkä pelaajan vuoro on ja monta heittoa hänellä on jäljellä.  
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/käyttöohje/in_game.png?raw=true" width="500">  

Viimeisessä näkymässä julistetaan pelin voittaja ja näytetään pelin lopullinen pistetilanne. Painamalla new game, peli siirtyy takaisin aloitusnäkymään mistä voi käynnistää uuden pelin.  
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/käyttöohje/game_end.png?raw=true" width="500">  

Peli palaa samaan aloitusnäkymään. Tällä kertaa alhaalla olevaan 'All time top 5 scores' taulukkoon on päivittynyt äskeisen pelin tulos. Tämä taulukko näyttää aina 5 suurinta pistemäärää mitä tietokannasta löytyy.  
<img src="https://github.com/ulmala/ot-harjoitustyo/blob/master/dokumentaatio/imgs/käyttöohje/start_view_2.png?raw=true" width="500">  