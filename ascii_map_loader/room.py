from typing import List
from ascii_map_loader.entity import Entity
from ascii_map_loader.exceptions.double_spawned_entity_error import DoubleSpawnedEntityError


class Room:
    """
    A 2D space that contains entities
    """

    _entities: List[Entity]

    def __init__(self):
        """
        Initializes the class
        """
        self._entities = []

    def spawn(self, entity: Entity):
        """
        Spawns the given entity in the room
        
        :param entity: The entity to spawn
        :raise DoubleSpawnedEntityError: If the given entity is already contained within the room
        """
        if self.contains(entity):
            raise DoubleSpawnedEntityError("Attempted to spawn the same instance of an entity while it \
                                           was already contained in the room")

        self._entities.append(entity)

    def num_entities(self) -> int:
        """
        :return: The number of entities on the room
        """
        return len(self._entities)

    def contains(self, entity: Entity) -> bool:
        """
        :param entity: The entity to check the room for
        :return: True if the given entity is contained in this room; otherwise, False
        """
        return entity in self._entities
