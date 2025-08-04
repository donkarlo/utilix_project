from abc import abstractmethod

from utilityx.data.access import Access
from utilityx.data.format.supporting_format import SupportingFormat
from utilityx.data.type.supporting_type import SupportingType


class Source:
    def __init__(self, type:SupportingType, format:SupportingFormat, access:Access):
        self._type = type
        self._format = format
        self._access = access

        # for lazy loading etc
        self._all_str_content = None


    @abstractmethod
    def load_all_str_content(self)->str:
        pass

    @abstractmethod
    def save_raw_string_content(self, content:String)->bool:
        """
        No validity check will be performed here. Just the given string will be added
        Args:
            content:

        Returns:

        """
        pass

    def get_type(self)->SupportingType:
        return self._type

    def get_format(self)->SupportingFormat:
        return self._format


