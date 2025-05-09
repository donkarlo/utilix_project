import os

class OsPath:
    def __init__(self, raw_path:str):
        '''
        I don't care about osx, I fix the path and I give native OS path, just call get_native_os_path()
        :param raw_path:str
        '''
        self.__raw_path = raw_path
        self._native_os_path = None

    def get_native_os_path(self) -> str:
        '''
        It removes the trailing slashes in case they are folders
        Converts / or \ to native osx paths
        :return:
        '''
        if self._native_os_path is None:
            self._native_os_path = os.path.normpath(self.__raw_path)
        return self._native_os_path

    def get_abs_path(self)->str:
        '''get absolute path'''
        return os.path.abspath(self.get_native_os_path())

    def get_native_os_path_with_trailing_slash(self) -> str:
        '''
        :return: str
        '''
        native_path:str = self.get_native_os_path()
        if self.is_dir():
            return native_path+os.sep
        return native_path

    def is_file(self)->bool:
        '''
        :return:
        '''
        return os.path.isfile(self.get_native_os_path())

    def is_dir(self)->bool:
        '''
        :return:
        '''
        return os.path.isdir(self.get_native_os_path())

if __name__ == '__main__':
    path = OsPath('H://docs//git\\text.txt')
    print(path.get_native_os_path())