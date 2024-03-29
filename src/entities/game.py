import pandas as pd


class Game:
    """Class which represents the Yahtzee game.

    Attributes:
        players: list of players in the game
        max_players: maximum number of players allowed in the game
        scoreboard: Yahtzee scoreboard represented as pandas dataframe
        current_turn: integer which holds the information on which row
                      (scoreboard) the game is currently on
        current_player: integer ('index') of the current player, ranging from (1 to max_players)
        dices: list of integers representing the dices (at the start all values are 'X')
        throws: amount of throws player has left. Max 3, min 0 (turn ends)
    """
    def __init__(self):
        """Class constructor
        """
        self.players = []
        self.max_players = 4
        index = ['Aces', 'Twos', 'Threes','Fours', 'Fives', 'Sixes', 'Bonus',
                 'Three of a kind', 'Four of a kind', 'Full house', 'Small straight',
                 'Large straight', 'Yahtzee', 'Chance']
        self.scoreboard = pd.DataFrame(index=index, columns=self.players)
        self.current_turn = 0
        self.current_player = 0
        self.dices = ['X'] * 5
        self.throws = 3

game = Game()
