from pathlib import Path
from typing import Dict, List, Tuple, Type, TypeVar

from ascii_loader.entity import Entity
from ascii_loader.exceptions.map_file_not_found_error import MapFileNotFoundError
from ascii_loader.utils import is_file_type

# TODO: test


T = TypeVar("T", bound=Entity)

MAP_FILE_SUFFIX = ".txt"


def load_map(map_file: Path,
             char_to_entity_type: Dict[str, Type[T]],
             empty_space_char=' ') -> Tuple[T, ...]:
    """
    Load a map from the given file using the given char_to_entity_type

    :param file: The file to load the ascii map from
    :param char_to_entity_type: A key describing what type of entity each character from the given map_file represents
    :param empty_space_char: A character that is used only to space out the map and won't be loaded as an entity
    :return: The entities that were described by the given map_file and the given char_to_entity_type

    :raise MapFileNotFoundError: If the given map_file path doesn't lead to a file with a suffix matching MAP_FILE_SUFFIX
    :raise KeyError: If given map_file contains a character that isn't also a key in the given char_to_entity_type 
    dictionary
    """
    if not is_file_type(map_file, MAP_FILE_SUFFIX):
        raise MapFileNotFoundError(f"No valid file found while attempting to load a {MAP_FILE_SUFFIX} map file")

    def read_map() -> List[str]:
        file_contents = ""

        with open(map_file, 'r') as f:
            file_contents = f.read().splitlines()

        return file_contents

    def create_entity(char: str, x: int, y: int) -> T:
        entity_type = char_to_entity_type[char]
        return entity_type(x, y)

    def create_entity_row(char_row: str, y: int) -> List[T]:
        return [create_entity(char_row[x], x, y)
                for x in range(len(char_row))
                if char_row[x] != empty_space_char]

    def create_entities(char_rows: List[str]) -> List[T]:
        return sum([create_entity_row(char_rows[y], y)
                    for y in range(len(char_rows))],
                   [])

    return tuple(create_entities(read_map()))
