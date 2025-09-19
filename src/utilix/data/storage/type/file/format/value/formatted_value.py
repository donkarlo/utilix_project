from abc import ABC, abstractmethod
from typing import Union

from utilix.data.storage.type.file.format.format import Format
from utilix.data.storage.type.file.format.value.value import Value


class FormattedValue(ABC):
    def __init__(self, format: Format, value:Union[Value, str]):
        self._format = format
        self._value = value

    @abstractmethod
    def __eq__(self, other:FormattedValue)->bool:
        if not (self._format == other._format and self._value == other._value):
            return False
        return True

    def return_value(self):
        return self._value
