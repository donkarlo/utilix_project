from typing import List, runtime_checkable, Protocol

from utilix.data.storage.decorator.multi_valued.interface import Interface as MultiValuedInterface
from utilix.data.storage.decorator.multi_valued.observer.add_to_ram_values_publisher import AddToRamValuesPublisher
from utilix.data.storage.decorator.multi_valued.observer.group_ram_values_addition_finished_publisher import \
    GroupRamValuesAdditionFinishedPublisher
from utilix.data.storage.interface import Interface as StorageInterface


@runtime_checkable
class SlicedInterface(MultiValuedInterface, AddToRamValuesPublisher, GroupRamValuesAdditionFinishedPublisher,
                      Protocol):
    def get_values_by_slice(self, slc: slice) -> List:
        """
        Retirns a list of strings as document
        Args:
            slc:

        Returns:

        """
        ...

    def get_slice(self)->slice: ...

    def get_ram_values_by_slice(self, slc:slice)->List: ...

