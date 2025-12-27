from copy import deepcopy
from typing import overload, Union
from utilix.data.storage.interface import Interface as StorageInterface
from utilix.data.storage.storage import Storage
from utilix.os.file_system.file.file import File as OsFile
from utilix.os.file_system.path.file import Path as FilePath
from utilix.os.file_system.path.directory import Directory as DirPath


class File(Storage, StorageInterface):

    def __init__(self, os_file:OsFile, create_directory_structure: bool):

        self._os_file = os_file
        path = self._os_file.get_path()

        if create_directory_structure == True:
            # absolute normalized Path
            parent_dir_path = DirPath(path.get_parent_directory_string_path())

            # ensure parent directory exists
            if not parent_dir_path.directory_exists():
                parent_dir_path.create_missing_directories()

            # ensure file exists - this creates the file if it doesnt exist
            if not path.file_exists():
                with open(path.get_native_absolute_string_path(), "w", encoding="utf-8"):
                    pass
        elif create_directory_structure == False and not path.file_exists():
            raise FileNotFoundError(f"File {path.get_native_absolute_string_path()} not exist")

        self._path = path
        Storage.__init__(self)

    def get_path(self) -> FilePath:
        return self._path

    def get_native_absolute_string_path(self) -> str:
        return self._path.get_native_absolute_string_path()

    def load(self) -> None:
        with open(self.get_native_absolute_string_path(), "r", encoding="utf-8") as file:
            self._ram = file.read()

    def save(self):
        with open(self.get_native_absolute_string_path(), "w", encoding="utf-8") as file:
            file.write(self._ram)
