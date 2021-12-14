class Roll:
    """Class which represents the roll/turn in Yahtzee game

    Attributes:
        dices: list of "dices" used when playing
        keep_dice: list containig information will the user reroll the dice or not
    """
    def __init__(self):
        """Class constructor
        """
        self.dices = [None] * 5
        self.keep_dice = [False] * 5

    def __str__(self):
        return str(self.dices)

roll = Roll()
