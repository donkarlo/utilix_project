from abc import ABC, abstractmethod
from typing import Union

from utilityx.data.format.format import Format
from utilityx.data.format.value.value import Value


class FormattedValue(ABC):
    def __init__(self, format: Format, value:Union[Value, str]):
        self._format = format
        self._value = value

    @abstractmethod
    def __eq__(self, other)->bool:
        pass
