import os
from typing import Union
from pathlib import Path as SysPath


class Path:
    """"""
    def __init__(self, raw_path:str):
        '''
        I don't care about os, I fix the str_path and I give native OS str_path, just call get_native_os_path()
        :param raw_path:str
        '''
        self.__raw_path = raw_path
        self._native_os_path = None

        # Lazy loadings
        self._all_abs_file_paths_rec = None

    def get_native_path(self) -> str:
        '''
        It removes the trailing slashes in case they are folders
        Converts / or \ to native os paths
        :return:
        '''
        if self._native_os_path is None:
            self._native_os_path = os.path.normpath(self.__raw_path)
        return self._native_os_path

    def get_native_absolute_path(self)->str:
        '''get absolute str_path'''
        return os.path.abspath(self.get_native_path())

    def get_native_os_path_with_trailing_slash(self) -> str:
        '''
        :return: str
        '''
        native_path:str = self.get_native_path()
        if self.is_directory():
            return native_path+os.sep
        return native_path

    def is_file(self)->bool:
        '''
        :return:
        '''
        return os.path.isfile(self.get_native_absolute_path())

    def is_directory(self)->bool:
        '''
        :return:
        '''
        return os.path.isdir(self.get_native_absolute_path())

    def get_real_file_type_regardless_of_extension(self, path_to_file_type:Union[str, 'Path']) -> bool:

        pass

    def get_all_absolute_file_paths_recursively(self)->list:
        if self._all_abs_file_paths_rec is None:
            root = SysPath(self.get_native_absolute_path())
            all_files_and_folders_rec = list(root.rglob("*"))
            self._all_abs_file_paths_rec = [f for f in all_files_and_folders_rec if f.is_file()]
        return self._all_abs_file_paths_rec

    @staticmethod
    def get_os_path_separator():
        return os.sep

    def get_parent_directory(self) -> str:
        """
        Returns the parent directory as a Path object.

        If the current str_path is a file or a folder, this always returns
        the directory immediately above it.
        """
        parent_dir = os.path.dirname(self.get_native_absolute_path())
        return parent_dir

    def dir_exists(self) -> bool:
        """
        Returns True only if the str_path exists and is a directory.
        """
        return os.path.isdir(self.get_native_absolute_path())

    def file_exists(self) -> bool:
        """
        Returns True only if the str_path exists and is a file.
        """
        return os.path.isfile(self.get_native_absolute_path())

    def path_exists(self) -> bool:
        """
        Returns True if either a file or a directory exists at this str_path.
        Equivalent to (dir_exists() or file_exists()).
        """
        return os.path.exists(self.get_native_absolute_path())

    def create_missing_directories(self):
        os.makedirs(self.get_native_absolute_path(), exist_ok=True)



