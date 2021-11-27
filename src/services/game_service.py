from entities.game import (
    game as default_game
)
from services.roll_service import roll_service


class GameService:
    def __init__(self, game=default_game):
        self.game = game

    def add_player(self, player):
        if len(self.game.players) < self.game.max_players:
            self.game.players.append(player)
            self.game.scoreboard[player.name] = '-'
            return True
        return False

    def turns_left(self):
        if self.game.current_turn < len(self.game.scoreboard.index):
            return True
        return False

    def play_turn(self):
        turn_name = self.game.scoreboard.index[self.game.current_turn]
        for player in self.game.scoreboard.columns:
            if turn_name == 'Bonus':
                points = self.check_bonus(player)
            else:
                points = roll_service.execute_rolls(turn_name)
            self.game.scoreboard.at[turn_name, player] = points
        self.game.current_turn += 1
        return self.game.scoreboard

    def check_bonus(self, player):
        if self.game.scoreboard[player][:6].sum() >= 63:
            return 50
        return 0

    def declare_winner(self):
        self.game.scoreboard = self.game.scoreboard.astype(int)
        winner = self.game.scoreboard.sum().idxmax()
        points = self.game.scoreboard.sum().max()
        return winner, points

    def get_status(self):
        return self.game.scoreboard.to_string()

    def get_players(self):
        return self.game.players

game_service = GameService()
