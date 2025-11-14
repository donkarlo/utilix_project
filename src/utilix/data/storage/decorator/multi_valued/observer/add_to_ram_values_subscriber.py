from typing import Protocol, runtime_checkable, Any


@runtime_checkable
class AddToRamValuesSubscriber(Protocol):
    def do_when_a_new_value_is_added_to_ram(self, value: Any) -> None: ...