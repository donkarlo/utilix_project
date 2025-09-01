from enum import IntEnum
from typing import Union
from functools import cache
from utilityx.data.storage.type.file.format.type.supporting_format import SupportingFormat

class SupportingFormat(IntEnum):
    """
    To infom mostly factories what class is needed
    """
    STRING = 0
    XML = 1
    YAML = 2

    @classmethod
    def is_supporting_type(cls, format: Union[int, str, SupportingFormat]) -> bool:
        if isinstance(format, int):
            #Formats.is_supporting_format(1)
            return format in cls._value2member_map_
        if isinstance(format, str):
            #Formats.is_supporting_format("file")
            return format.upper() in cls.__members__
        if isinstance(format, cls):
            #Formats.is_supporting_format(Formats.DB)
            return True
        return False

    @staticmethod
    @cache
    def get_all_as_str_int_tuple() -> tuple[tuple[str, int], ...]:
        return tuple((member.name, member.value) for member in SupportingFormat)

    @staticmethod
    @cache
    def get_all_as_str_tuple() -> tuple[str, ...]:
        return tuple(member.name for member in SupportingFormat)
      # ('FILE', 'DIR', 'DB')
