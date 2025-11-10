# in component.py
from abc import ABC, abstractmethod
from typing import Iterable, Tuple


class Component(ABC):
    """Base class for Composite pattern."""

    def __init__(self, name: str) -> None:
        self._name = name

    @abstractmethod
    def stringify(self) -> str:
        ...

    # Leaf-like defaults
    def add_child(self, child: "Component") -> None:
        raise NotImplementedError

    def remove_child(self, child: "Component") -> None:
        raise NotImplementedError

    def get_children(self) -> Tuple["Component", ...]:
        return ()

    def is_leaf(self) -> bool:
        return True

    def get_depth(self) -> int:
        return 1

    def get_size(self) -> int:
        return 1

    def walk(self) -> Iterable["Component"]:
        yield self

    def get_name(self) -> str:
        return self._name

    def get_tree(self, prefix: str = "", is_last: bool = True) -> str:
        """Default leaf drawing."""
        return prefix + ("└── " if is_last else "├── ") + self.get_name()

    def get_graphviz(self, dot=None, parent_name: str | None = None):
        """Default leaf node for Graphviz."""
        from graphviz import Digraph
        if dot is None:
            dot = Digraph(comment=f"Tree ({self.get_name()})")
        dot.node(self.get_name())
        if parent_name:
            dot.edge(parent_name, self.get_name())
        return dot

    def draw(self)->None:
        self.get_graphviz().render("tree", view=True)

    def draw_tree(self)->None:
        print(self.get_tree())
