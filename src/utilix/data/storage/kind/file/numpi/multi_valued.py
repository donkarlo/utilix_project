from typing import Any
import numpy as np

from utilix.data.storage.decorator.multi_valued.interface import Interface as MultiValuedBaseStorageInterface
from utilix.os.file_system.file.file import File as OsFile
from utilix.data.storage.kind.file.file import File as FileStorage


class MultiValued(FileStorage, MultiValuedBaseStorageInterface):
    """
    """

    def __init__(self, os_file: OsFile, create_directory_structure: bool):
        FileStorage.__init__(self, os_file, create_directory_structure)

    def load(self) -> Any:
        file_path = self.get_path().get_native_absolute_string_path()
        ram = np.load(file_path)
        FileStorage.set_ram(self, ram["arr_0"])
        return self._ram

    def save(self) -> None:
        file_path = self.get_path().get_native_absolute_string_path()
        np.savez(file_path,self.get_ram())