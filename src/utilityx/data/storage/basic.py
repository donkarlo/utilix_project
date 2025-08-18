from abc import ABC, abstractmethod

from typing import Any, override
from utilityx.data.storage.access import Access
from utilityx.data.storage.interface import Interface as StorageInterface


class Basic(StorageInterface):
    """
    This is the conceret Object of the Decorator pattern. Here it is not concerete because between what is in type

    """
    def __init__(self, access:Access):
        self._access = access
        # from source to python variable
        self._ram: str = None

    def set_ram(self, content:str):
        self._ram = content

    def add_to_ram(self, content:str):
        self._ram += content

    def earase_ram(self):
        self._ram = None