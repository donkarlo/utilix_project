from abc import ABC, abstractmethod
from typing import Any, override
from utilityx.data.storage.decorator.decorator import Decorator as StorageDecorator


class Decorator(StorageInterface):
    """
    Base storage decorator that forwards to an inner StorageInterface.
    """
    __slots__ = ("_inner",)

    def __init__(self, inner: StorageInterface) -> None:
        """
        .__inner is either the most basic object, in this case data.storage.basic.Basic or a decorator
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
