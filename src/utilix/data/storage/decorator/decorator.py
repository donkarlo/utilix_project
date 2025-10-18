from abc import ABC, abstractmethod
from typing import Any, override, runtime_checkable
from utilix.data.storage.interface import Interface as StorageInterface
import inspect

class Decorator(StorageInterface):
    """
    Base storage decorator that forwards to an inner StorageInterface.
    """
    __slots__ = ("_inner",)

    def __init__(self, inner: StorageInterface):
        """
        .__inner is either the most basic object, in this case data.storage.basic.Yaml or a decorator
        Args:
            inner:
        """
        self._inner = inner

    @override
    def load(self) -> str:
        return self._inner.load()

    @override
    def save(self) -> bool:
        return self._inner.save()

    @override
    def set_ram(self,content:str)->None:
        self._inner.set_ram(content)

    @override
    def add_to_ram(self, content:str) -> None:
        self._inner.set_ram(self._inner.get_ram() + content)

    @override
    def earase_storage(self) -> bool:
        self._inner.earase_storage()

    @override
    def earase_ram(self) -> bool:
        self._inner.earase_ram()

    def get_ram(self) -> str:
        return self._inner.get_ram()

    def __getattr__(self, name: str) -> Any:
        if name.startswith("__") and name.endswith("__"):
            raise AttributeError(f"{type(self).__name__} has no attribute {name!r}")

        target: Any = self._inner
        seen = set()
        while target is not None and id(target) not in seen:
            seen.add(id(target))
            try:
                inspect.getattr_static(target, name)
                return getattr(target, name)
            except AttributeError:
                target = getattr(target, "_inner", None)
        raise AttributeError(
            f"{type(self).__name__} and its inner chain have no attribute {name!r}"
        )
