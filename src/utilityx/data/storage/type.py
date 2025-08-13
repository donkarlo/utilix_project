from enum import IntEnum
from typing import Union
from functools import cache

class Type(IntEnum):
    """
    This class might be only useful in factory methods
    """
    FILE = 0
    DIR = 1
    DB = 2

    @classmethod
    def is_supporting_type(cls, type: Union[int, str, "Type"]) -> bool:
        if isinstance(type, int):
            #Types.is_supporting_type(1)
            return type in cls._value2member_map_
        if isinstance(type, str):
            #Types.is_supporting_type("file")
            return type.upper() in cls.__members__
        if isinstance(type, cls):
            #Types.is_supporting_type(Types.DB)
            return True
        return False

    @staticmethod
    @cache
    def get_all_as_str_int_tuple() -> tuple[tuple[str, int], ...]:
        return tuple((member.name, member.value) for member in Type)

    @staticmethod
    @cache
    def get_all_as_str_tuple() -> tuple[str, ...]:
        return tuple(member.name for member in Type)
