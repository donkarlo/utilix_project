from utilityx.data.storage.interface import Interface as StorageInterface
from utilityx.data.storage.decorator.decorator import Decorator as StorageDecorator
from utilityx.data.type.type import Type as DataType

class SingleValued(StorageDecorator):
    def __init__(self, inner: StorageInterface , data_type: DataType):
        self._data_type = data_type
        super().__init__(inner)

    def set_ram(self, ram:str)->None:
        if not __validate_ram(ram):
            raise ValueError(f"ram {ram} is not valid.")
        super().set_ram(ram)

    def save(self)->None:
        if not __validate_ram(self.get_ram()):
            raise ValueError(f"ram {self.get_ram()} is not valid.")
            raise ValueError(f"ram {ram} is not valid.")
        super().save(ram)

    def __validate_ram(self, ram:str)->bool:
        return self._data_type.validate(ram)