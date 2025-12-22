from utilix.data.kind.dic.dic import Dic
from utilix.data.storage.kind.file.file import File as FileStorage
from utilix.data.storage.interface import Interface as StorageInterface
from utilix.os.file_system.file.file import File as OsFile
import yaml

class Yaml(FileStorage, StorageInterface):
    """
   """

    def __init__(self, os_file: OsFile, create_directory_structure: bool):
        FileStorage.__init__(self, os_file, create_directory_structure)

    def load(self) -> Dic:
        with open(self._os_file.get_path().get_native_absolute_string_path(), "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        self._ram = Dic(data)
        return self._ram

    def __getitem__(self, item):
        return self._ram[item]

    def __ittr__(self):
        return iter(self._ram)

    def save(self) -> None:
        pass

    def earase_storage(self) -> None:
        pass

    def delete_storage(self) -> None:
        pass