from typing import Dict, Protocol


class Interface(Protocol):
    _raw_dict: Dict

    def get_raw_dict(self) -> Dict:
        ...