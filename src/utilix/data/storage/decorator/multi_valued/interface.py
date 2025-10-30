from typing import List, runtime_checkable, Protocol
from utilix.data.storage.decorator.multi_valued.add_value_observer_interface import AddValueObserverInterface
from utilix.data.storage.interface import Interface as StorageInterface

@runtime_checkable
class Interface(StorageInterface, Protocol):
    def get_values_by_slice(self, slc:slice)->List:
        """
        Retirns a list of strings as document
        Args:
            slc:

        Returns:

        """
        ...
    def attach_add_value_observer(self, add_observer: AddValueObserverInterface)->None:
        ...

    def dettach_add_value_observer(self, add_observer: AddValueObserverInterface)->None:
        ...