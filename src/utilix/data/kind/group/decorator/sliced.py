from utilix.data.kind.group.decorator.decorator import Decorator
from utilix.data.kind.group.interface import Interface


class Sliced(Decorator):
    """
    A part of a bigger group
    """
    def __init__(self, inner:Interface, slc:slice):
        self._inner = inner
        self._slice = slc
    def get_slice(self)->slice:
        return self._slice
