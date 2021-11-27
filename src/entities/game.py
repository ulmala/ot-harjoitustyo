import pandas as pd


class Game:
    def __init__(self):
        self.players = []
        self.max_players = 2
        index = ['Aces', 'Twos', 'Threes','Fours', 'Fives', 'Sixes', 'Bonus']
        columns = self.players
        self.scoreboard = pd.DataFrame(index=index, columns=columns)
        self.current_turn = 0

game = Game()
