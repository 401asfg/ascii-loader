from pathlib import Path
import unittest
from ascii_loader.room_loader import RoomLoader

from ascii_loader.utils import ROOT_DIR


class TestRoomLoader(unittest.TestCase):
    LOADING_DIRECTORY = ROOT_DIR / "test/rooms"

    room_loader: RoomLoader

    def setUp(self) -> None:
        self.room_loader = RoomLoader(self.LOADING_DIRECTORY)

    def test_init(self):
        self.assertEqual(self.LOADING_DIRECTORY,
                         self.room_loader.loading_directory)

    def test_load(self):
        # TODO: write
        pass
