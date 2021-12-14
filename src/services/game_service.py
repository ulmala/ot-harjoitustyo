from entities.game import (
    game as default_game
)
from entities.player import Player
from services.roll_service import roll_service


class GameService:
    """Class which is handles game related functions
    
    Attributes:
        game: instance of Game class
    """
    def __init__(self, game=default_game):
        """Class consturctor

        Args:
            game (Game, optional): instance of class Game. Defaults to default_game.
        """
        self.game = game

    def add_player(self, player_name):
        """Function which adds players to the game. Creates instance of Player class
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
        if self.game.current_turn < len(self.game.scoreboard.index):
            return True
        return False

    def play_turn(self):
        """Responsible for executin one turn/row in the scoreboard.
        Loops through each player in the game. If the current turn is the Bonus
        turn, will call the check_bonus function.

        Returns:
            pd.DataFrame(): updated scoreboard
        """
        turn_name = self.game.scoreboard.index[self.game.current_turn]
        for player in self.game.players:
            if turn_name == 'Bonus':
                points = self.check_bonus(player)
            else:
                points = roll_service.execute_rolls(turn_name)
            self.game.scoreboard.at[turn_name, player] = points
        self.game.current_turn += 1
        return self.game.scoreboard

    def check_bonus(self, player):
        """Checks if the player is allowed to have bonus points (sum of the
        first 6 rows in the game scoreboard is equal or greater than 63)

        Args:
            player (Player): player to check the bonus points

        Returns:
            int: 50 if player is allowed to have the bonus points, else 0.
        """
        if self.game.scoreboard[player][:6].sum() >= 63:
            return 50
        return 0

    def declare_winner(self):
        """Calculates the sum of each players points in the scoreboard

        Returns:
            (Player, int): winner of the game and the winning points
        """
        self.game.scoreboard = self.game.scoreboard.astype(int)
        winner = self.game.scoreboard.sum().idxmax()
        points = self.game.scoreboard.sum().max()
        return winner, points

    def get_status(self):
        """Returns the current scoreboard situation as type string

        Returns:
            str: current scoreboard
        """
        return self.game.scoreboard.to_string()

    def get_players(self):
        """Returns the list of players in current game

        Returns:
            list[Player]: list of players
        """
        return self.game.players

game_service = GameService()
