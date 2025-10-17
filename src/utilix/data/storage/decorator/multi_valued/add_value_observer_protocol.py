from typing import Protocol


class AddValueObserverProtocol(Protocol):
    def update(self, data: Any) -> None: ...