import unittest
from ascii_loader.room_loader import RoomLoader

from ascii_loader.utils import ROOT_DIR


class TestRoomLoader(unittest.TestCase):
    DATA_DIR = ROOT_DIR / "test/data"
    LOADING_DIR = DATA_DIR / "rooms"

    room_loader: RoomLoader

    def setUp(self) -> None:
        self.room_loader = RoomLoader(self.LOADING_DIR)

    def test_init(self):
        self.assertEqual(self.LOADING_DIR,
                         self.room_loader.loading_dir)

    def test_load(self):
        # TODO: write
        pass
