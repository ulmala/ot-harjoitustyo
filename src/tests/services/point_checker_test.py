import unittest
from services.game_service import GameService
from services.point_checker import PointChecker

class TestPointChecker(unittest.TestCase):
    def setUp(self):
        self.point_checker = PointChecker()
        self.game_service = GameService()
        self.game_service.add_player('player_1')
        self.game_service.add_player('player_2')
        
    def test_checking_combination_returns_correct_sum(self):
        dices = [[3, 2, 4, 2, 1],
                 [2, 6, 6, 6, 6],
                 [4, 4, 5, 3, 3],
                 [5, 1, 6, 2, 3],
                 [6, 1, 1, 1, 3],
                 [6, 6, 6, 6, 6]]
        self.assertEqual(self.point_checker._check_combination(dices[0], 1), 1)
        self.assertEqual(self.point_checker._check_combination(dices[1], 2), 2)
        self.assertEqual(self.point_checker._check_combination(dices[2], 3), 6)
        self.assertEqual(self.point_checker._check_combination(dices[3], 4), 0)
        self.assertEqual(self.point_checker._check_combination(dices[4], 5), 0)
        self.assertEqual(self.point_checker._check_combination(dices[5], 6), 30)

    def test_checking_three_of_a_kind_returns_correct_sum(self):
        dices = [[1, 1, 1, 2, 2],
                 [1, 2, 3, 4, 5],
                 [1, 3, 4, 3, 3],
                 [1, 4, 5, 5, 5]]
        self.assertEqual(self.point_checker._check_three_of_a_kind(dices[0]), 3)
        self.assertEqual(self.point_checker._check_three_of_a_kind(dices[1]), 0)
        self.assertEqual(self.point_checker._check_three_of_a_kind(dices[2]), 9)
        self.assertEqual(self.point_checker._check_three_of_a_kind(dices[3]), 15)

    def test_checking_four_of_a_kind_returns_correct_sum(self):
        dices = [[2, 1, 2, 2, 2],
                 [5, 4, 4, 4, 4],
                 [6, 2, 3, 6, 6]]
        self.assertEqual(self.point_checker._check_four_of_a_kind(dices[0]), 8)
        self.assertEqual(self.point_checker._check_four_of_a_kind(dices[1]), 16)
        self.assertEqual(self.point_checker._check_four_of_a_kind(dices[2]), 0)

    def test_checking_full_house_returns_correct_sum(self):
        dices = [[1, 2, 1, 2, 1],
                 [3, 6, 3, 6, 6],
                 [5, 5, 5, 5, 5]]
        self.assertEqual(self.point_checker._check_full_house(dices[0]), 25)
        self.assertEqual(self.point_checker._check_full_house(dices[1]), 25)
        self.assertEqual(self.point_checker._check_full_house(dices[2]), 0)
        
    def test_checking_small_straight_returns_correct_sum(self):
        dices = [[3, 4, 5, 2, 1],
                 [5, 3, 2, 4, 2],
                 [4, 4, 3, 6, 5],
                 [3, 2, 1, 5, 6]]
        self.assertEqual(self.point_checker._check_small_straight(dices[0]), 30)
        self.assertEqual(self.point_checker._check_small_straight(dices[1]), 30)
        self.assertEqual(self.point_checker._check_small_straight(dices[2]), 30)
        self.assertEqual(self.point_checker._check_small_straight(dices[3]), 0)

    def test_checking_large_straight_returns_correct_sum(self):
        dices = [[1, 2, 3, 4, 5],
                 [4, 5, 2, 3, 6],
                 [1, 1, 2, 3, 4]]
        self.assertEqual(self.point_checker._check_large_straight(dices[0]), 40)
        self.assertEqual(self.point_checker._check_large_straight(dices[1]), 40)
        self.assertEqual(self.point_checker._check_large_straight(dices[2]), 0)

    def test_checking_yahtzee_returns_correct_sum(self):
        dices = [[1, 1, 1, 1, 1],
                 [1, 2, 3, 4, 5]]
        self.assertEqual(self.point_checker._check_yahtzee(dices[0]), 50)
        self.assertEqual(self.point_checker._check_yahtzee(dices[1]), 0)

    def test_checking_chance_returns_correct_sum(self):
        dices = [1, 2, 3, 4, 5]
        self.assertEqual(self.point_checker._check_chance(dices), sum(dices))

    def test_check_bonus_returns_bonus_when_points_over_63(self):
        player = self.game_service.get_players()[0]
        self.game_service.game.scoreboard[player] = [3, 6, 9, 12, 15, 18, '-', '-', '-', '-', '-', '-', '-', '-']
        self.assertEqual(self.point_checker._check_bonus(player, self.game_service.game.scoreboard), 50)

    def test_check_bonus_does_not_return_bonuse_when_points_under_63(self):
        player = self.game_service.get_players()[0]
        self.game_service.game.scoreboard[player] = [3, 6, 9, 12, 15, 0, '-', '-', '-', '-', '-', '-', '-', '-']
        self.assertEqual(self.point_checker._check_bonus(player, self.game_service.game.scoreboard), 0)      
