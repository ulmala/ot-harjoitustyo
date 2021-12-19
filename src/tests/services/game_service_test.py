import pandas as pd
import unittest
from services.game_service import GameService
from entities.player import Player

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

class TestGameService(unittest.TestCase):
    def setUp(self):
        self.game = FakeGame()
        self.game_service = GameService(self.game)
        self.game_service.add_player('player1')
        self.game_service.add_player('player2')

    def test_add_player_returns_true_if_player_added(self):
        self.game_service = GameService(FakeGame())
        print(self.game_service.get_player_names())
        self.assertTrue(self.game_service.add_player('player1'))

    def test_turns_left_returns_false_if_game_has_no_turns_left(self):
        self.game.current_turn = len(self.game.scoreboard) + 1
        self.assertFalse(self.game_service.turns_left())

    def test_turns_left_returns_true_if_game_has_turns_left(self):
        self.game.current_turn = 2
        self.assertTrue(self.game_service.turns_left())

    def test_roll_dices_does_not_roll_dices_which_player_wants_to_keep(self):
        self.game_service.dices = [1,2,3,4,5]
        keep = [1,1,1,1,1]
        self.assertEqual(self.game_service.roll_dices(keep), self.game_service.dices)

    def test_roll_dices_rolls_only_dices_which_player_does_not_want_to_keep(self):
        self.game_service.dices = [1,2,3,4,5]
        keep = [1,0,0,0,1]
        for _ in range(100):
            dices = self.game_service.roll_dices(keep)
            self.assertEqual((dices[0], dices[-1]), (self.game_service.dices[0], self.game_service.dices[-1]))

    def test_turn_ends_returns_true_when_current_turn_ends(self):
        self.game.current_player = self.game.max_players - 1
        self.assertTrue(self.game_service.turn_ends())
    
    def test_turn_ends_returns_false_if_all_players_not_played_current_turn(self):
        self.game.current_player = 0
        self.assertFalse(self.game_service.turn_ends())

    def test_get_current_turn_name_returns_correct_turn_name(self):
        for idx, _ in self.game.scoreboard.iterrows():
            self.game.current_turn = self.game.scoreboard.index.get_loc(idx)
            self.assertEqual(self.game_service.get_current_turn_name(), idx)

    def test_execute_bonus_round_updates_possible_bonus_points_into_scoreboard(self):
        self.game.scoreboard[self.game_service.get_players()[0]] = [3, 6, 9, 12, 15, 18, '-', '-', '-', '-', '-', '-', '-', '-']
        self.game.scoreboard[self.game_service.get_players()[1]] = [3, 6, 9, 12, 15, 0, '-', '-', '-', '-', '-', '-', '-', '-']
        self.game_service.execute_bonus_round()
        self.assertEqual(self.game.scoreboard.at['Bonus', self.game_service.get_players()[0]], 50)
        self.assertEqual(self.game.scoreboard.at['Bonus', self.game_service.get_players()[1]], 0)

    def test_get_player_names_returns_correct_player_names(self):
        self.assertEqual(self.game_service.get_player_names(), ['player1', 'player2'])

    def test_declare_winner_returns_correct_winner(self):
        self.game.scoreboard[self.game.players[0]] = [1] * len(self.game.scoreboard)
        self.game.scoreboard[self.game.players[1]] = [0] * len(self.game.scoreboard)
        self.assertEqual(self.game_service.declare_winner(), (self.game.players[0], 1 * len(self.game.scoreboard)))

    def test_next_turn_updates_scoreboard_correctly(self):
        self.game_service.dices = [1,1,1,1,1]
        self.game_service.next_turn()
        self.assertEqual(self.game.scoreboard.at['Aces', self.game.players[0]], 5)
    
    def test_next_run_proceeds_to_next_turn_if_all_players_played(self):
        turn_before = self.game.current_turn
        self.game_service.roll_dices([0]*5)
        self.game.current_player = 1
        self.game_service.next_turn()
        self.assertTrue(self.game.current_turn > turn_before)

    def test_next_turn_calls_execute_bonus_round_when_the_next_round_is_bonus_round(self):
        self.game.scoreboard[self.game_service.get_players()[0]] = [3, 6, 9, 12, 15, 18, '-', '-', '-', '-', '-', '-', '-', '-']
        self.game.scoreboard[self.game_service.get_players()[1]] = [3, 6, 9, 12, 15, 0, '-', '-', '-', '-', '-', '-', '-', '-']
        self.game.current_turn = 5
        self.game.current_player = 1
        self.game_service.next_turn()
        self.assertEqual(self.game.current_turn, 7)

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
