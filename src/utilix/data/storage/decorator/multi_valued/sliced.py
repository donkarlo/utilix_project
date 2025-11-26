from typing import override, List, Any

from utilix.data.storage.decorator.decorator import Decorator
from utilix.data.storage.decorator.multi_valued.multi_valued import MultiValued
from utilix.data.kind.indexed_value.sliced_value.sliced_values import SlicedValues
from utilix.data.storage.decorator.multi_valued.observer.add_to_ram_values_subscriber import AddToRamValuesSubscriber
from utilix.data.storage.decorator.multi_valued.sliced_interface import SlicedInterface
from utilix.oop.inheritance.overriding.override_from import override_from


class Sliced(MultiValued, SlicedInterface):
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
        #to hold one ram raw_value TODO: Convert the list to group
        self._inner._ram:SlicedValues = SlicedValues(self._slc, None)





    @override_from(MultiValued, False, False)
    def set_ram(self, sliced_values:SlicedValues)->None:
        self._ram = sliced_values

    @override_from(SlicedInterface)
    def get_ram_values_by_slice(self, slc: slice) -> List:
        values = self._ram.get_values()[slc]
        return values

    @override_from(SlicedInterface)
    def get_slice(self)->slice:
        return self._slc

    @override_from(SlicedInterface)
    def add_to_ram_values(self, value:Any)->None:
        self._ram.add_value(value)
        self.notify_add_to_ram_values_subscribers(value)


