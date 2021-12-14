import unittest
from entities.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player('player')

    def test_constructor_sets_name_correctly(self):
        self.assertEqual(self.player.name, 'player')

    def test_player_str_repr_is_correct(self):
        self.assertEqual(str(self.player), 'player')