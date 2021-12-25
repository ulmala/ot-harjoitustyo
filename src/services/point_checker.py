from functools import partial


class PointChecker:
    """Class is responsible for checking points in the game.

    Attributes:
        dispatcher: list which holds all the point checking function. Based on the index
        of the function, right function can be called in the game.
        
    """
    def __init__(self):
        """Class constructor
        """
        self.dispatcher = []
        for i in range(1,7):
            self.dispatcher.append(partial(
                self._check_combination, n=i
            ))
        self.dispatcher.append(self._check_bonus)
        self.dispatcher.append(self._check_three_of_a_kind)
        self.dispatcher.append(self._check_four_of_a_kind)
        self.dispatcher.append(self._check_full_house)
        self.dispatcher.append(self._check_small_straight)
        self.dispatcher.append(self._check_large_straight)
        self.dispatcher.append(self._check_yahtzee)
        self.dispatcher.append(self._check_chance)

    def _check_combination(self, dices, n):
        """Returns the sum of dice with the number n.
        e.g. return 3 with dices [1,1,1,2,3] when n=1
        Args:
            dices (list): list of integers representing dice digits
            n (int): dice number to be used
        Returns:
            int: sum of dice with the number n
        """
        return dices.count(n) * n

    def _check_bonus(self, player, scoreboard):
        """Checks if the player is allowed to have bonus points based on the points
        of first six rows in scoreboard. If the sum of first six rows is equal or
        greater than 63, player will have 50 bonus points.

        Args:
            player (Player): player whos bonus will be checked
            scoreboard ([type]): scoreboard of current game

        Returns:
            int: 50 if player is allowed to have bonus, else 0
        """
        if scoreboard[player][:6].sum() >= 63:
            return 50
        return 0

    def _check_three_of_a_kind(self, dices):
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

    def _check_four_of_a_kind(self, dices):
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

    def _check_full_house(self, dices):
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

    def _check_small_straight(self, dices):
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

    def _check_large_straight(self, dices):
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

    def _check_yahtzee(self, dices):
        """Checks if Yahtzee can be constructed from the dices given as argument.
        Args:
            dices (list): list of integers representing dice digits
        Returns:
            int: 50 points if Yahtzee can be constructed from dices, else 0 points
        """
        if len(set(dices)) == 1:
            return 50
        return 0

    def _check_chance(self, dices):
        """Calculates the sum of all dices given as argument.
        Args:
            dices (list): list of integers representing dice digits
        Returns:
            int: sum of all dices, ranges from 5 to 30
        """
        return sum(dices)

point_checker = PointChecker()
