from abc import abstractmethod, ABC
from typing import Any


class Type(ABC):
    def __init__(self):
        """
        To hold both the string string_content and how to convert it to a python object
        - it can not have storage save option. if saving is needed, it should be done through a storage object
        """

    @abstractmethod
    def validate_content(self, content:str)->bool:
        pass

    @abstractmethod
    def convert_content_to_type(self, string_content:str)->bool:
        pass

    @abstractmethod
    def convert_from_type_to_content(self)->str:
        pass