import pickle

from utilix.data.storage.interface import Interface as StorageInterface
from utilix.os.file_system.file.file import File as OsFile
from utilix.data.storage.kind.file.file import File as FileStorage

class Pkl(FileStorage, StorageInterface):
    """
    """
    def __init__(self, os_file:OsFile, create_directory_structure: bool):
        FileStorage.__init__(self, os_file, create_directory_structure)

    def load(self) -> None:
        pass

    def save(self) -> None:
        with open(self.get_path().get_native_absolute_string_path(), "wb") as f:
            ram = self.get_ram()
            pickle.dump(self.get_ram(), f, protocol=pickle.HIGHEST_PROTOCOL)

    def earase_storage(self) -> None:
        pass

    def delete_storage(self) -> None:
        pass