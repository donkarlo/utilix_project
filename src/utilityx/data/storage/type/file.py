from utilityx.data.storage import Storage
from utilityx.os.path import Path


class File(Storage):
    def __init__(self, path:Path):
        self._os_path = path

    def get_os_path(self)->Path:
        return self._os_path

    def get_abs_os_path(self)->str:
        return self._os_path.get_abs_path()