from typing import Protocol, runtime_checkable, Any


@runtime_checkable
class AddValueObserverInterface(Protocol):
    def add_value_update(self, data: Any) -> None: ...