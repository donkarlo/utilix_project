from utilityx.osx.filesys.format.supporting_format import Formats

from utilityx.osx.filesys.os_path import OsPath


class File:
    def __init__(self, os_path:OsPath, format:Format):
        self._os_path = os_path
        if Formats.is_supporting_type(format):
            self._format = format