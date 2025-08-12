from abc import ABC, abstractmethod

from utilityx.data.unit.supporting_format import SupportingFormat

from utilityx.data.unit import Unit


class Conversion(ABC):
    """
    conversion from one unit to another
    """
    def __init__(self, from_format:Unit, to_supporting_format:SupportingFormat=None):
        self._from_format = from_format
        self._to_format = to_supporting_format

        #
        self._new_format = None

    @abstractmethod
    def get_converted(self)->Unit:
        pass