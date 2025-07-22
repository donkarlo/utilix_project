from utilityx.data.format.format import Format
from utilityx.data.type.type import Type
from utilityx.osx.filesys.os_path import OsPath


class File(Type):
    def __init__(self, path:OsPath):
        self._os_path = path

    def get_os_path(self)->OsPath:
        return self._os_path

    def get_abs_os_path(self)->str:
        return self._os_path.get_abs_path()