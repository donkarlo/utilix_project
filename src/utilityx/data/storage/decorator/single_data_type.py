from utilityx.data.storage.unit import unit

from utilityx.data.storage.decorator import Decorator

from utilityx.data.storage import Storage
from utilityx.data.type import Type as DataType


class SingleDataType(Decorator):
    """
    Must add the functionality of checking each string_content data type before adding
    """
    def __init__(self, inner:Storage, type:DataType):
        super().__init__(inner)
        self._type = type

    def validate_content_before_adding_to_ram_memory(self, content:str)->bool:
        self._type.validate_content(content)
        self._ram_memory = content