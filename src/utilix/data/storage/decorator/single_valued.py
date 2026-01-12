from typing import Any

from utilix.data.storage.interface import Interface as StorageInterface
from utilix.data.storage.decorator.decorator import Decorator as StorageDecorator
from utilix.data.kind.core.kind import Kind as DataType

class SingleValued(StorageDecorator):
    def __init__(self, inner: StorageInterface , data_type: DataType):
        super().__init__(inner)
        self._data_type = data_type

    def get_special_ram_object(self)->Any:
        ram = self.get_ram()
        special_ram_object = self._data_type.get_special_object(ram)
        return special_ram_object

    def set_ram(self, ram:str)->None:
        if not self.__validate_ram(ram):
            raise ValueError(f"ram {ram} is not valid.")
        super().set_ram(ram)

    def save(self)->None:
        if not self.__validate_ram(self.get_ram()):
            raise ValueError(f"ram {self.get_ram()} is not valid.")
        super().save(self.get_ram())

    def __validate_ram(self, ram:str)->bool:
        return self._data_type.is_of_my_kind(ram)