from typing import Dict, Protocol, runtime_checkable

@runtime_checkable
class Interface(Protocol):
    _raw_dict: Dict
    def get_raw_dict(self) -> Dict: ...