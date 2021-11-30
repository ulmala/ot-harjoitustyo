from entities import game
from entities.player import Player
from entities.roll import Roll
from services.game_service import game_service

class UI:
    def start(self):
        print('\n' * 50)
        print('################# YATZY #################')
        print()
        
        # Pelin luominen
        while True:
            choice = input('Syötä x jos haluat käynnistää uuden pelin\ntai syötä q jos haluat lopettaa: ')
            if choice == 'q':
                exit()
            elif choice == 'x':
                break
            else:
                continue
        print("\n\n")        

        # Pelaajien lisääminen
        while True:
            name = input('Syötä pelaajan nimi: ')
            if name == 'q':
                break
            if not game_service.add_player(Player(name)):
                print('Peli tukee vain kahta pelaajaa!')
                break
        print("\n\n")

        print("Kun kysytään minkä nopan haluat pitää, syötä niiden noppien indeksit mitkä haluat pitää (eroteltuna pilkulla)")
        
        # Peli alkaa
        while game_service.turns_left():
            print(game_service.play_turn())

        # Voittajan julistus
        print("\n\n")
        print(game_service.get_status())
        winner, points = game_service.declare_winner()
        print(f'VOITTAJA ON PELAAJA: {winner}, PISTEILLÄ {points}')