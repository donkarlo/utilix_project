from abc import abstractmethod, ABC

from utilityx.data.access.access import Access
from utilityx.data.format.supporting_format import SupportingFormat
from utilityx.data.type.supporting_type import SupportingType


class Source:
    def __init__(self, type:SupportingType, format:SupportingFormat, access:Access):
        self._type = type
        self._format = format
        self._access = access


    @abstractmethod
    def get_str_content(self)->str:
        pass

    def get_type(self)->int:
        return self._type


