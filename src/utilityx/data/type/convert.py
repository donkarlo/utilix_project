from abc import ABC, abstractmethod

from utilityx.data.type.supporting_format import SupportingFormat

from utilityx.data.type import Type


class Conversion(ABC):
    """
    conversion from one type to another
    """
    def __init__(self, from_type:Type, to_type:Type):
        self._from_type = from_type
        self._to_type = to_type

    @abstractmethod
    def get_converted_string_content(self, string_content:str)->str:
        pass