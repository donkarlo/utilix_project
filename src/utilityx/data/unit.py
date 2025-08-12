from abc import abstractmethod, ABC
from typing import Any


class Unit(ABC):
    def __init__(self, id:int, str_content:str):
        """
        Responsible to hold the unit, maybe in future how to interprete a block of string data
        Args:
            id:
        """
        self.__id = id
        self._str_content = str_content

    @abstractmethod
    def validate(self, content:str)->bool:
        pass

    @abstractmethod
    def convert_from_str_to_unit(self, raw:Any)->bool:
        pass

    @abstractmethod
    def convert_from_unit_to_str(self)->str:
        pass