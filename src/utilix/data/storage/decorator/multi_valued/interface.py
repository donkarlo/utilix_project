from typing import List, runtime_checkable, Protocol

from utilix.data.storage.decorator.multi_valued.add_to_ram_values_publisher import AddToRamValuesPublisher
from utilix.data.storage.interface import Interface as StorageInterface
from utilix.data.type.sliced_value.values_slice import ValuesSlice
from utilix.data.type.sliced_value.values_slices import ValuesSlices


@runtime_checkable
class Interface(StorageInterface, AddToRamValuesPublisher , Protocol):
    def get_values_by_slice(self, slc:slice)->List:
        """
        Retirns a list of strings as document
        Args:
            slc:

        Returns:

        """
        ...

    def set_ram_values(self, ram_values: List) -> None: ...

    def get_ram_values(self) -> List: ...

    def get_ram_value_at(self, at: int) -> None: ...

    def add_to_ram_values_at(self, index: int, values: List) -> None: ...

    def get_ram_values_by_slice(self, slc: slice) -> List: ...

    def add_to_ram_values(self, value: str) -> None: ...

    def add_to_ram_values_slices(self, valuesSlice: ValuesSlice) -> None: ...

    def earase_ram_values(self) -> None: ...

    def get_ram_values_slices(self) -> ValuesSlices: ...

    def get_ram_values_from_values_slices_by_slice(self, slc: slice) -> List[str]: ...

