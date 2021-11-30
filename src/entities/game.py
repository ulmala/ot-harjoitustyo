import pandas as pd


class Game:
    def __init__(self):
        self.players = []
        self.max_players = 2
        index = ['Aces', 'Twos', 'Threes','Fours', 'Fives', 'Sixes', 'Bonus',
                 'Three of a kind', 'Four of a kind', 'Full house', 'Small straight',
                 'Large straight', 'Yahtzee', 'Chance']
        columns = self.players
        self.scoreboard = pd.DataFrame(index=index, columns=columns)
        self.current_turn = 0

game = Game()
