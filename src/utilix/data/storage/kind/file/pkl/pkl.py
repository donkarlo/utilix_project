from utilix.data.storage.interface import Interface as StorageInterface
from utilix.os.file_system.file.file import File as OsFile
from utilix.data.storage.kind.file.file import File as FileStorage

class Pkl(FileStorage, StorageInterface):
    """
    """
    def __init__(self, os_file:OsFile, create_directory_structure: bool):
        super().__init__(os_file, create_directory_structure)

    def load(self) -> None:
        pass

    def save(self) -> None:
        pass

    def earase_storage(self) -> None:
        pass

    def delete_storage(self) -> None:
        pass