from abc import abstractmethod
from typing import override, List

from utilix.data.storage.decorator.decorator import Decorator
from utilix.data.type.sliced_value.values_slice import ValuesSlice
from utilix.data.type.sliced_value.values_slices import ValuesSlices

class MultiValued(Decorator):
    """
    A kind of source full of  values such as a sliced_value doc yaml file.
    Each raw_value can have a different format
    """
    __slots__ = ("_ram_values", "_separator", "_ram_values_slices")

    def __init__(self, inner:Decorator, separator:str):
        """
        Args:
            inner:
            separator: holds the strategy for breaking string blob in the storage to values
        """
        super().__init__(inner)

        #to hold one ram raw_value
        self._ram_values:List = []

        # To cache ram values slices TODO: sync ram values to
        self._ram_values_slices = ValuesSlices()

        #how string documents are separated for example in sliced_value yaml files it s ---
        self._separator = separator


    @override
    def save(self):
        # for example in core is File then
        if self._separator is not None:
            self._inner.set_ram(self._separator.join(self._ram_values))
        else:
            self._inner.set_ram("".join(self._ram_values))
        #call save from decorator
        super().save()


    def set_ram_values(self, ram_values:List):
        self._ram_values = ram_values

    def get_ram_values(self)->List:
        return self._ram_values

    def get_ram_value_at(self, at:int):
        return self._ram_values[at]

    def add_to_ram_values_at(self, index: int, values: List) -> None:
        for offset, value in enumerate(values):
            self._ram_values.insert(index + offset, value)


    def get_ram_values_by_slice(self, slc: slice) -> List:
        return self._ram_values[slc]

    def add_ram_value(self, value:str):
        self._ram_values.append(value)

    def add_to_ram_values_slices(self, valuesSlice:ValuesSlice):
        self._ram_values_slices.add_values_slice(valuesSlice)

    def earase_ram_values(self):
        self._ram_values.clear()

    def get_ram_values_slices(self)->ValuesSlices:
        return self._ram_values_slices

    def get_ram_values_from_values_slices_by_slice(self,slc:slice)->List[str]:
        return self._ram_values_slices.get_values_by_slice(slc)


