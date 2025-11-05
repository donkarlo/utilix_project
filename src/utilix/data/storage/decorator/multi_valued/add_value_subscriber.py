from typing import Protocol, runtime_checkable, Any


@runtime_checkable
class AddValueSubscriber(Protocol):
    def add_value_update(self, value: Any) -> None: ...