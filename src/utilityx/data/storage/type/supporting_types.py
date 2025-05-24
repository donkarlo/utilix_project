from enum import IntEnum
from typing import Union
from functools import cache

class SupportingTypes(IntEnum):
    FILE = 0
    DIR = 1
    DB = 2

    @classmethod
    def is_supporting_type(cls, type: Union[int, str, "SupportingTypes"]) -> bool:
        if isinstance(type, int):
            return type in cls._value2member_map_
        if isinstance(type, str):
            return type.upper() in cls.__members__
        if isinstance(type, cls):
            return True
        return False

    @staticmethod
    @cache
    def get_all_as_str_int_tuple() -> tuple[tuple[str, int], ...]:
        return tuple((member.name, member.value) for member in SupportingTypes)

    @staticmethod
    @cache
    def get_all_as_str_tuple() -> tuple[str, ...]:
        return tuple(member.name for member in SupportingTypes)


if __name__ == '__main__':
    print(type(SupportingTypes.FILE))                      # <enum 'SupportingTypes'>
    print(SupportingTypes.FILE.value)                      # 0
    print(list(SupportingTypes))                           # [<SupportingTypes.FILE: 0>, <SupportingTypes.DIR: 1>, <SupportingTypes.DB: 2>]
    print(SupportingTypes.get_all_as_str_int_tuple())      # (('FILE', 0), ('DIR', 1), ('DB', 2))
    print(SupportingTypes.get_all_as_str_tuple())          # ('FILE', 'DIR', 'DB')
