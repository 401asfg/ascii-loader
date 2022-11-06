# TODO: should this be abstract?


class Entity:
    """
    An object that can be added to a map
    """

    _x: int
    _y: int

    def __init__(self, x: int, y: int):
        """
        Initializes the class

        :param x: The entity's x position in a map
        :param y: The entity's y position in a map

        :raise ValueError: If the x or y are less than 0
        """
        if x < 0 or y < 0:
            raise ValueError("Tried to create an entity with negative coordinates")

        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y
