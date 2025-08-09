from aix.data.data_source import DataSource

from utilityx.data.source import Source


class Partial(Decorator):
    """
    Partial means that you can save from a beginning index
    """
    def __init__(self, inner:Source):
        super().__init__(inner)
        pass

    @abstractmethod
    def add_content_at(self, index:int)->bool:
        pass

    @abstractmethod
    def get_slice(self, slice:slice)->slice:
        pass

