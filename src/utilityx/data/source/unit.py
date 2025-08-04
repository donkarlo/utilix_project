from abc import abstractmethod
from importlib.metadata import pass_none


class Unit(ABC):
    """Smallest meaningful unit"""
    def __init__(self, string_unit:str):
        pass

    @abstractmethod
    def translate_from_string_to_unit_structure(self)->Unit:
        pass

    @abstractmethod
    def get_string(self):
        pass_none()