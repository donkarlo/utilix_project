from typing import List, Any
from utilix.data.storage.decorator.decorator import Decorator
from utilix.data.storage.decorator.multi_valued.multi_valued import MultiValued
from utilix.data.kind.indexed_value.sliced_value.sliced_values import SlicedValues
from utilix.data.storage.decorator.multi_valued.decorator.sliced.interface import Interface
from utilix.oop.inheritance.overriding.override_from import override_from


class Sliced(MultiValued, Interface):
    """
    A kind of os_file full of  values such as a sliced_value doc yaml file.
    Each raw_value can have a different format
    """

    def __init__(self, inner:Decorator, slc:slice, separator:str):
        """
        Args:
            inner:
            separator: holds the strategy for breaking string blob in the storage to values
        """
        MultiValued.__init__(self, inner, separator)

        # how string documents are separated for example in sliced_value yaml files it s ---
        self._separator = separator
        self._slc: slice = slc


        # self._ram is not mentioned here as it is the
        self._inner._ram:SlicedValues = SlicedValues(self._slc, None)





    @override_from(MultiValued, False, False)
    def set_ram(self, values:List)->None:
        Decorator.set_ram(self, SlicedValues(self._slc, values))

    @override_from(Interface)
    def get_ram_by_slice(self, slc: slice) -> List:
        values = self._ram.get_values()[slc]
        return values

    @override_from(Interface)
    def get_slice(self)->slice:
        return self._slc

    @override_from(Interface)
    def add_to_ram(self, value:Any)->None:
        self._ram.add_value(value)
        self.notify_add_to_ram_values_subscribers(value)


