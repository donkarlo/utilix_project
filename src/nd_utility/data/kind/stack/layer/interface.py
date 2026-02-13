from typing import Protocol, runtime_checkable, Any


@runtime_checkable
class Interface(Protocol):
    _data: Any
    def get_data(self): ...


