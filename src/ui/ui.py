from entities.player import Player
from entities.roll import Roll
from services.game_service import GameService

class UI:
    def start(self):
        print('########### LETS PLAY YATHZEE! ###########')
        name = input('Give name for player: ')
        player = Player(name)
        print(f'Welcome {player}!')
        game_service = GameService()
        while True:
            roll = Roll()
            for _ in range(3):
                if all(roll.keep_dice):
                    break
                print('here are the dices ', roll.dices)
                keep = input('which dices you want to keep? ')
                roll.keep_dices(keep)
                roll.roll_dices()
            print(game_service.check_combination(roll.dices, 1))
            if input == 'q':
                break