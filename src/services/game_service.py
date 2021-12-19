from entities.game import (
    game as default_game
)
from entities.player import Player
import random
from services.roll_service import roll_service


class GameService:
    def __init__(self, game=default_game):
        self.game = game
        self.dices = [':('] * 5
        self.throws = 3
        self.current_player = 0

    def add_player(self, player_name):
        player = Player(player_name)
        if len(self.game.players) < self.game.max_players:
            self.game.players.append(player)
            self.game.scoreboard[player] = '-'
            return True
        return False

    def turns_left(self):
        if self.game.current_turn < len(self.game.scoreboard.index):
            return True
        return False

    def roll_dices(self, keep):
        for i in range(5):
            if keep[i] == 0:
                self.dices[i] = random.randint(1,6)
        return self.dices

    def next_turn(self):
        points = roll_service.check_points(self.dices, self.get_current_turn_name())
        self.game.scoreboard.at[self.get_current_turn_name(),
                                self.get_current_player()] = points
        # 'Nollataan' nopat
        self.dices = [random.randint(1,6) for _ in range(5)]
        # Seuraavalle pelaajalle täydet heitot
        self.throws = 3
        # Jos pelattava vuoro loppuu niin siirrytään seuravaan ja aloitetaan
        # taas pelilaudan ensimmäisestä pelaajasta
        if self.turn_ends():
            self.game.current_turn += 1
            self.game.current_player = 0
        # Jos pelattava vuoro ei lopu niin siirrytään seuraavaan pelaajaan
        else:
            self.game.current_player += 1
        return True

    def turn_ends(self):
        if self.get_current_player() == self.game.scoreboard.columns[-1]:
            return True
        return False

    def get_current_player(self):
        return self.game.scoreboard.columns[self.game.current_player]

    def get_current_turn_name(self):
        return self.game.scoreboard.index[self.game.current_turn]

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
