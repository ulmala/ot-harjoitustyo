import random
from entities.player import Player
from entities.game import Game
from services.point_checker import point_checker
from repositories.game_repository import (
    game_repository as default_game_repository
)

class GameService:
    """Class which is handles game related functions

    Attributes:
        game: instance of Game class

        LISÄÄ MUUT

    """
    def __init__(self, game_repository=default_game_repository) -> None:
        """Class consturctor
        Args:
            game (Game, optional): instance of class Game. Defaults to default_game.
        """
        self.game = Game()
        self._game_repository = game_repository

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

    def turns_left(self) -> bool:
        """Function which can be used to check if there is any turns left in the game
        (rows in the game scoreboard)
        Returns:
            boolean: True if game has turns left, else False
        """
        if self.game.current_turn < len(self.game.scoreboard.index) - 1:
            return True
        return False

    def roll_dices(self, keep) -> list:
        """Function which rolls all dices (random number) user wants to reroll.

        Args:
            keep (list): list holding information which dices user wants to keep
            0 = user wants to reroll dice, 1 = user wants to keep the dice

        Returns:
            list: list of dices
        """
        for i in range(5):
            if keep[i] == 0:
                self.game.dices[i] = random.randint(1,6)
        self.game.throws -= 1
        return self.game.dices

    def update_points(self):
        """Updates current players points into the scoreboard. This function is called
        when players turn ends
        """
        points = point_checker.dispatcher[self.game.current_turn](self.game.dices)
        self.game.scoreboard.at[self.get_current_turn_name(),
                                self.get_current_player()] = points

    def new_turn(self) -> bool:
        """This function is responsible for proceeding the game to the next round and changing
        the player. If game does not have any turns left, will end the game.

        Returns:
            bool: returns True if proceeds to next round, else False
        """
        if self.game_ends():
            return False
        self.game.throws = 3
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
            points = point_checker.dispatcher[self.game.current_turn](player, self.game.scoreboard)
            self.game.scoreboard.at['Bonus', player] = points
        self.game.current_turn += 1

    def game_ends(self) -> bool:
        """Checks if the game has ended. If the current turn has ended (no players left)
        and there are no furhter turns left means that the game has ended

        Returns:
            bool: True if game ended, else Fals
        """
        if self.turn_ends() and not self.turns_left():
            self.save_winner()
            return True
        return False

    def turn_ends(self) -> bool:
        """Checks if the turn/round ends. If the current player is the last one
        to play the turn, turn ends.

        Returns:
            bool: True if turn ends, else False
        """
        if self.get_current_player() == self.game.scoreboard.columns[-1]:
            return True
        return False

    def get_current_player(self) -> Player:
        """Returns the the player whos turn it currently is in the game.

        Returns:
            Player: instance of Player class
        """
        return self.game.scoreboard.columns[self.game.current_player]

    def get_current_turn_name(self) -> str:
        """Returns the name of current turn, e.g. 'Aces'

        Returns:
            str: name of the current turn
        """
        return self.game.scoreboard.index[self.game.current_turn]

    def get_current_turn(self) -> int:
        """Returns the number of current turn (index in the scoreboard)

        Returns:
            int: number of current turn
        """
        return self.game.current_turn

    def declare_winner(self) -> tuple:
        """Declares the winner of the game. Calculates the sum of all players
        points.

        Returns:
            tuple: name of the winner and the winning points
        """
        self.game.scoreboard = self.game.scoreboard.astype(int)
        winner = self.game.scoreboard.sum().idxmax()
        points = self.game.scoreboard.sum().max()
        return winner, points

    def get_players(self) -> list:
        """Returns the list of players in the game

        Returns:
            list: list of class Player instances
        """
        return self.game.players

    def get_player_names(self) -> list:
        """Returns list of player names

        Returns:
            list: list of player names
        """
        return [player.name for player in self.game.players]

    def get_throws_left(self) -> int:
        """Returns the amount of throws current player has left

        Returns:
            int: amount of throws
        """
        return self.game.throws

    def get_dices(self) -> list:
        """Returns the dices.

        Returns:
            list: dices as list
        """
        return self.game.dices


    ### TÄMÄ PITÄÄ TEHDÄ LOPPUUN
    def save_winner(self):
        winner, points = self.declare_winner()
        self._game_repository.insert_game(self.game.scoreboard.to_csv(sep=';'), str(winner), int(points))
        self._game_repository.get_all_games()
        print(self._game_repository.get_top_5_high_scores())
game_service = GameService()
