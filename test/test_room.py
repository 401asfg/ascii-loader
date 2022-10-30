import unittest
from ascii_loader.exceptions.double_spawned_entity_error import DoubleSpawnedEntityError
from ascii_loader.room import Room
from ascii_loader.entity import Entity

class TestRoom(unittest.TestCase):
    X_A = 0
    Y_A = 0
    entity_a: Entity

    X_B = 9
    Y_B = 6
    entity_b: Entity

    X_C = 12
    Y_C = 1
    entity_c: Entity

    X_D = 35
    Y_D = 33
    entity_d: Entity

    room: Room

    def setUp(self) -> None:
        self.entity_a = Entity(self.X_A, self.Y_A)
        self.entity_b = Entity(self.X_B, self.Y_B)
        self.entity_c = Entity(self.X_C, self.Y_C)
        self.entity_d = Entity(self.X_D, self.Y_D)

        self.room = Room()

    def test_init(self):
        self.assertEqual(0, self.room.num_entities())
        self.assertFalse(self.room.contains(self.entity_a))
        self.assertFalse(self.room.contains(self.entity_b))
        self.assertFalse(self.room.contains(self.entity_c))
        self.assertFalse(self.room.contains(self.entity_d))

    def test_spawn(self):
        def assert_spawn(entity: Entity,
                         num_entities: int,
                         contains_a: bool,
                         contains_b: bool,
                         contains_c: bool,
                         contains_d: bool):
            self.room.spawn(entity)
            self.assertEqual(num_entities, self.room.num_entities())
            self.assertEqual(contains_a, self.room.contains(self.entity_a))
            self.assertEqual(contains_b, self.room.contains(self.entity_b))
            self.assertEqual(contains_c, self.room.contains(self.entity_c))
            self.assertEqual(contains_d, self.room.contains(self.entity_d))

        def assert_fail(entity: Entity,
                        num_entities: int,
                        contains_a: bool,
                        contains_b: bool,
                        contains_c: bool,
                        contains_d: bool):
            try:
                self.room.spawn(entity)
                self.fail()
            except DoubleSpawnedEntityError:
                self.assertEqual(num_entities, self.room.num_entities())
                self.assertEqual(contains_a, self.room.contains(self.entity_a))
                self.assertEqual(contains_b, self.room.contains(self.entity_b))
                self.assertEqual(contains_c, self.room.contains(self.entity_c))
                self.assertEqual(contains_d, self.room.contains(self.entity_d))

        assert_spawn(self.entity_a,
                   1,
                   True,
                   False,
                   False,
                   False)

        assert_fail(self. entity_a,
                    1,
                    True,
                    False,
                    False,
                    False)

        assert_spawn(self.entity_c,
                     2,
                     True,
                     False,
                     True,
                     False)

        assert_fail(self.entity_c,
                    2,
                    True,
                    False,
                    True,
                    False)

        assert_fail(self.entity_a,
                    2,
                    True,
                    False,
                    True,
                    False)

        assert_spawn(self.entity_b,
                     3,
                     True,
                     True,
                     True,
                     False)

        assert_fail(self.entity_a,
                    3,
                    True,
                    True,
                    True,
                    False)

        assert_fail(self.entity_b,
                    3,
                    True,
                    True,
                    True,
                    False)

        assert_fail(self.entity_c,
                    3,
                    True,
                    True,
                    True,
                    False)

        assert_spawn(self.entity_d,
                     4,
                     True,
                     True,
                     True,
                     True)

        assert_fail(self.entity_a,
                    4,
                    True,
                    True,
                    True,
                    True)

        assert_fail(self.entity_b,
                    4,
                    True,
                    True,
                    True,
                    True)

        assert_fail(self.entity_c,
                    4,
                    True,
                    True,
                    True,
                    True)

        assert_fail(self.entity_d,
                    4,
                    True,
                    True,
                    True,
                    True)
