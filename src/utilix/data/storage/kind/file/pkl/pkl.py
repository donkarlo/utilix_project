import pickle
from typing import Any

from utilix.data.storage.interface import Interface as StorageInterface
from utilix.os.file_system.file.file import File as OsFile
from utilix.data.storage.kind.file.file import File as FileStorage

class Pkl(FileStorage, StorageInterface):
    """
    """
    def __init__(self, os_file:OsFile, create_directory_structure: bool):
        FileStorage.__init__(self, os_file, create_directory_structure)

    def load(self) -> Any:
        file_path = self.get_path().get_native_absolute_string_path()
        with open(file_path, "rb") as opened_file:
            ram = pickle.load(opened_file)
        return ram

    def save(self) -> None:
        with open(self.get_path().get_native_absolute_string_path(), "wb") as opened_file:
            pickle.dump(self.get_ram(), opened_file, protocol=pickle.HIGHEST_PROTOCOL)

    def earase(self) -> None:
        pass

    def delete(self) -> None:
        pass