from utilix.data.storage.storage import Storage
from utilix.os.file_system.path.path import Path


class File(Storage):
    def __init__(self, path:Path, create_directory_structure:bool):

        if create_directory_structure == True:
            # absolute normalized Path
            parent_dir = Path(path.get_parent_directory_string_path())

            # ensure parent directory exists
            if not parent_dir.directory_exists():
                parent_dir.create_missing_directories()

            # ensure file exists
            if not path.file_exists():
                with open(path.get_native_absolute_path(), "w", encoding="utf-8"):
                    pass

        self._path = path

    def get_path(self) -> Path:
        return self._path

    def get_native_absolute_path(self) -> str:
        return self._path.get_native_absolute_path()

    def load(self) -> None:
        with open(self.get_native_absolute_path(), "r", encoding="utf-8") as file:
            self._ram = file.read()

    def save(self):
        with open(self.get_native_absolute_path(), "w", encoding="utf-8") as file:
            file.write(self._ram)
