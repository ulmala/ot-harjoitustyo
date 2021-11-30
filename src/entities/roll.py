class Roll:
    def __init__(self):
        self.dices = [None] * 5
        self.keep_dice = [False] * 5

    def __str__(self):
        return str(self.dices)
