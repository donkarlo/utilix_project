from typing import Protocol, runtime_checkable, Any


@runtime_checkable
class AddToRamValuesSubscriber(Protocol):
    def add_to_ram_values_update(self, value: Any) -> None: ...