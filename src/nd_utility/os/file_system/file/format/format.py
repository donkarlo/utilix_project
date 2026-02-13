from enum import Enum, auto

from nd_utility.os.file_system.file.format.kind.kinds import Kinds


class Format(Enum):
    def __init__(self, format_kind:Kinds):
        """
        """
        self._format_kind = format_kind

    def get_format_kind(self)->Kinds:
        return self._format_kind
