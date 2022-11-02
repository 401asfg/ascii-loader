from typing import List
from ascii_loader.entity import Entity
from ascii_loader.exceptions.entity_multi_spawn_error import EntityMultiSpawnError


class Room:
    """
    A space that contains entities
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
        :raise EntityMultiSpawnError: If the given entity is already contained within the room
        """
        if self.contains(entity):
            raise EntityMultiSpawnError("Attempted to spawn the same instance of an entity while it \
                                           was already contained in the room")

        self._entities.append(entity)

    def despawn(self, entity: Entity):
        """
        Despawns the given entity from the room

        :param entity: The entity to despawn
        :raise ValueError: If the room doesn't contain the given entity
        """
        self._entities.remove(entity)

    def get(self, index: int) -> Entity:
        """
        :param index: The index of the entity to get
        :return: The entity at the given index in the room

        :raise ValueError: If the given index is less than 0, or greater than or equal to num_entities()
        """
        if index < 0 or index >= self.num_entities():
            raise ValueError("Attempted to access an entity in a room with an index that didn't \
                             correspond to any entity")

        return self._entities[index]

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
