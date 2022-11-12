from pathlib import Path


def is_file_type(path: Path, suffix: str) -> bool:
    """
    :param path: The path to the file to check for
    :param suffix: The suffix, to check for, of the file
    :return: True if there is a file at the given path, and that file has the 
    given suffix; otherwise, False
    """
    return path.is_file() and path.suffix == suffix
