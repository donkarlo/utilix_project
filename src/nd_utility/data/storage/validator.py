from abc import ABC, abstractmethod
from typing import Any


class Vaidator(ABC):
    """
    """

    def __init__(self, value: Any):
        self._value = value

    def get_value(self) -> Any:
        return self._value

    @abstractmethod
    def validate(self) -> bool: ...
