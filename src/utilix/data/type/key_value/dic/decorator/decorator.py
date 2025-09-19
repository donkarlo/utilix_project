from typing import Dict, Any

from utilix.data.type.key_value.dic.interface import Interface as DicInterface


class Decorator(DicInterface):
    def __init__(self, inner: DicInterface):
        self._inner: DicInterface = inner

    def get_raw_dict(self) -> Dict:
        return self._inner.get_raw_dict()

    def __getattr__(self, name: str) -> Any:
        """
        Walk the inner chain to find missing attributes/methods.
        This will pass all the arguments
        """
        target: Any = self._inner
        while True:
            if hasattr(target, name):
                return getattr(target, name)
            target = getattr(target, "_inner", None)
            if target is None:
                break
        raise AttributeError(
            f"{type(self).__name__} and its inner chain have no attribute {name!r}"
        )