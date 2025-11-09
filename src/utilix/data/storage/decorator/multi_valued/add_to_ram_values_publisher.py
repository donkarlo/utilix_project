from typing import List, runtime_checkable, Protocol, Any
from utilix.data.storage.decorator.multi_valued.add_to_ram_values_subscriber import AddToRamValuesSubscriber
from utilix.data.storage.interface import Interface as StorageInterface


@runtime_checkable
class AddToRamValuesPublisher(StorageInterface, Protocol):

    def attach_add_to_ram_values_observer(self, add_observer: AddToRamValuesSubscriber) -> None:
        ...

    def dettach_add_to_ram_values_observer(self, add_observer: AddToRamValuesSubscriber) -> None:
        ...

    def notify_add_to_ram_values_subscribers(self, value:Any) -> None:
        ...