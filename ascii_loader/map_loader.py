from pathlib import Path
from typing import Dict, List, Tuple, Type

from ascii_loader.entity import Entity
from ascii_loader.exceptions.map_file_not_found_error import MapFileNotFoundError

# TODO: implement and test
# TODO: add spritemap_file param
# TODO: make a function?
# TODO: use this code to dynamically import entity types
# import importlib
# module = importlib.import_module(module_name)
# class_ = getattr(module, class_name)
# instance = class_()


MAP_FILE_SUFFIX = ".txt"


def load_map(map_file: Path, char_to_entity_type: Dict[str, Type[Entity]]) -> Tuple[Entity, ...]:
    """
    Load a map from the given map_file using the given char_to_entity_type

    :param map_file: The .txt file to load the ascii map from
    :param char_to_entity_type: A key describing what type of entity each character from the given map_file represents
    :return: The entities that were described by the given map_file and the given char_to_entity_type

    :raise MapFileNotFoundError: If the given map_file path doesn't lead to a file with a suffix matching MAP_FILE_SUFFIX
    """
    if not map_file.is_file() or map_file.suffix != MAP_FILE_SUFFIX:
        raise MapFileNotFoundError(f"No valid file found while attempting to load a {MAP_FILE_SUFFIX} map file")

    def read_map() -> List[str]:
        f = open(map_file, mode='r')
        file_contents = f.readlines()
        f.close()
        return file_contents

    def create_entity(char: str, x: int, y: int) -> Entity:
        entity_type = char_to_entity_type[char]
        return entity_type(x, y)

    def create_entity_row(char_row: str, y: int) -> List[Entity]:
        return [create_entity(char_row[x], x, y)
                for x in range(len(char_row))]

    def create_entities(char_rows: List[str]) -> List[Entity]:
        return sum([create_entity_row(char_rows[y], y)
                    for y in range(len(char_rows))])

    return tuple(create_entities(read_map()))
