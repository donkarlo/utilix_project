from typing import List, runtime_checkable, Protocol

from nd_utility.data.storage.decorator.multi_valued.observer.add_to_ram_values_publisher import AddToRamValuesPublisher
from nd_utility.data.storage.decorator.multi_valued.observer.group_ram_values_addition_finished_publisher import \
    GroupRamValuesAdditionFinishedPublisher
from nd_utility.data.kind.indexed_value.sliced_value.sliced_values import SlicedValues
from nd_utility.data.kind.indexed_value.sliced_value.group.group import Group
from nd_utility.data.storage.decorator.multi_valued.interface import Interface as MultiValuedInterface


@runtime_checkable
class Interface(MultiValuedInterface, AddToRamValuesPublisher, GroupRamValuesAdditionFinishedPublisher , Protocol):
    def get_values_by_slice(self, slc:slice)->List:
        """
        Retirns a list of strings as document
        Args:
            slc:

        Returns:

        """
        ...
    def get_ram_by_slice(self, slc: slice) -> List: ...

    def add_to_ram_slice_group(self, values_slice: SlicedValues) -> None: ...

    def get_ram_slices(self) -> Group: ...

    def get_ram_from_values_slices_by_slice(self, slc: slice) -> List[str]: ...

