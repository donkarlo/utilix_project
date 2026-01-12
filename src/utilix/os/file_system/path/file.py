from utilix.os.file_system.path.path import Path


class File(Path):
    def __init__(self, str_path: str)->None:
        super().__init__(str_path)

    def get_containing_abolute_directory_path(self)->str:
        return self.get_parent_directory_string_path()