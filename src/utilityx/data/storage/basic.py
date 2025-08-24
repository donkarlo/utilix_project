from abc import ABC, abstractmethod

from typing import Any, override, TYPE_CHECKING, Optional

from utilityx.data.storage.access.access import Access
from utilityx.data.storage.interface import Interface as StorageInterface

class Basic(StorageInterface):
    """
    This is the conceret Object of the Decorator pattern. Here it is not concerete because between what is in type

    """
    def __init__(self, access:Optional[Access]=None):
        """

        Args:
            access: value None means every thing is allowed
        """
        self.access = access
        # from source to python variable
        self._ram: str |  None = None

    def get_ram(self)->str:
        return self._ram

    def get_access(self)->Optional[Access]:
        return self.access

    def set_ram(self, content:str):
        self._ram = content

    def earase_ram(self):
        self._ram = None