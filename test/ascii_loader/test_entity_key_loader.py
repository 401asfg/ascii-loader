from pathlib import Path
from typing import Dict, Type
import unittest

from ascii_loader.entity import Entity
from ascii_loader.entity_key_loader import load_entity_key
from ascii_loader.exceptions.entity_key_file_not_found_error import EntityKeyFileNotFoundError


class TestEntityKeyLoader(unittest.TestCase):
    ENTITY_KEY_DIR = Path(__file__).parent.parent / "data/entity_keys"

    def assert_load_entity_key(self,
                               expected_dict: Dict[str, Type[Entity]],
                               entity_key_file: Path):
        actual_dict = load_entity_key(entity_key_file)
        self.assertEqual(expected_dict, actual_dict)

    def assert_entity_key_file_not_found_error(self,
                                               entity_key_file: Path):
        try:
            load_entity_key(entity_key_file)
            self.fail()
        except EntityKeyFileNotFoundError:
            pass

    def assert_import_error(self, entity_key_file: Path):
        try:
            load_entity_key(entity_key_file)
            self.fail()
        except ImportError:
            pass

    def assert_attribute_error(self, entity_key_file: Path):
        try:
            load_entity_key(entity_key_file)
            self.fail()
        except AttributeError:
            pass

    # def test_load_entity_key_valid(self):
    #     # TODO: write

    # def test_load_entity_key_invalid(self):
    #     # TODO: write

    # def test_load_entity_key_other_types(self):
    #     # TODO: write

    # def test_load_entity_key_invalid_empty(self):
    #     # TODO: write

    # def test_load_entity_key_no_file_valid(self):
    #     # TODO: write

    # def test_load_entity_key_no_file_invalid_no_extension(self):
    #     # TODO: write

    # def test_load_entity_key_no_file_invalid_with_extension(self):
    #     # TODO: write

    # TODO: write tests based on test map loader's layout
