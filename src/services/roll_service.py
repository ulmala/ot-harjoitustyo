import random
from entities.roll import (
    roll as default_roll
)

class RollService:
    """Class which handles all funtionalities related to during turn activites

    Attributes:
        roll: instance of Roll class
    """
    def __init__(self, roll=default_roll):
        """Class constructor

        Args:
            roll (Roll, optional): instance of Roll class. Defaults to default_roll.
        """
        self.roll = roll

    def execute_rolls(self, idx):
        """Executes all three rolls/throws for the player. Checks how many
        points are given after that.

        Args:
            idx (int): index of the scoreboard (which row is played at the moment)

        Returns:
            int: points awarded for the player in this turn
        """
        for _ in range(3):
            if all(self.roll.keep_dice):
                break
            self.roll_dices(self.roll)
            self.keep_dices(self.roll, '')
        points = self.check_points(self.roll, idx)
        return points

    def roll_dices(self, roll):
        """Rolls all the dices which player wants to reroll.

        Args:
            dices (list): list of integers representing dice digits
        """
        for i in range(5):
            if not roll.keep_dice[i]:
                roll.dices[i] = random.randint(1,6)
        roll.keep_dices = [False] * 5
        return roll.dices

    def keep_dices(self, roll, dices_to_keep):
        if len(dices_to_keep) == 0:
            return
        for dice in dices_to_keep.split(','):
            roll.keep_dice[int(dice)] = True

    def check_points(self, roll, roll_name):
        """Helper function to call the correct point checking function.

        Args:
            roll (Roll): instacen of Roll class
            roll_name ([type]): roll/turn name

        Returns:
            int: awarded points
        """
        if roll_name == 'Aces':
            return self.check_combination(roll.dices, 1)
        if roll_name == 'Twos':
            return self.check_combination(roll.dices, 2)
        if roll_name == 'Threes':
            return self.check_combination(roll.dices, 3)
        if roll_name == 'Fours':
            return self.check_combination(roll.dices, 4)
        if roll_name == 'Fives':
            return self.check_combination(roll.dices, 5)
        if roll_name == 'Sixes':
            return self.check_combination(roll.dices, 6)
        if roll_name == 'Three of a kind':
            return self.check_three_of_a_kind(roll.dices)
        if roll_name == 'Four of a kind':
            return self.check_four_of_a_kind(roll.dices)
        if roll_name == 'Full house':
            return self.check_full_house(roll.dices)
        if roll_name == 'Small straight':
            return self.check_small_straight(roll.dices)
        if roll_name == 'Large straight':
            return self.check_large_straight(roll.dices)
        if roll_name == 'Yahtzee':
            return self.check_yahtzee(roll.dices)
        if roll_name == 'Chance':
            return self.check_chance(roll.dices)

    def check_combination(self, dices, n):
        """Returns the sum of dice with the number n.
        e.g. return 3 with dices [1,1,1,2,3] when n=1

        Args:
            dices (list): list of integers representing dice digits
            n (int): dice number to be used

        Returns:
            int: sum of dice with the number n
        """
        return dices.count(n) * n

    def check_three_of_a_kind(self, dices):
        """Checks if three of a kind can be constructed from the dices.

        Args:
            dices (list): list of integers representing dice digits

        Returns:
            int: sum of three of a kind (if exists), else 0
        """
        dices.sort()
        if dices[:3].count(dices[0]) == 3:
            return sum(dices[:3])
        if dices[1:4].count(dices[1]) == 3:
            return sum(dices[1:4])
        if dices[2:5].count(dices[2]) == 3:
            return sum(dices[2:5])
        return 0

    def check_four_of_a_kind(self, dices):
        """Checks if four of a kind can be constructed from the dices.

        Args:
            dices (list): list of integers representing dice digits

        Returns:
            int: sum of four of a kind (if exists), else 0
        """
        dices.sort()
        if dices[:4].count(dices[0]) == 4:
            return sum(dices[:4])
        if dices[1:5].count(dices[1]) == 4:
            return sum(dices[1:5])
        return 0

    def check_full_house(self, dices):
        """Checks if full house (two and three same of a kind) can be constructed from the dices.

        Args:
            dices (list): list of integers representing dice digits

        Returns:
            int: 25 points if full house can be constructed, else 0 points
        """
        dices.sort()
        if dices[0] == dices[1] == dices[2] and dices[3] == dices[4] and dices[0] != dices[4]:
            return 25
        if dices[0] == dices[1] and dices[2] ==  dices[3] == dices[4] and dices[0] != dices[4]:
            return 25
        return 0

    def check_small_straight(self, dices):
        """Checks if small straight can be constructed from given dices.

        Args:
            dices (list): list of integers representing dice digits

        Returns:
            int: 30 points if small straight exists, else 0
        """
        dices.sort()
        if all(x in dices for x in [1, 2, 3, 4]):
            return 30
        if all(x in dices for x in [2, 3, 4, 5]):
            return 30
        if all(x in dices for x in [3, 4, 5, 6]):
            return 30
        return 0

    def check_large_straight(self, dices):
        """Checks if large straight can be constructed from given dices.

        Args:
            dices (list): list of integers representing dice digits

        Returns:
            int: 40 points if large straight exists, else 0
        """
        dices.sort()
        if all(x in dices for x in [1, 2, 3, 4, 5]):
            return 40
        if all(x in dices for x in [2, 3, 4, 5, 6]):
            return 40
        return 0

    def check_yahtzee(self, dices):
        """Checks if Yahtzee can be constructed from the dices given as argument.

        Args:
            dices (list): list of integers representing dice digits

        Returns:
            int: 50 points if Yahtzee can be constructed from dices, else 0 points
        """
        if len(set(dices)) == 1:
            return 50
        return 0

    def check_chance(self, dices):
        """Calculates the sum of all dices given as argument.

        Args:
            dices (list): list of integers representing dice digits

        Returns:
            int: sum of all dices, ranges from 5 to 30
        """
        return sum(dices)

roll_service = RollService()
