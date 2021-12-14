import pandas as pd
import unittest
from services.game_service import GameService
from entities.game import game
from entities.player import Player

class FakeGame():
    def __init__(self):
        self.players = []
        self.max_players = 2
        index = ['Aces', 'Twos', 'Threes','Fours', 'Fives', 'Sixes', 'Bonus',
                 'Three of a kind', 'Four of a kind', 'Full house', 'Small straight',
                 'Large straight', 'Yahtzee', 'Chance']
        columns = self.players
        self.scoreboard = pd.DataFrame(index=index, columns=columns)
        self.current_turn = 0

class TestGameService(unittest.TestCase):
    def setUp(self):
        self.game = FakeGame()
        self.game_service = GameService(self.game)

    def test_check_bonus_returns_bonus_when_points_over_63(self):
        player = 'player_1'
        self.game.scoreboard[player] = [3, 6, 9, 12, 15, 18, '-', '-', '-', '-', '-', '-', '-', '-']
        self.assertEqual(self.game_service.check_bonus(player), 50)

    def test_check_bonus_does_not_return_bonuse_when_points_under_63(self):
        player = 'player_1'
        self.game.scoreboard[player] = [3, 6, 9, 12, 15, 0, '-', '-', '-', '-', '-', '-', '-', '-']
        self.assertEqual(self.game_service.check_bonus(player), 0)

    def test_add_player_returns_false_when_player_cant_be_added(self):
        player_1, player_2 = Player('player_1'), Player('player_2')
        self.game_service.add_player(player_1)
        self.game_service.add_player(player_2)
        self.assertFalse(self.game_service.add_player('player'))

    def test_add_player_returns_true_when_player_added(self):
        player = Player('player_1')
        self.assertTrue(self.game_service.add_player(player))

    def test_get_players_returns_correct_players(self):
        player_1, player_2 = Player('player_1'), Player('player_2')
        self.game_service.add_player(player_1)
        self.game_service.add_player(player_2)
        self.assertEqual(self.game_service.get_players(), [player_1, player_2])

    def test_declare_winner_returns_correct_winner(self):
        player_1, player_2 = Player('player_1'), Player('player_2')
        self.game_service.add_player(player_1)
        self.game_service.add_player(player_2)
        self.game.scoreboard[player_1] = [1] * len(self.game.scoreboard)
        self.game.scoreboard[player_2] = [2] * len(self.game.scoreboard)
        self.assertEqual(self.game_service.declare_winner(), (player_2, 28))
