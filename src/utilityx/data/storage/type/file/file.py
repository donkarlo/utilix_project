from utilityx.data.storage.basic import Basic
from utilityx.os.path import Path


class File(Basic):
    def __init__(self, path:Path):
        self._path = path

    def get_path(self)->Path:
        return self._path

    def get_native_absolute_path(self)->str:
        return self._path.get_native_absolute_path()

    def load(self) -> str:
        with open(self._path.get_native_absolute_path(), "r", encoding="utf-8") as file:
            self._ram = file.read()
        return self._ram

    def save(self):
        with open(self._path.get_native_absolute_path(), "w", encoding="utf-8") as file:
            file.write(self._path.get_native_absolute_path())

    def get_ram(self)->str:
        if self._ram is None:
            self._load()
        return self._ram