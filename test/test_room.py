import unittest
from ascii_loader.exceptions.entity_multi_spawn_error import EntityMultiSpawnError
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
            except EntityMultiSpawnError:
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

    def test_despawn(self):
        def assert_despawn(entity: Entity,
                           num_entities: int,
                           contains_a: bool,
                           contains_b: bool,
                           contains_c: bool,
                           contains_d: bool):
            self.room.despawn(entity)
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
                self.room.despawn(entity)
                self.fail()
            except ValueError:
                self.assertEqual(num_entities, self.room.num_entities())
                self.assertEqual(contains_a, self.room.contains(self.entity_a))
                self.assertEqual(contains_b, self.room.contains(self.entity_b))
                self.assertEqual(contains_c, self.room.contains(self.entity_c))
                self.assertEqual(contains_d, self.room.contains(self.entity_d))

        self.room.spawn(self.entity_a)
        assert_despawn(self.entity_a,
                            0,
                            False,
                            False,
                            False,
                            False)

        self.room.spawn(self.entity_b)
        self.room.spawn(self.entity_c)
        assert_despawn(self.entity_b,
                            1,
                            False,
                            False,
                            True,
                            False)

        self.room.spawn(self.entity_a)
        self.room.spawn(self.entity_b)
        self.room.spawn(self.entity_d)
        assert_despawn(self.entity_a,
                            3,
                            False,
                            True,
                            True,
                            True)

        assert_despawn(self.entity_c,
                            2,
                            False,
                            True,
                            False,
                            True)

        assert_despawn(self.entity_b,
                            1,
                            False,
                            False,
                            False,
                            True)

        assert_despawn(self.entity_d,
                            0,
                            False,
                            False,
                            False,
                            False)

    def test_get(self):
        def assert_get(expected_entity: Entity, index: int):
            self.assertEqual(expected_entity, self.room.get(index))

        def assert_fail(lowest_fail_index: int):
            def fail(index):
                try:
                    self.room.get(index)
                    self.fail()
                except ValueError:
                    pass
            fail(81)
            fail(11)
            fail(7)
            fail(6)
            fail(5)
            fail(4)
            
            for i in range(lowest_fail_index, 4):
                fail(i)

            fail(-1)
            fail(-2)
            fail(-17)
            fail(-23)

        assert_fail(0)

        self.room.spawn(self.entity_b)
        assert_get(self.entity_b, 0)
        assert_fail(1)

        self.room.despawn(self.entity_b)
        assert_fail(0)

        self.room.spawn(self.entity_c)
        self.room.spawn(self.entity_d)
        assert_get(self.entity_d, 1)
        assert_get(self.entity_c, 0)
        assert_fail(2)

        self.room.despawn(self.entity_c)
        assert_get(self.entity_d, 0)
        assert_fail(1)

        self.room.spawn(self.entity_a)
        self.room.spawn(self.entity_b)
        self.room.spawn(self.entity_c)
        assert_get(self.entity_d, 0)
        assert_get(self.entity_a, 1)
        assert_get(self.entity_b, 2)
        assert_get(self.entity_c, 3)
        assert_fail(4)
