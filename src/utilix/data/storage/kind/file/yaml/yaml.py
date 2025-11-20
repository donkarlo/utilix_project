from utilix.data.storage.storage import Storage
from utilix.data.storage.interface import Interface as StorageInterface
from utilix.os.file_system.file.file import File as OsFile

class Yaml(Storage, StorageInterface):
    """
   """


def __init__(self, os_file: OsFile):
    self._os_file = os_file

def load(self) -> None:
    pass

def save(self) -> None:
    pass

def earase_storage(self) -> None:
    pass

def delete_storage(self) -> None:
    pass