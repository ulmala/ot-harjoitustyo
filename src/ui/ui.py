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
                
        print('\n' * 50)
        # Pelaajien lisääminen
        while True:
            name = input('Syötä pelaajan nimi: ')
            if name == 'q': break
            if not game_service.add_player(Player(name)):
                print('Peli tukee vain kahta pelaajaa!')
                break

        # Pelaaminen alkaa
        print('\n' * 50)
        print('################# PELI ALKAA #################')
        print('HUOM! kun kysytään mitkä nopat haluat pitää niin syötä niiden noppien\nlista indeksit mitkä haluat pitää ja erota ne pilkulla ","!')
        input('Aloita peli painamalla Enter')
        game_service.start_game()

        # Voittajan julistus
        winner, points = game_service.declare_winner()
        print('\n' * 2)
        print(f'VOITTAJA ON PELAAJA: {winner}, PISTEILLÄ {points}')