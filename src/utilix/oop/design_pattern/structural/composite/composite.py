from typing import List, Tuple, Iterable
from utilix.oop.design_pattern.structural.composite.component import Component

class Composite(Component):
    """Composite node that can hold other Interfaces."""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children: List[Component] = []

    def _would_create_cycle(self, child: Component) -> bool:
        # Prevent adding an ancestor as a child
        for node in child.walk():
            if node is self:
                return True
        return False

    def add_child(self, child: Component) -> None:
        if child is self:
            raise ValueError("Cannot add node to itself.")
        if self._would_create_cycle(child):
            raise ValueError("Adding this child would create a cycle.")
        self._children.append(child)

    def remove_child(self, child: Component) -> None:
        self._children.remove(child)

    def get_children(self) -> Tuple[Component, ...]:
        return tuple(self._children)

    def is_leaf(self) -> bool:
        return False

    def get_depth(self) -> int:
        if not self._children:
            return 1
        return 1 + max(ch.get_depth() for ch in self._children)

    def get_size(self) -> int:
        return 1 + sum(child.get_size() for child in self._children)

    def walk(self) -> Iterable[Component]:
        yield self
        for child in self._children:
            yield from child.walk()

    def stringify(self) -> str:
        # Simple tree-like representation
        lines = [self._name]
        for child in self._children:
            for ln in child.stringify().splitlines():
                lines.append("  " + ln)
        return "\n".join(lines)