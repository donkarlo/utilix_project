from typing import List, runtime_checkable, Protocol, Any

from utilix.data.storage.decorator.multi_valued.observer.add_to_ram_values_publisher import AddToRamValuesPublisher
from utilix.data.storage.decorator.multi_valued.observer.group_ram_values_addition_finished_publisher import \
    GroupRamValuesAdditionFinishedPublisher
from utilix.data.storage.interface import Interface as StorageInterface


@runtime_checkable
class Interface(StorageInterface, AddToRamValuesPublisher, GroupRamValuesAdditionFinishedPublisher , Protocol):
    def get_values_by_slice(self, slc:slice)->List:
        """
        Retirns a list of strings as document
        Args:
            slc:

        Returns:

        """
        ...

    def set_ram(self, ram: List[Any]) -> None: ...

    def get_ram_at(self, at: int) -> None: ...

    def add_to_ram_at(self, index: int, values: List) -> None: ...

    def add_to_ram(self, value: Any) -> None: ...

