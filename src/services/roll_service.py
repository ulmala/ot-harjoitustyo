import random
from entities.roll import (
    roll as default_roll
)
from entities.game import (
    game as default_game
)

class RollService:
    def __init__(self, roll=default_roll, game=default_game):
        self.roll = roll
        self.game = game

    def roll_dices(self, keep):
        if all(k == 1 for k in keep) or self.roll.throws == 0:
            self.roll.dices = [':(']*5
            self.roll.throws = 3
        else:
            for i in range(5):
                if keep[i] == 0:
                    self.roll.dices[i] = random.randint(1,6)
        return self.roll.dices

    def get_current_player(self):
        return self.game.scoreboard.columns[self.roll.player_in_turn]

    def turn_ends(self):
        if self.get_current_player() == self.game.scoreboard.columns[-1]:
            return True

    def check_points(self, dices, turn_name):
        if turn_name == 'Aces':
            return self.check_combination(dices, 1)
        if turn_name == 'Twos':
            return self.check_combination(dices, 2)
        if turn_name == 'Threes':
            return self.check_combination(dices, 3)
        if turn_name == 'Fours':
            return self.check_combination(dices, 4)
        if turn_name == 'Fives':
            return self.check_combination(dices, 5)
        if turn_name == 'Sixes':
            return self.check_combination(dices, 6)
        if turn_name == 'Three of a kind':
            return self.check_three_of_a_kind(dices)
        if turn_name == 'Four of a kind':
            return self.check_four_of_a_kind(dices)
        if turn_name == 'Full house':
            return self.check_full_house(dices)
        if turn_name == 'Small straight':
            return self.check_small_straight(dices)
        if turn_name == 'Large straight':
            return self.check_large_straight(dices)
        if turn_name == 'Yahtzee':
            return self.check_yahtzee(dices)
        if turn_name == 'Chance':
            return self.check_chance(dices)

    def check_combination(self, dices, n):
        return dices.count(n) * n

    def check_three_of_a_kind(self, dices):
        dices.sort()
        if dices[:3].count(dices[0]) == 3:
            return sum(dices[:3])
        if dices[1:4].count(dices[1]) == 3:
            return sum(dices[1:4])
        if dices[2:5].count(dices[2]) == 3:
            return sum(dices[2:5])
        return 0

    def check_four_of_a_kind(self, dices):
        dices.sort()
        if dices[:4].count(dices[0]) == 4:
            return sum(dices[:4])
        if dices[1:5].count(dices[1]) == 4:
            return sum(dices[1:5])
        return 0

    def check_full_house(self, dices):
        dices.sort()
        if dices[0] == dices[1] == dices[2] and dices[3] == dices[4] and dices[0] != dices[4]:
            return 25
        if dices[0] == dices[1] and dices[2] ==  dices[3] == dices[4] and dices[0] != dices[4]:
            return 25
        return 0

    def check_small_straight(self, dices):
        dices.sort()
        if all(x in dices for x in [1, 2, 3, 4]):
            return 30
        if all(x in dices for x in [2, 3, 4, 5]):
            return 30
        if all(x in dices for x in [3, 4, 5, 6]):
            return 30
        return 0

    def check_large_straight(self, dices):
        dices.sort()
        if all(x in dices for x in [1, 2, 3, 4, 5]):
            return 40
        if all(x in dices for x in [2, 3, 4, 5, 6]):
            return 40
        return 0

    def check_yahtzee(self, dices):
        if len(set(dices)) == 1:
            return 50
        return 0

    def check_chance(self, dices):
        return sum(dices)

roll_service = RollService()
