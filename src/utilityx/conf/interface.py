from typing import Protocol, Dict, Any

class Interface(Protocol):
    props:Dict[str, Any]
    def _do_init_props(self): ...