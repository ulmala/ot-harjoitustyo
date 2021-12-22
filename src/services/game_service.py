import random
from entities.game import (
    game as default_game
)
from entities.player import Player
from services.point_checker import point_checker


class GameService:
    """Class which is handles game related functions
    
    Attributes:
        game: instance of Game class

        LISÄÄ MUUT

    """
    def __init__(self, game=default_game):
        """Class consturctor
        Args:
            game (Game, optional): instance of class Game. Defaults to default_game.
        """
        self.game = game
        self.dices = ['X'] * 5
        self.throws = 3
        self.current_player = 0

    def add_player(self, player_name):
        """Function adds players to the game. Creates instance of Player class
        based on the player_name argument
        Args:
            player_name (str): name of the player
        Returns:
            boolean: True if player was added to the game. Return False if number of
            maximum players has been reached.
        """
        player = Player(player_name)
        if len(self.game.players) < self.game.max_players:
            self.game.players.append(player)
            self.game.scoreboard[player] = '-'
            return True
        return False

    def turns_left(self):
        """Function which can be used to check if there is any turns left in the game
        (rows in the game scoreboard)
        Returns:
            boolean: True if game has turns left, else False
        """
        if self.game.current_turn < len(self.game.scoreboard.index) - 1:
            return True
        return False

    def roll_dices(self, keep):
        """Function which rolls all dices (random number) user wants to reroll.

        Args:
            keep (list): list holding information which dices user wants to keep
            0 = user wants to reroll dice, 1 = user wants to keep the dice

        Returns:
            list: list of dices
        """
        for i in range(5):
            if keep[i] == 0:
                self.dices[i] = random.randint(1,6)
        return self.dices

    def next_turn(self):
        points = point_checker.dispatcher[self.game.current_turn](self.dices)
        self.game.scoreboard.at[self.get_current_turn_name(),
                                self.get_current_player()] = points
        self.dices = ['X' for _ in range(5)]
        self.throws = 3
        if self.turn_ends():
            self.game.current_turn += 1
            self.game.current_player = 0
            if self.get_current_turn_name() == 'Bonus':
                self.execute_bonus_round()
        else:
            self.game.current_player += 1
        return True

    def execute_bonus_round(self):
        """Executes the bonus round. This will be executed automatically when
        first six rounds are played. Iterates over each player and checks if the
        are allowed to have bonus points. Updates the scoreboard.
        """
        for player in self.get_players():
            points = self.check_bonus(player)
            self.game.scoreboard.at['Bonus', player] = points
        self.game.current_turn += 1

    def turn_ends(self):
        """Checks if the turn/round ends. If the current player is the last one
        to play the turn, turn ends.

        Returns:
            bool: True if turn ends, else False
        """
        if self.get_current_player() == self.game.scoreboard.columns[-1]:
            return True
        return False

    def get_current_player(self):
        """Returns the the player whos turn it currently is in the game.

        Returns:
            Player: instance of Player class
        """
        return self.game.scoreboard.columns[self.game.current_player]

    def get_current_turn_name(self):
        """Returns the name of current turn, e.g. 'Aces'

        Returns:
            str: name of the current turn
        """
        return self.game.scoreboard.index[self.game.current_turn]

    def get_current_turn(self):
        """Returns the number of current turn (index in the scoreboard)

        Returns:
            int: number of current turn
        """
        return self.game.current_turn

    def check_bonus(self, player):
        """Checks if the player is allowed to have bonus points, at least 63 points
        from the first six rounds.

        Args:
            player ([type]): [description]

        Returns:
            int: 50 if bonus is okay, else 0
        """
        if self.game.scoreboard[player][:6].sum() >= 63:
            return 50
        return 0

    def declare_winner(self):
        """Declares the winner of the game. Calculates the sum of all players
        points.

        Returns:
            tuple: name of the winner and the winning points
        """
        self.game.scoreboard = self.game.scoreboard.astype(int)
        winner = self.game.scoreboard.sum().idxmax()
        points = self.game.scoreboard.sum().max()
        return winner, points

    def get_players(self):
        """Returns the list of players in the game

        Returns:
            list: list of class Player instances
        """
        return self.game.players

    def get_player_names(self):
        """Returns list of player names

        Returns:
            list: list of player names
        """
        return [player.name for player in self.game.players]

game_service = GameService()
