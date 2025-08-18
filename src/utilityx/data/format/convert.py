from abc import ABC, abstractmethod

from utilityx.data.format.format import SupportingFormat

from utilityx.data.format.format import Format


class Conversion(ABC):
    """
    conversion from one format to another
    """
    def __init__(self, from_type:Format, to_type:Format):
        self._from_type = from_type
        self._to_type = to_type

    @abstractmethod
    def get_converted_string_content(self, string_content:str)->str:
        pass