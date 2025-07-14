from enum import IntEnum
from typing import Union
from functools import cache

class SupportingFormat(IntEnum):
    STRING = 0
    XML = 1
    YAML = 2

    @classmethod
    def is_supporting_format(cls, format: Union[int, str, "SupportingFormat"]) -> bool:
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


if __name__ == '__main__':
    print(format(SupportingFormat.FILE))                      # <enum 'SupportingFormats'>
    print(SupportingFormat.FILE.value)                      # 0
    print(list(SupportingFormat))                           # [<SupportingFormats.FILE: 0>, <SupportingFormats.DIR: 1>, <SupportingFormats.DB: 2>]
    print(SupportingFormat.get_all_as_str_int_tuple())      # (('FILE', 0), ('DIR', 1), ('DB', 2))
    print(SupportingFormat.get_all_as_str_tuple())          # ('FILE', 'DIR', 'DB')
