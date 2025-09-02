from abc import ABC, abstractmethod
from typing import Protocol, Any, runtime_checkable


@runtime_checkable
class Type(Protocol):
    def __init__(self):
        pass

    def validate(self, value:str)->bool:
        ...

    def get_special_object(self, value:str)->Any:
        """
        To build and return the most special object
        Args:
            value:

        Returns:

        """
        ...