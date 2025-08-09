from utilityx.data.storage import Type
from utilityx.os.filesys.os_path import OsPath


class File(Type):
    def __init__(self, path:OsPath):
        self._os_path = path

    def get_os_path(self)->OsPath:
        return self._os_path

    def get_abs_os_path(self)->str:
        return self._os_path.get_abs_path()