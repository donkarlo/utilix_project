from utilix.data.storage.type.file.format.format import Format
from utilix.data.storage.basic import Basic
from utilix.os.path import Path


class File(Basic):
    def __init__(self, path:Path):
        self._path:Path = path
        super().__init__()

    def get_path(self)->Path:
        return self._path

    def get_native_absolute_path(self)->str:
        return self._path.get_native_absolute_path()

    def load(self) -> None:
        with open(self._path.get_native_absolute_path(), "r", encoding="utf-8") as file:
            self._ram = file.read()

    def save(self):
        with open(self._path.get_native_absolute_path(), "w", encoding="utf-8") as file:
            file.write(self._path.get_native_absolute_path())