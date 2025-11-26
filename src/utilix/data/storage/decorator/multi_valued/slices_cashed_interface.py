from typing import List, runtime_checkable, Protocol

from utilix.data.storage.decorator.multi_valued.observer.add_to_ram_values_publisher import AddToRamValuesPublisher
from utilix.data.storage.decorator.multi_valued.observer.group_ram_values_addition_finished_publisher import \
    GroupRamValuesAdditionFinishedPublisher
from utilix.data.kind.indexed_value.sliced_value.sliced_values import SlicedValues
from utilix.data.kind.indexed_value.sliced_value.group.group import Group
from utilix.data.storage.decorator.multi_valued.interface import Interface as MultiValuedInterface


@runtime_checkable
class SlicesCashedInterface(MultiValuedInterface, AddToRamValuesPublisher, GroupRamValuesAdditionFinishedPublisher , Protocol):
    def get_values_by_slice(self, slc:slice)->List:
        """
        Retirns a list of strings as document
        Args:
            slc:

        Returns:

        """
        ...
    def get_ram_values_by_slice(self, slc: slice) -> List: ...

    def add_to_ram_values_slice_group(self, values_slice: SlicedValues) -> None: ...

    def get_ram_values_slices(self) -> Group: ...

    def get_ram_values_from_values_slices_by_slice(self, slc: slice) -> List[str]: ...

