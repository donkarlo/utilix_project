from utilix.os.path.path import Path


class FilePath(Path):
    def __init__(self, str_path: str)->None:
        super().__init__(str_path)