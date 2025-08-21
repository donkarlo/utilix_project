from abc import abstractmethod
from typing import override, List

from utilityx.data.storage.decorator.decorator import Decorator
from utilityx.data.type.muti.values_slices import ValuesSlices


class MultiValued(Decorator):
    """
    A kind of source full of  values such as a multi doc yaml file
    """
    __slots__ = ("_ram_values", "_separator", "_ram_values_slices")

    def __init__(self, inner:Decorator, separator:str, single_value:bool):
        """
        Args:
            inner:
            separator: holds the strategy for breaking string blob in the storage to values
        """
        super().__init__(inner)
        self._ram_values:list[str] = []
        self._ram_values_slices = ValuesSlices()
        self._separator = separator

    @abstractmethod
    def _do_load_slice(self, s:slice) -> list[str]:
        """
        To load a slice into
        Args:
            s:

        Returns:

        """
        pass

    @override
    def save(self):
        if self._separator is not None:
            self._ram = self._separator.join(self._ram_values)
        else:
            self._ram = "".join(self._ram_values)
        super().save()

    @override
    def load(self) -> str:
        None


    def load_slice(self, slc:slice)->None:
        if not self._ram_values_slices.slice_exists(slc):
            self._do_load_slice(slc)



    def set_ram_values(self, ram_values:list[str]):
        self._ram_values = ram_values

    def get_ram_values(self):
        return self._ram_values

    def get_ram_value_at(self, at:int):
        return self._ram_values[at]

    def add_to_ram_values_at(self, index: int, values: list[str]) -> None:
        for offset, value in enumerate(values):
            self._ram_values.insert(index + offset, value)


    def get_ram_values_slice(self, s: slice) -> list[str]:
        return self._ram_values[s]

    def add_ram_value(self, value:str):
        self._ram_values.append(value)

    def earase_ram_values(self):
        self._ram_values.clear()




