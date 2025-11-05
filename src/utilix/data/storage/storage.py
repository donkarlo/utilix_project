from typing import Optional

from utilix.data.storage.interface import Interface as StorageInterface

class Storage(StorageInterface):
    """
    This is the conceret Object of the Decorator pattern. Here it is not concerete because between what is in type
    - This is a single object if you want multi raw_value storage then multi_valued decorator
    """
    def __init__(self):
        # from source to python variable
        self._ram: str |  None = None

    def get_ram(self)->Optional[str]:
        if self._ram is None:
            self.load()
        return self._ram

    def set_ram(self, content:str)->None:
        self._ram = content

    def add_to_ram(self, content:str)->str:
        self._ram += content
        return self._ram

    def earase_ram(self):
        self._ram = None