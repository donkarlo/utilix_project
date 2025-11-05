from typing import Protocol, runtime_checkable

@runtime_checkable
class Interface(Protocol):
    _var:Any
    def method(self): ...
