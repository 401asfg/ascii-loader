import json
from pathlib import Path
from typing import Dict, List, Tuple, Type, TypeVar
from xml.dom.minidom import Entity
from importlib import import_module

from ascii_loader.exceptions.entity_key_file_not_found_error import EntityKeyFileNotFoundError
from ascii_loader.utils import is_file_type

# TODO: implement and test


T = TypeVar("T", bound=Entity)

ENTITY_KEY_FILE_SUFFIX = ".json"

ENTITY_KEY_CHARACTER_KEY = "character"
ENTITY_KEY_MODULE_NAME_KEY = "module_name"
ENTITY_KEY_CLASS_NAME_KEY = "class_name"


def load_entity_key(entity_key_file: Path) -> Dict[str, Type[T]]:
    """
    Load an entity key from the given entity_key_file

    :param file: The file to load the entity key from
    :return: The ascii characters paired with their entity types, described by the given entity_key_file
    
    :raise CharKeyFileNotFoundError: If the given entity_key_file path doesn't lead to a file with a 
    suffix matching ENTITY_KEY_FILE_SUFFIX
    :raise ImportError: If one of the entries in the given entity_key_file doesn't have a valid value 
    in it's ENTITY_KEY_MODULE_NAME_KEY field
    :raise AttributeError: If one of the entries in the given entity_key_file doesn't have a valid value 
    in it's ENTITY_KEY_CLASS_NAME_KEY field
    """
    if not is_file_type(entity_key_file, ENTITY_KEY_FILE_SUFFIX):
        raise EntityKeyFileNotFoundError(
            f"No valid file found while attempting to load a {ENTITY_KEY_FILE_SUFFIX} entity key file")

    def read_entity_key() -> List[Dict[str, str]]:
        file_contents: List[Dict[str, str]] = []

        with open(entity_key_file, 'r') as f:
            file_contents = json.load(f)

        return file_contents

    def import_entity_type(entity_key_entry: Dict[str, str]) -> Type[T]:
        module_name = entity_key_entry[ENTITY_KEY_MODULE_NAME_KEY]
        class_name = entity_key_entry[ENTITY_KEY_CLASS_NAME_KEY]

        entity_module = import_module(module_name)
        entity_type = getattr(entity_module, class_name)

        return entity_type

    def create_char_to_entity_type_entry(entity_key_entry: Dict[str, str]) -> Tuple[str, Type[T]]:
        character = entity_key_entry[ENTITY_KEY_CHARACTER_KEY]
        entity_type = import_entity_type(entity_key_entry)
        return character, entity_type

    def create_char_to_entity_type_dict(entity_key: List[Dict[str, str]]) -> Dict[str, Type[T]]:
        return dict([create_char_to_entity_type_entry(entity_key_entry)
                     for entity_key_entry in entity_key])

    return create_char_to_entity_type_dict(read_entity_key())
