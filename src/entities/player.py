class Player:
    """Class which represents the player in the game.

    Attributes:
        name: name of the player
    """
    def __init__(self, name):
        """Class consturctor

        Args:
            name (str): name of the plauer
        """
        self.name = name

    def __str__(self):
        return self.name


