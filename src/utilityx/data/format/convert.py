from abc import ABC, abstractmethod

from utilityx.data.format.supporting_format import SupportingFormat

from utilityx.data.format import Format


class Conversion(ABC):
    """
    conversion from one format to another
    """
    def __init__(self, from_format:Format, to_supporting_format:SupportingFormat=None):
        self._from_format = from_format
        self._to_format = to_supporting_format

        #
        self._new_format = None

    @abstractmethod
    def get_converted(self)->Format:
        pass