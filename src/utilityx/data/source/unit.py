from abc import abstractmethod
from importlib.metadata import pass_none


class Unit(ABC):
    """Smallest meaningful unit"""
    def __init__(self, id:int):
        """

        Args:
            id: id number in storage, it is not a type id
        """
        self.__id = id

    @abstractmethod
    def translate_from_string_to_unit_structure(self, content:str)->Unit:
        pass

    @abstractmethod
    def get_string(self):
        """converts to  string"""
        pass