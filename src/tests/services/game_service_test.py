import unittest
from entities.game import Game
from services.game_service import GameService
from entities.player import Player


class TestGameService(unittest.TestCase):
    def setUp(self):
        self.game_service = GameService()
        self.game_service.add_player('player1')
        self.game_service.add_player('player2')

    def test_add_player_returns_true_if_player_added(self):
        self.game_service.game = Game()
        self.assertTrue(self.game_service.add_player('player1'))

    def test_turns_left_returns_false_if_game_has_no_turns_left(self):
        self.game_service.game.current_turn = len(self.game_service.game.scoreboard) + 1
        self.assertFalse(self.game_service._turns_left())

    def test_turns_left_returns_true_if_game_has_turns_left(self):
        self.game_service.game.current_turn = 2
        self.assertTrue(self.game_service._turns_left())

    def test_roll_dices_does_not_roll_dices_which_player_wants_to_keep(self):
        self.game_service.game.dices = [1,2,3,4,5]
        keep = [1,1,1,1,1]
        self.assertEqual(self.game_service.roll_dices(keep), self.game_service.game.dices)

    def test_roll_dices_rolls_only_dices_which_player_does_not_want_to_keep(self):
        self.game_service.game.dices = [1,2,3,4,5]
        keep = [1,0,0,0,1]
        for _ in range(100):
            dices = self.game_service.roll_dices(keep)
            self.assertEqual((dices[0], dices[-1]), (self.game_service.game.dices[0], self.game_service.game.dices[-1]))

    def test_turn_ends_returns_true_when_current_turn_ends(self):
        self.game_service.game.current_player = len(self.game_service.get_players()) - 1
        self.assertTrue(self.game_service._turn_ends())
    
    def test_turn_ends_returns_false_if_all_players_not_played_current_turn(self):
        self.game_service.game.current_player = 0
        self.assertFalse(self.game_service._turn_ends())

    def test_get_current_turn_name_returns_correct_turn_name(self):
        for idx, _ in self.game_service.game.scoreboard.iterrows():
            self.game_service.game.current_turn = self.game_service.game.scoreboard.index.get_loc(idx)
            self.assertEqual(self.game_service.get_current_turn_name(), idx)

    def test_execute_bonus_round_updates_possible_bonus_points_into_scoreboard(self):
        self.game_service.game.current_turn = 6
        self.game_service.game.scoreboard[self.game_service.get_players()[0]] = [3, 6, 9, 12, 15, 18, '-', '-', '-', '-', '-', '-', '-', '-']
        self.game_service.game.scoreboard[self.game_service.get_players()[1]] = [3, 6, 9, 12, 15, 0, '-', '-', '-', '-', '-', '-', '-', '-']
        self.game_service._execute_bonus_round()
        self.assertEqual(self.game_service.game.scoreboard.at['Bonus', self.game_service.get_players()[0]], 50)
        self.assertEqual(self.game_service.game.scoreboard.at['Bonus', self.game_service.get_players()[1]], 0)

    def test_get_player_names_returns_correct_player_names(self):
        self.assertEqual(self.game_service.get_player_names(), ['player1', 'player2'])

    def test_declare_winner_returns_correct_winner(self):
        self.game_service.game.scoreboard[self.game_service.game.players[0]] = [1] * len(self.game_service.game.scoreboard)
        self.game_service.game.scoreboard[self.game_service.game.players[1]] = [0] * len(self.game_service.game.scoreboard)
        self.assertEqual(self.game_service.declare_winner(), (self.game_service.game.players[0], 1 * len(self.game_service.game.scoreboard)))

    def test_update_points_updates_scoreboard_correctly(self):
        self.game_service.game.dices = [1,1,1,1,1]
        self.game_service.update_points()
        self.assertEqual(self.game_service.game.scoreboard.at['Aces', self.game_service.get_players()[0]], 5)
    
    def test_new_run_proceeds_to_next_turn_if_all_players_played(self):
        turn_before = self.game_service.get_current_turn()
        self.game_service.roll_dices([0]*5)
        self.game_service.game.current_player = 1
        self.game_service.new_turn()
        self.assertTrue(self.game_service.get_current_turn() > turn_before)

    def test_new_turn_calls_execute_bonus_round_when_the_next_round_is_bonus_round(self):
        self.game_service.game.scoreboard[self.game_service.get_players()[0]] = [3, 6, 9, 12, 15, 18, '-', '-', '-', '-', '-', '-', '-', '-']
        self.game_service.game.scoreboard[self.game_service.get_players()[1]] = [3, 6, 9, 12, 15, 0, '-', '-', '-', '-', '-', '-', '-', '-']
        self.game_service.game.current_turn = 5
        self.game_service.game.current_player = 1
        self.game_service.new_turn()
        self.assertEqual(self.game_service.get_current_turn(), 7)

    def test_add_player_returns_false_when_player_cant_be_added(self):
        player_1, player_2 = Player('player_1'), Player('player_2')
        self.game_service.add_player(player_1)
        self.game_service.add_player(player_2)
        self.assertFalse(self.game_service.add_player('player'))

    def test_game_ends_returns_true_when_last_player_has_played_last_round(self):
        self.game_service.game.current_player = len(self.game_service.get_players()) - 1
        self.game_service.game.current_turn = 14
        for col in self.game_service.game.scoreboard:
            self.game_service.game.scoreboard[col] = list(range(14))
        self.assertTrue(self.game_service.game_ends())

    def test_new_turn_returns_false_when_game_ends(self):
        self.game_service.game.current_player = len(self.game_service.get_players()) - 1
        self.game_service.game.current_turn = 14
        for col in self.game_service.game.scoreboard:
            self.game_service.game.scoreboard[col] = list(range(14))
        self.assertFalse(self.game_service.new_turn())

    def test_new_turn_gives_the_turn_to_next_player(self):
        player_in_turn_before = self.game_service.get_current_player()
        self.game_service.new_turn()
        self.assertNotEqual(self.game_service.get_current_player(), player_in_turn_before)

    def test_get_dices_returns_correct_dices(self):
        self.game_service.roll_dices(keep=[0,0,0,0,0])
        dices = self.game_service.game.dices
        self.assertEqual(self.game_service.get_dices(), dices)

    def test_get_throws_returns_correct_number_of_trhows(self):
        self.assertEqual(self.game_service.get_throws_left(), 3)
        self.game_service.game.throws -= 2
        self.assertEqual(self.game_service.get_throws_left(), 1)