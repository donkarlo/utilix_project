from utilix.os.file_system.path.path import Path


class File(Path):
    def __init__(self, str_path: str)->None:
        super().__init__(str_path)