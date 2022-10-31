from pathlib import Path

from ascii_loader.room import Room


# TODO: implement and test


class RoomLoader:
    """
    Loads rooms from .txt files
    """

    def __init__(self, loading_directory: Path):
        """
        Initializes the class

        :param loading_directory: The path to the directory that holds the .txt files to load rooms from
        """
        pass

    def load(self, file_name: str) -> Room:
        """
        Load a room from the file with the given file_name

        :param file_name: The name of the file to load a room from
        :return: A room, loaded from the file of the given file_name

        :raise FileNotFoundError: If there is no file with the given file_name
        """
        return None

    @property
    def loading_directory(self) -> Path:
        return None
