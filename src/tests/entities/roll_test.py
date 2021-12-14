import unittest
from entities.roll import Roll

class TestRoll(unittest.TestCase):
    def setUp(self):
        self.roll = Roll()

    def test_roll_has_five_dices(self):
        self.assertEqual(len(self.roll.dices), 5)

    def test_roll_does_not_keep_any_dices_by_default(self):
        self.assertEqual(self.roll.keep_dice, [False]*5)

    def test_roll_str_repr_is_correct(self):
        for i in range(5):
            self.roll.dices[i] = i+1
        self.assertEqual(str(self.roll), '[1, 2, 3, 4, 5]')