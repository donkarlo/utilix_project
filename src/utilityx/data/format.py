from abc import abstractmethod, ABC

from utilityx.data.format.object_model import ObjectModel


class Format(ABC):
    def __init__(self, id:int, object_model:ObjectModel):
        """
        Responsible to hold the format, maybe in future how to interprete a block of string data
        Args:
            id:
        """
        self.__id = id
        self._object_model = object_model

    @abstractmethod
    def get_object_model(self, content:str)->ObjectModel:
        """

        Args:
            content:

        Returns:

        """
        pass

    @abstractmethod
    def validate(self, content:str)->bool:
        pass