from abc import ABC, abstractmethod

class Component(ABC):
    """Base class for Composite pattern."""
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def stringify(self): ...

    def add(self, child: "Component") -> None:
        raise NotImplementedError

    def remove(self, child: "Component") -> None:
        raise NotImplementedError

    def children(self):
        return ()

    def is_leaf(self) -> bool:
        return True

    def depth(self) -> int:
        """Depth measured as number of levels from this node to the farthest leaf."""
        return 1  # leaf depth = 1

    def size(self) -> int:
        """Total number of nodes in the subtree rooted here."""
        return 1

    def walk(self):
        """Preorder traversal."""
        yield self

    def name(self) -> str:
        return self._name