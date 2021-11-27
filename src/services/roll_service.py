import random
from entities import game
from entities.roll import Roll

class RollService:

    def execute_rolls(self, idx):
        roll = Roll()
        for _ in range(3):
            if all(roll.keep_dice):
                break
            self.roll_dices(roll)
            print('Tässä ovat nopat: ', roll.dices)
            dices_to_keep = input('Mitkä nopat haluat pitää?')
            self.keep_dices(roll, dices_to_keep)
        points = self.check_points(roll, idx)
        return points

    def roll_dices(self, roll):
        for i in range(5):
            if not roll.keep_dice[i]:
                roll.dices[i] = random.randint(1,6)
        roll.keep_dices = [False] * 5

    def keep_dices(self, roll, dices_to_keep):
        if len(dices_to_keep) == 0:
            return
        for dice in dices_to_keep.split(','):
            roll.keep_dice[int(dice)] = True

    def check_points(self, roll, roll_name):
        if roll_name == 'Aces':
            return self.check_combination(roll.dices, 1)
        elif roll_name == 'Twos':
            return self.check_combination(roll.dices, 2)
        elif roll_name == 'Threes':
            return self.check_combination(roll.dices, 3)
        elif roll_name == 'Fours':
            return self.check_combination(roll.dices, 4)
        elif roll_name == 'Fives':
            return self.check_combination(roll.dices, 5)
        elif roll_name == 'Sixes':
            return self.check_combination(roll.dices, 6)    

    def check_combination(self, dices, n):
        return dices.count(n) * n

    def check_three_of_a_kind(self, dices):
        dices.sort()
        if dices[:3].count(dices[0]) == 3:
            return sum(dices[:3])
        elif dices[1:4].count(dices[1]) == 3:
            return sum(dices[1:4])
        elif dices[2:5].count(dices[2]) == 3:
            return sum(dices[2:5])
        return 0

    def check_four_of_a_kind(self, dices):
        dices.sort()
        if dices[:4].count(dices[0]) == 4:
            return sum(dices[:4])
        elif dices[1:5].count(dices[1]) == 4:
            return sum(dices[1:5])
        return 0

    def check_full_house(self, dices):
        dices.sort()
        if dices[0] == dices[1] == dices[2] and dices[3] == dices[4] and dices[0] != dices[4]:
            return 25
        elif dices[0] == dices[1] and dices[2] ==  dices[3] == dices[4] and dices[0] != dices[4]:
            return 25
        return 0

    def check_small_straight(self, dices):
        dices.sort()
        if all(x in dices for x in [1, 2, 3, 4]):
            return 30
        elif all(x in dices for x in [2, 3, 4, 5]):
            return 30
        elif all(x in dices for x in [3, 4, 5, 6]):
            return 30
        return 0

    def check_large_straight(self, dices):
        dices.sort()
        if all(x in dices for x in [1, 2, 3, 4, 5]):
            return 40
        elif all(x in dices for x in [2, 3, 4, 5, 6]):
            return 40
        return 0

    def check_yahtzee(self, dices):
        if len(set(dices)) == 1:
            return 50
        return 0

    def check_chance(self, dices):
        return sum(dices)

roll_service = RollService()
