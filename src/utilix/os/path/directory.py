from utilix.os.path.path import Path


class Directory(Path):
    def __init__(self, str_path: str)->None:
        super().__init__(str_path)

    def create_directory(self, name: str) -> None:
        if self.is_directory():
            os.mkdir(self.get_native_os_path_with_trailing_slash() + name)
        else:
            raise TypeError("create_directory() not implemented for non-directory")