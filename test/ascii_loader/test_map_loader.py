from pathlib import Path
from typing import Dict, Tuple, Type
import unittest

from ascii_loader.entity import Entity
from ascii_loader.exceptions.map_file_not_found_error import MapFileNotFoundError
from ascii_loader.map_loader import load_map


class EntityA(Entity):
    pass


class EntityB(Entity):
    pass


class EntityC(Entity):
    pass


class EntityD(Entity):
    pass


class EntityE(Entity):
    pass


class EntityF(Entity):
    pass


class EntityG(Entity):
    pass


class EntityH(Entity):
    pass


class EntityI(Entity):
    pass


class EntityJ(Entity):
    pass


class EntityK(Entity):
    pass


class EntityX(Entity):
    pass


class TestMapLoader(unittest.TestCase):
    MAP_DIR = Path(__file__).parent.parent / "data/maps"

    def assert_load_map(self,
                        expected_entities: Tuple[Entity, ...],
                        map_file: Path,
                        char_to_entity_type: Dict[str, Type[Entity]]):
        def assert_pass(expected_entity: Entity, actual_entity: Entity):
            self.assertTrue(isinstance(actual_entity, type(expected_entity)))
            self.assertEqual(expected_entity.x, actual_entity.x)
            self.assertEqual(expected_entity.y, actual_entity.y)

        actual_entities = load_map(map_file, char_to_entity_type)
        [assert_pass(expected_entities[i], actual_entities[i])
            for i in range(max(len(expected_entities), len(actual_entities)))]

    def assert_key_error(self,
                         map_file: Path,
                         char_to_entity_type: Dict[str, Type[Entity]]):
        try:
            load_map(map_file, char_to_entity_type)
            self.fail()
        except KeyError:
            pass

    def assert_map_file_not_found_error(self,
                                        map_file: Path,
                                        char_to_entity_type: Dict[str, Type[Entity]]):
        try:
            load_map(map_file, char_to_entity_type)
            self.fail()
        except MapFileNotFoundError:
            pass

    def test_load_map_empty(self):
        map_file = self.MAP_DIR / "empty.txt"

        def assert_load_map(expected_entities: Tuple[Entity, ...],
                            char_to_entity_type: Dict[str, Type[Entity]]):
            self.assert_load_map(expected_entities,
                                 map_file,
                                 char_to_entity_type)

        assert_load_map((), {})
        assert_load_map((),
                        {
                            '$': EntityA,
                            '|': EntityA,
                            '-': EntityB
                        })
        assert_load_map((),
                        {
                            '$$$$': EntityA,
                            '|asdf': EntityB
                        })

    def test_load_map_valid(self):
        map_file = self.MAP_DIR / "valid.txt"

        def assert_load_map(expected_entities: Tuple[Entity, ...],
                            char_to_entity_type: Dict[str, Type[Entity]]):
            self.assert_load_map(expected_entities,
                                 map_file,
                                 char_to_entity_type)

        def assert_key_error(char_to_entity_type: Dict[str, Type[Entity]]):
            self.assert_key_error(map_file,
                                  char_to_entity_type)

        assert_key_error({})

        assert_key_error({
            'a': EntityA
        })

        assert_key_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC,
            'd': EntityD,
            'e': EntityE,
            'f': EntityF,
            'g': EntityG,
            'h': EntityH,
            'i': EntityI,
            'j': EntityJ,
            'k': EntityK
        })

        assert_key_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC,
            'd': EntityD,
            'e': EntityE,
            'f': EntityF,
            'g': EntityG,
            'h': EntityH,
            'i': EntityI,
            'j': EntityJ,
            'k': EntityK,
            '0': EntityD,
            '1': EntityA,
            '2': EntityB,
            '3': EntityB,
            'X': EntityG,
            ';': EntityI,
            '/': EntityI,
            '?': EntityC,
            '{': EntityK,
            '[': EntityE
        })

        assert_load_map(
            (
                EntityA(0, 0),
                EntityB(1, 0),
                EntityC(2, 0),
                EntityD(3, 0),
                EntityE(4, 0),
                EntityF(5, 0),
                EntityG(6, 0),
                EntityH(7, 0),
                EntityI(8, 0),
                EntityJ(9, 0),
                EntityK(10, 0),
                EntityD(0, 1),
                EntityA(1, 1),
                EntityB(2, 1),
                EntityB(3, 1),
                EntityG(0, 2),
                EntityG(1, 2),
                EntityG(2, 2),
                EntityG(3, 2),
                EntityG(4, 2),
                EntityG(5, 2),
                EntityG(6, 2),
                EntityG(7, 2),
                EntityG(8, 2),
                EntityG(9, 2),
                EntityG(10, 2),
                EntityI(0, 4),
                EntityI(1, 4),
                EntityC(2, 4),
                EntityK(3, 4),
                EntityE(4, 4),
                EntityD(5, 4),
                EntityI(0, 6)
            ),
            {
                'a': EntityA,
                'b': EntityB,
                'c': EntityC,
                'd': EntityD,
                'e': EntityE,
                ']': EntityD,
                'f': EntityF,
                'g': EntityG,
                'h': EntityH,
                'i': EntityI,
                'j': EntityJ,
                'k': EntityK,
                '0': EntityD,
                '1': EntityA,
                '2': EntityB,
                '3': EntityB,
                'X': EntityG,
                ';': EntityI,
                '/': EntityI,
                '?': EntityC,
                '{': EntityK,
                '[': EntityE
            }
        )

        assert_load_map(
            (
                EntityA(0, 0),
                EntityB(1, 0),
                EntityC(2, 0),
                EntityD(3, 0),
                EntityE(4, 0),
                EntityF(5, 0),
                EntityG(6, 0),
                EntityH(7, 0),
                EntityI(8, 0),
                EntityJ(9, 0),
                EntityK(10, 0),
                EntityD(0, 1),
                EntityA(1, 1),
                EntityB(2, 1),
                EntityB(3, 1),
                EntityG(0, 2),
                EntityG(1, 2),
                EntityG(2, 2),
                EntityG(3, 2),
                EntityG(4, 2),
                EntityG(5, 2),
                EntityG(6, 2),
                EntityG(7, 2),
                EntityG(8, 2),
                EntityG(9, 2),
                EntityG(10, 2),
                EntityI(0, 4),
                EntityI(1, 4),
                EntityC(2, 4),
                EntityK(3, 4),
                EntityE(4, 4),
                EntityD(5, 4),
                EntityI(0, 6)
            ),
            {
                'a': EntityA,
                'b': EntityB,
                'c': EntityC,
                'd': EntityD,
                'e': EntityE,
                ']': EntityD,
                'f': EntityF,
                'g': EntityG,
                'h': EntityH,
                'i': EntityI,
                'j': EntityJ,
                'k': EntityK,
                '0': EntityD,
                '1': EntityA,
                '2': EntityB,
                '3': EntityB,
                'X': EntityG,
                ';': EntityI,
                '/': EntityI,
                '?': EntityC,
                '{': EntityK,
                '[': EntityE,
                'Y': EntityA,
                'Z': EntityX
            }
        )

    def test_load_map_invalid(self):
        map_file = self.MAP_DIR / "invalid"

        def assert_map_file_not_found_error(char_to_entity_type: Dict[str, Type[Entity]]):
            self.assert_map_file_not_found_error(map_file,
                                                 char_to_entity_type)

        assert_map_file_not_found_error({})

        assert_map_file_not_found_error({
            'c': EntityC
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC,
            'd': EntityD
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC,
            'd': EntityD,
            'X': EntityA,
            'O': EntityK
        })

    def test_load_map_other_type(self):
        map_file = self.MAP_DIR / "other-type.xml"

        def assert_map_file_not_found_error(char_to_entity_type: Dict[str, Type[Entity]]):
            self.assert_map_file_not_found_error(map_file,
                                                 char_to_entity_type)

        assert_map_file_not_found_error({})

        assert_map_file_not_found_error({
            'c': EntityC
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC,
            'd': EntityD
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC,
            'd': EntityD,
            'X': EntityA,
            'O': EntityK
        })

    def test_load_map_invalid_empty(self):
        map_file = self.MAP_DIR / "invalid_empty"

        def assert_map_file_not_found_error(char_to_entity_type: Dict[str, Type[Entity]]):
            self.assert_map_file_not_found_error(map_file,
                                                 char_to_entity_type)

        assert_map_file_not_found_error({})

        assert_map_file_not_found_error({
            'c': EntityC
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC,
            'd': EntityD
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC,
            'd': EntityD,
            'X': EntityA,
            'O': EntityK
        })

    def test_load_map_no_file_valid(self):
        map_file = self.MAP_DIR / "no_file.txt"

        def assert_map_file_not_found_error(char_to_entity_type: Dict[str, Type[Entity]]):
            self.assert_map_file_not_found_error(map_file,
                                                 char_to_entity_type)

        assert_map_file_not_found_error({})

        assert_map_file_not_found_error({
            'c': EntityC
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC,
            'd': EntityD
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC,
            'd': EntityD,
            'X': EntityA,
            'O': EntityK
        })

    def test_load_map_no_file_invalid_no_extension(self):
        map_file = self.MAP_DIR / "no_file"

        def assert_map_file_not_found_error(char_to_entity_type: Dict[str, Type[Entity]]):
            self.assert_map_file_not_found_error(map_file,
                                                 char_to_entity_type)

        assert_map_file_not_found_error({})

        assert_map_file_not_found_error({
            'c': EntityC
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC,
            'd': EntityD
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC,
            'd': EntityD,
            'X': EntityA,
            'O': EntityK
        })

    def test_load_map_no_file_invalid(self):
        map_file = self.MAP_DIR / "no_file.xml"

        def assert_map_file_not_found_error(char_to_entity_type: Dict[str, Type[Entity]]):
            self.assert_map_file_not_found_error(map_file,
                                                 char_to_entity_type)

        assert_map_file_not_found_error({})

        assert_map_file_not_found_error({
            'c': EntityC
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC,
            'd': EntityD
        })

        assert_map_file_not_found_error({
            'a': EntityA,
            'b': EntityB,
            'c': EntityC,
            'd': EntityD,
            'X': EntityA,
            'O': EntityK
        })
