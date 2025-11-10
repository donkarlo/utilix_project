from utilix.data.storage.storage import Storage
from utilix.os.path.path import Path
import os


class File(Storage):
    def __init__(self, path: Path):

        # absolute normalized Path
        native_path = Path(path.get_native_absolute_path())
        parent_dir = Path(path.get_parent_directory())

        # ensure parent directory exists
        if not parent_dir.dir_exists():
            parent_dir.create_missing_directories()

        # ensure file exists
        if not native_path.file_exists():
            with open(native_path.get_native_absolute_path(), "w", encoding="utf-8"):
                pass

        self._path: Path = native_path

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
