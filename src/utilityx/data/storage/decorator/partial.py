from abc import abstractmethod
from utilityx.data.source import Source


class Partial(Decorator):
    """
    Partial means that you can save from a beginning index
    """
    def __init__(self, inner:Source):
        super().__init__(inner)

    @abstractmethod
    def add_to_memory_content_at(self, index:int, content:str)->bool:
        pass

    @abstractmethod
    def get_slice(self, slice:slice)->slice:
        pass

