import pandas as pd


class FakeGame():
    def __init__(self):
        self.players = []
        self.max_players = 2
        index = ['Aces', 'Twos', 'Threes','Fours', 'Fives', 'Sixes', 'Bonus',
                 'Three of a kind', 'Four of a kind', 'Full house', 'Small straight',
                 'Large straight', 'Yahtzee', 'Chance']
        self.scoreboard = pd.DataFrame(index=index, columns=self.players)
        self.current_turn = 0
        self.current_player = 0

fake_game = FakeGame()