from utilix.oop.design_pattern.structural.composite.component import Component


class Composite(Component):
    """Composite node that can hold other components."""

    def __init__(self, name: str):
        super().__init__(name)
        self._children:Component = []

    def add(self, child: Component) -> None:
        if child is self:
            raise ValueError("Cannot add node to itself.")
        self._children.append(child)

    def remove(self, child: Component) -> None:
        self._children.remove(child)

    def children(self):
        return tuple(self._children)

    def is_leaf(self) -> bool:
        return False

    def depth(self) -> int:
        if not self._children:
            return 1
        return 1 + max(ch.depth() for ch in self._children)

    def size(self) -> int:
        return 1 + sum(ch.size() for ch in self._children)

    def walk(self):
        yield self
        for ch in self._children:
            yield from ch.walk()