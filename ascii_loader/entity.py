from abc import ABC


class Entity(ABC):
    """
    An object that is loaded from a map
    """

    x: int
    y: int

    def __init__(self, x: int, y: int):
        """
        Initializes the class

        :param x: The entity's x position in a map
        :param y: The entity's y position in a map
        """
        self.x = x
        self.y = y
