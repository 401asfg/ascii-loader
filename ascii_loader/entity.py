# TODO: should this be abstract?


class Entity:
    """
    An object that is loaded from a map
    """

    _x: int
    _y: int

    def __init__(self, x: int, y: int):
        """
        Initializes the class

        :param x: The entity's x position in a map
        :param y: The entity's y position in a map
        """
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y
