from typing import Protocol, runtime_checkable


@runtime_checkable
class Type(Protocol):
    def validate_str_value(self, value:str): ...