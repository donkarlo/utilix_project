from abc import ABC, abstractmethod
from typing import Optional, Any

from utilix.data.kind.empty.empty import Empty
from utilix.data.storage.interface import Interface as StorageInterface

class Storage(StorageInterface, ABC):
    """
    This is the conceret Object of the Decorator pattern. Here it is not concerete because between what is in kind
    - This is a single object if you want multi raw_value storage then multi_valued decorator
    """
    def __init__(self):
        # from os_file to python variable
        self._ram: Optional[Any] = None

    def get_ram(self)->Optional[Any]:
        if Empty(self._ram).is_empty():
            self.load()
        return self._ram

    def set_ram(self, content:Any)->None:
        self._ram = content

    def add_to_ram(self, content:Any)->Any:
        self._ram += content
        return self._ram

    def earase_ram(self)->None:
        self._ram = None

    @abstractmethod
    def load(self) -> None:
        """
        TODO: The menimim previlidge is to load into memory so that only the coputer works with it
        Returns:

        """
        ...



