from pathlib import Path
import unittest


class TestEntityKeyLoader(unittest.TestCase):
    ENTITY_KEY_DIR = Path(__file__).parent.parent / "data/entity_keys"

    # TODO: write tests based on test map loader's layout
