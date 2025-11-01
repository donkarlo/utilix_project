from typing import Any, List, Type
import inspect
from abc import ABC, ABCMeta

class Decorator(ABC):
    def __init__(self, inner:Any):
        """

        Args:
            inner:
        """
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

    def get_decorator_stack(self)->List["Decorator"]:
        """
        Return the decoration stack from the most inner to the most outer Decorator.
        """
        stack: List[Decorator] = []
        seen = set()
        current: Any = self
        # Collect from outer -> inner
        while isinstance(current, Decorator) and id(current) not in seen:
            seen.add(id(current))
            stack.append(current)
            current = getattr(current, "_inner", None)
        # Reverse to inner -> outer
        stack.reverse()
        return stack

    def isinstance(self, obj: Any, decorator: Any) -> bool:
        """
        Check whether a given decorator (class or instance) exists in the decoration stack.

        Args:
            obj: The possibly decorated object (may be a Decorator or a plain inner object).
            decorator: Either a Decorator subclass (type) or a Decorator instance.

        Returns:
            True if the specified decorator type appears in the chain; otherwise False.
        """
        # Normalize the target decorator type
        if isinstance(decorator, Decorator):
            target_type: Type[Decorator] = type(decorator)
        elif isinstance(decorator, type) and issubclass(decorator, Decorator):
            target_type = decorator
        else:
            raise TypeError(
                "decorator must be a Decorator instance or a Decorator subclass"
            )

        # Walk from 'obj' inward; accept either a Decorator chain or a plain object
        seen = set()
        current: Any = obj
        while isinstance(current, Decorator) and id(current) not in seen:
            seen.add(id(current))
            if isinstance(current, target_type):
                return True
            current = getattr(current, "_inner", None)
        return False

    @classmethod
    def __instancecheck__(cls, instance):
        # Return True if any decorator in the chain is an instance of this class
        current = instance
        seen = set()
        while isinstance(current, Decorator) and id(current) not in seen:
            seen.add(id(current))
            if type(current) is cls:
                return True
            current = getattr(current, "_inner", None)
        return False