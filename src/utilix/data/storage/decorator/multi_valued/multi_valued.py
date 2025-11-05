from abc import abstractmethod
from typing import override, List

from utilix.data.storage.decorator.decorator import Decorator
from utilix.data.type.sliced_value.values_slice import ValuesSlice
from utilix.data.type.sliced_value.values_slices import ValuesSlices
from utilix.data.storage.decorator.multi_valued.add_value_subscriber import AddValueSubscriber
from utilix.data.storage.decorator.multi_valued.interface import Interface as MultiValuedInterface
from utilix.data.storage.decorator.multi_valued.add_value_publisher import AddValuePublisher

class MultiValued(Decorator, AddValuePublisher, MultiValuedInterface):
    """
    A kind of source full of  values such as a sliced_value doc yaml file.
    Each raw_value can have a different format
    """
    __slots__ = ("_ram_values", "_separator", "_ram_values_slices", "_add_value_subscribers")

    def __init__(self, inner:Decorator, separator:str):
        """
        Args:
            inner:
            separator: holds the strategy for breaking string blob in the storage to values
        """
        super(Decorator, self).__init__(inner)

        #add_value_observer
        self._add_value_subscribers: List[AddValueSubscriber] = []

        #to hold one ram raw_value
        self._ram_values:List = []

        # To cache ram values slices TODO: sync ram values to
        self._ram_values_slices = ValuesSlices()

        #how string documents are separated for example in sliced_value yaml files it s ---
        self._separator = separator

    def attach_add_value_observer(self, add_value_observer:AddValueSubscriber)->None:
        if add_value_observer not in self._add_value_subscribers:
            self._add_value_subscribers.append(add_value_observer)

    def dettach_add_value_observer(self, add_value_observer: AddValueSubscriber)->None:
        if add_value_observer in self._add_value_subscribers:
            self._add_value_subscribers.remove(add_value_observer)


    @override(Decorator)
    def save(self):
        # for example in core is File then
        if self._separator is not None:
            self._inner.set_ram(self._separator.join(self._ram_values))
        else:
            self._inner.set_ram("".join(self._ram_values))
        #call save from decorator
        super().save()

    @override(MultiValuedInterface)
    def set_ram_values(self, ram_values:List)->None:
        self._ram_values = ram_values

    @override(MultiValuedInterface)
    def get_ram_values(self)->List:
        return self._ram_values

    @override(MultiValuedInterface)
    def get_ram_value_at(self, at:int)->None:
        return self._ram_values[at]

    @override(MultiValuedInterface)
    def add_to_ram_values_at(self, index: int, values: List) -> None:
        for offset, value in enumerate(values):
            self._ram_values.insert(index + offset, value)
            for add_value_observer in self._add_value_subscribers:
                add_value_observer.add_value_update(value)

    @override(MultiValuedInterface)
    def get_ram_values_by_slice(self, slc: slice) -> List:
        return self._ram_values[slc]

    @override(MultiValuedInterface)
    def add_to_ram_values(self, value:str)->None:
        self._ram_values.append(value)
        for add_value_observer in self._add_value_subscribers:
            add_value_observer.add_value_update(value)

    @override(MultiValuedInterface)
    def add_to_ram_values_slices(self, valuesSlice:ValuesSlice)->None:
        self._ram_values_slices.add_values_slice(valuesSlice)
        for add_value_observer in self._add_value_subscribers:
            for value in valuesSlice.get_values():
                add_value_observer.add_value_update(value)

    @override(MultiValuedInterface)
    def earase_ram_values(self)->None:
        self._ram_values.clear()

    @override(MultiValuedInterface)
    def get_ram_values_slices(self)->ValuesSlices:
        return self._ram_values_slices

    @override(MultiValuedInterface)
    def get_ram_values_from_values_slices_by_slice(self,slc:slice)->List[str]:
        return self._ram_values_slices.get_values_by_slice(slc)


