import unittest
from ascii_loader.entity import Entity

class TestEntity(unittest.TestCase):
    def test_init(self):
        def assert_init(x, y):
            entity = Entity(x, y)
            self.assertEqual(x, entity.x)
            self.assertEqual(y, entity.y)

        assert_init(0, 0)
        assert_init(34, 0)
        assert_init(0, 8)
        assert_init(593, 6)
        assert_init(11, 3)
        assert_init(787, 787)

        def assert_fail(x, y):
            try:
                Entity(x, y)
                self.fail()
            except ValueError:
                pass

        assert_fail(-1, 0)
        assert_fail(0, -1)
        assert_fail(-1, -1)
        assert_fail(-34, -9)
