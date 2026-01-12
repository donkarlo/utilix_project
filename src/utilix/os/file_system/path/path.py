import os
from pathlib import Path as SysPath
from typing import Union, Optional, List


class Path:
    """"""

    def __init__(self, raw_path: str):
        '''
        I don't care about os, I fix the str_path and I give native OS str_path, just call get_native_os_path()
        :param raw_path:str
        '''
        self.__raw_path = raw_path
        self._native_os_path:Optional[str] = None

        # Lazy loadings
        self._all_abs_file_paths_rec:Optional[List] = None

    def get_native_string_path(self) -> str:
        """
        It removes the trailing slashes in case they are folders
        - Converts forward slash (/) or backslash (\\) to native OS paths
        """
        if self._native_os_path is None:
            self._native_os_path = os.path.normpath(self.__raw_path)
        return self._native_os_path

    def get_native_absolute_string_path(self) -> str:
        '''get absolute str_path'''
        return os.path.abspath(self.get_native_string_path())

    def get_native_os_string_path_with_trailing_slash(self) -> str:
        '''
        :return: str
        '''
        native_path: str = self.get_native_string_path()
        if self.directory_exists():
            return native_path + os.sep
        return native_path

    def get_all_absolute_file_paths_recursively(self) -> Optional[List]:
        if self._all_abs_file_paths_rec is None:
            root = SysPath(self.get_native_absolute_string_path())
            all_files_and_folders_rec = list(root.rglob("*"))
            self._all_abs_file_paths_rec = [f for f in all_files_and_folders_rec if f.is_file()]
        return self._all_abs_file_paths_rec

    @staticmethod
    def get_os_path_separator():
        return os.sep

    def get_parent_directory_string_path(self) -> str:
        """
        Returns the parent directory as a Path object.

        If the current str_path is a file or a folder, this always returns
        the directory immediately above it.
        """
        parent_dir = os.path.dirname(self.get_native_absolute_string_path())+os.sep
        return parent_dir

    def directory_exists(self) -> bool:
        """
        Returns True only if the str_path exists and is a directory.
        """
        return os.path.isdir(self.get_native_absolute_string_path())

    def file_exists(self) -> bool:
        """
        Returns True only if the str_path exists and is a file.
        """
        return os.path.isfile(self.get_native_absolute_string_path())

    def path_exists(self) -> bool:
        """
        Returns True if either a file or a directory exists at this str_path.
        Equivalent to (dir_exists() or file_exists()).
        """
        return os.path.exists(self.get_native_absolute_string_path())

    def create_missing_directories(self):
        os.makedirs(self.get_native_absolute_string_path(), exist_ok=True)

    def append_segment(self, segment: Union["Path", str]):
        if isinstance(segment, Path):
            self.__raw_path = self.get_native_string_path() + self.get_os_path_separator() + segment.get_native_string_path()
        elif isinstance(segment, str):
            self.__raw_path = self.get_native_string_path() + self.get_os_path_separator() + segment
