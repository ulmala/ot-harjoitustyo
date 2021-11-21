from entities.player import Player
from entities.roll import Roll
from services.game_service import game_service

class UI:
    def start(self):
        print('lets play yahtzee')
        print()
        
        # Pelin luominen
        while True:
            choice = input('press x to start new game, q to exit: ')
            if choice == 'q':
                exit()
            elif choice == 'x':
                break
            else:
                continue
    
        # Pelaajien lisääminen
        while True:
            name = input('give name for player (q to quit adding): ')
            if name == 'q': break
            if not game_service.add_player(Player(name)):
                print('max players achieved!')
                break
        # Pelaaminen alkaa --> loopataan dataframe läpi
        game_service.start_game()