import unittest
from pathlib import Path

from ascii_loader.utils import is_file_type


class TestUtils(unittest.TestCase):
    def test_is_file_type(self):
        self.assertTrue(is_file_type(Path(__file__), '.py'))
        self.assertFalse(is_file_type(Path(__file__), ''))
        self.assertFalse(is_file_type(Path(__file__), '.json'))
        self.assertFalse(is_file_type(Path(__file__), '.txt'))

        self.assertFalse(is_file_type(Path(__file__).parent, ''))
        self.assertFalse(is_file_type(Path(__file__).parent, '.py'))
        self.assertFalse(is_file_type(Path(__file__).parent, '.json'))
        self.assertFalse(is_file_type(Path(__file__).parent, '.txt'))

        self.assertTrue(is_file_type(Path(__file__).parent / "__init__.py", '.py'))
        self.assertFalse(is_file_type(Path(__file__).parent / "__init__.py", ''))
        self.assertFalse(is_file_type(Path(__file__).parent / "__init__.py", '.json'))
        self.assertFalse(is_file_type(Path(__file__).parent / "__init__.py", '.txt'))

        self.assertTrue(is_file_type(Path(__file__).parent.parent / "data/maps/empty.txt", '.txt'))
        self.assertFalse(is_file_type(Path(__file__).parent.parent / "data/maps/empty.txt", ''))
        self.assertFalse(is_file_type(Path(__file__).parent.parent / "data/maps/empty.txt", '.py'))
        self.assertFalse(is_file_type(Path(__file__).parent.parent / "data/maps/empty.txt", '.json'))


if __name__ == '__main__':
    unittest.main()
