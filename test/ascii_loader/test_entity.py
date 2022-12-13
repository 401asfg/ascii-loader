import unittest

from ascii_loader import Entity


class MockEntity(Entity):
    ...


class TestEntity(unittest.TestCase):
    XA = 0
    YA = 0

    XB = 37
    YB = 9

    XC = -7
    YC = -87

    entity_a: MockEntity
    entity_b: MockEntity
    entity_c: MockEntity

    def setUp(self) -> None:
        self.entity_a = MockEntity(self.XA, self.YA)
        self.entity_b = MockEntity(self.XB, self.YB)
        self.entity_c = MockEntity(self.XC, self.YC)

    def test_init(self):
        def assert_init(entity, x, y):
            self.assertEqual(x, entity.x)
            self.assertEqual(y, entity.y)

        assert_init(self.entity_a, self.XA, self.YA)
        assert_init(self.entity_b, self.XB, self.YB)
        assert_init(self.entity_c, self.XC, self.YC)


if __name__ == '__main__':
    unittest.main()
