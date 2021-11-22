import pandas as pd


class Game:
    def __init__(self):
        self.players = []
        self.max_players = 2
        index = ['Aces', 'Twos', 'Threes','Fours', 'Fives', 'Sixes']
        columns = self.players
        self.scoreboard = pd.DataFrame(index=index, columns=columns)

game = Game()
