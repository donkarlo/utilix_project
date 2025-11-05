from typing import List, runtime_checkable, Protocol, Any
from utilix.data.storage.decorator.multi_valued.add_value_subscriber import AddValueSubscriber
from utilix.data.storage.interface import Interface as StorageInterface


@runtime_checkable
class AddValuePublisher(StorageInterface, Protocol):
    def get_values_by_slice(self, slc: slice) -> List:
        """
        Retirns a list of strings as document
        Args:
            slc:

        Returns:

        """
        ...

    def attach_add_value_observer(self, add_observer: AddValueSubscriber) -> None:
        ...

    def dettach_add_value_observer(self, add_observer: AddValueSubscriber) -> None:
        ...

    def notify_add_value_subscribers(self, value:Any) -> None:
        pass