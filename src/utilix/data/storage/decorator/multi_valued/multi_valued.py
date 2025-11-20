from typing import override, List, Any

from utilix.data.storage.decorator.decorator import Decorator
from utilix.data.storage.decorator.multi_valued.observer.add_to_ram_values_publisher import AddToRamValuesPublisher
from utilix.data.storage.decorator.multi_valued.observer.group_ram_values_addition_finished_publisher import \
    GroupRamValuesAdditionFinishedPublisher
from utilix.data.storage.decorator.multi_valued.observer.group_ram_values_addition_finished_subscriber import \
    GroupRamValuesAdditionFinishedSubscriber
from utilix.data.kind.sliced_value.values_slice import ValuesSlice
from utilix.data.kind.sliced_value.values_slices import ValuesSlices
from utilix.data.storage.decorator.multi_valued.observer.add_to_ram_values_subscriber import AddToRamValuesSubscriber
from utilix.data.storage.decorator.multi_valued.interface import Interface as MultiValuedInterface
from utilix.oop.inheritance.overriding.override_from import override_from


class MultiValued(Decorator, MultiValuedInterface):
    """
    A kind of os_file full of  values such as a sliced_value doc yaml file.
    Each raw_value can have a different format
    """

    def __init__(self, inner:Decorator, separator:str):
        """
        Args:
            inner:
            separator: holds the strategy for breaking string blob in the storage to values
        """
        Decorator.__init__(self, inner)

        #add_value_subscriber
        self._add_value_subscribers: List[AddToRamValuesSubscriber] = []
        self._group_ram_values_finished_subscribers:List[GroupRamValuesAdditionFinishedSubscriber] = []

        #to hold one ram raw_value TODO: Convert the list to group
        self._ram_values:List = []

        # To cache ram values slices TODO: sync ram values to
        self._ram_values_slices = ValuesSlices()

        #how string documents are separated for example in sliced_value yaml files it s ---
        self._separator = separator

    @override_from(AddToRamValuesPublisher)
    def attach_add_to_ram_values_subscriber(self, add_value_subscriber:AddToRamValuesSubscriber)->None:
        if add_value_subscriber not in self._add_value_subscribers:
            self._add_value_subscribers.append(add_value_subscriber)

    @override_from(AddToRamValuesPublisher)
    def dettach_add_to_ram_values_subscriber(self, add_value_subscriber: AddToRamValuesSubscriber)->None:
        if add_value_subscriber in self._add_value_subscribers:
            self._add_value_subscribers.remove(add_value_subscriber)

    @override_from(GroupRamValuesAdditionFinishedPublisher)
    def attach_group_ram_values_addition_finished_subscriber(self, add_values_finished_subscriber: GroupRamValuesAdditionFinishedSubscriber) -> None:
        self._group_ram_values_finished_subscribers.append(add_values_finished_subscriber)

    def notify_add_to_ram_values_subscribers(self, value:Any) -> None:
        for add_value_observer in self._add_value_subscribers:
            add_value_observer.do_when_a_new_value_is_added_to_ram(value)

    def notify_group_ram_values_finished_subscribers(self) -> None:
        for group_ram_values_finished_subscriber in self._group_ram_values_finished_subscribers:
            group_ram_values_finished_subscriber.do_when_group_ram_values_addition_is_finished()


    @override
    def save(self):
        # for example in core is File then
        if self._separator is not None:
            self._inner.set_ram(self._separator.join(self._ram_values))
        else:
            self._inner.set_ram("".join(self._ram_values))
        #call save from decorator
        super().save()

    @override
    def set_ram_values(self, ram_values:List)->None:
        self._ram_values = ram_values

    @override
    def get_ram_values(self)->List:
        return self._ram_values

    @override
    def get_ram_value_at(self, at:int)->None:
        return self._ram_values[at]

    @override
    def add_to_ram_values_at(self, index: int, values: List) -> None:
        for offset, value in enumerate(values):
            self._ram_values.insert(index + offset, value)
        self.notify_add_to_ram_values_subscribers(value)

    @override
    def get_ram_values_by_slice(self, slc: slice) -> List:
        return self._ram_values[slc]

    @override
    def add_to_ram_values(self, value:str)->None:
        self._ram_values.append(value)
        self.notify_add_to_ram_values_subscribers(value)

    @override
    def add_to_ram_values_slices(self, values_slice:ValuesSlice)->None:
        self._ram_values_slices.add_values_slice(values_slice)
        for add_value_subscriber in self._add_value_subscribers:
            for value in values_slice.get_values():
                add_value_subscriber.do_when_a_new_value_is_added_to_ram(value)
        self.notify_group_ram_values_finished_subscribers()

    @override
    def earase_ram_values(self)->None:
        self._ram_values.clear()

    @override
    def get_ram_values_slices(self)->ValuesSlices:
        return self._ram_values_slices

    @override
    def get_ram_values_from_values_slices_by_slice(self,slc:slice)->List[str]:
        return self._ram_values_slices.get_values_by_slice(slc)


