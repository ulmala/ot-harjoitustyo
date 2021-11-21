import random

class Roll:
    def __init__(self):
        self.dices = [None] * 5
        self.keep_dice = [False] * 5

    def __srt__(self):
        return str(self.dices)