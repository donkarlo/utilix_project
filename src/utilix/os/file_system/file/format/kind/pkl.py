from utilix.os.file_system.file.format.format import Format
from utilix.os.file_system.file.format.kind.kinds import Kinds


class Pkl(Format):
    def __init__(self):
        super().__init__(Kinds.PKL)
