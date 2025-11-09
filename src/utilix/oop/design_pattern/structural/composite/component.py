from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable, List, Tuple


class Component(ABC):
    """Base class for Composite pattern."""

    def __init__(self, name: str) -> None:
        self._name = name

    @abstractmethod
    def stringify(self) -> str:
        """Return a string representation of the subtree."""
        ...

    # Default leaf-like behavior
    def add_child(self, child: "Component") -> None:
        raise NotImplementedError

    def remove_child(self, child: "Component") -> None:
        raise NotImplementedError

    def get_children(self) -> Tuple["Component", ...]:
        return ()

    def is_leaf(self) -> bool:
        return True

    def get_depth(self) -> int:
        return 1  # leaf depth = 1

    def get_size(self) -> int:
        return 1

    def walk(self) -> Iterable["Component"]:
        """Preorder traversal."""
        yield self

    def get_name(self) -> str:
        return self._name