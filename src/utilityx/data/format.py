from abc import abstractmethod, ABC


class Format(ABC):
    def __init__(self, id:int):
        """
        Responsible to hold the format, maybe in future how to interprete a block of string data
        Args:
            id:
        """
        self.__id = id

    @abstractmethod
    def get_modeled(self, content:str):
        pass