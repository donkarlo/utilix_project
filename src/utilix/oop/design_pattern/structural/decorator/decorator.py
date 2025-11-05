from typing import Any, List, Type
import inspect
from abc import ABC


class Decorator(ABC):
    def __init__(self, inner: Any):
        self._inner = inner

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

    def get_decorator_stack(self) -> List["Decorator"]:
        stack: List[Decorator] = []
        seen = set()
        current: Any = self
        while hasattr(current, "_inner") and issubclass(current.__class__, Decorator) and id(current) not in seen:
            seen.add(id(current))
            stack.append(current)
            current = getattr(current, "_inner", None)
        stack.reverse()
        return stack

    def isinstance(self, decorator: Any) -> bool:
        if hasattr(decorator, "_inner") and issubclass(decorator.__class__, Decorator):
            target_type: Type[Decorator] = decorator.__class__
        elif isinstance(decorator, type) and issubclass(decorator, Decorator):
            target_type = decorator
        else:
            raise TypeError("decorator must be a Decorator instance or subclass")

        seen = set()
        current: Any = self
        while hasattr(current, "_inner") and issubclass(current.__class__, Decorator) and id(current) not in seen:
            seen.add(id(current))
            if issubclass(current.__class__, target_type):
                return True
            current = getattr(current, "_inner", None)
        return False

    @classmethod
    def __instancecheck__(cls, instance: Any) -> bool:
        current = instance
        seen = set()
        if not hasattr(current, "_inner") or not issubclass(current.__class__, Decorator):
            return False

        while hasattr(current, "_inner") and issubclass(current.__class__, Decorator) and id(current) not in seen:
            seen.add(id(current))
            if issubclass(current.__class__, cls):
                return True
            current = getattr(current, "_inner", None)
        return False
