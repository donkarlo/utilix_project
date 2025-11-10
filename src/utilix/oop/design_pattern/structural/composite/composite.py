# in composite.py
from typing import Iterable, List, Tuple, Optional, override
from utilix.oop.design_pattern.structural.composite.component import Component
from utilix.oop.design_pattern.structural.composite.leaf import Leaf
from graphviz import Digraph


class Composite(Component):
    """
    Composite node that can hold other Components.
    """
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
        # Optional: forbid duplicates
        if child in self._children:
            return
        self._children.append(child)

    def remove_child(self, child: Component) -> None:
        self._children.remove(child)

    def get_child(self, child: Component) -> Component:
        # If you prefer Optional: change return kind to Optional[Component] and return None instead of raising
        for c in self._children:
            if c is child:
                return c
        raise ValueError("Child not found.")

    def convert_leaf_to_composite(self, leaf: Leaf) -> "Composite":
        """Promote a direct child Leaf into a Composite with the same name, keeping its position."""
        # Ensure the argument is a direct child of self
        if leaf not in self._children:
            raise ValueError("Given leaf is not a direct child of this composite.")
        # Remove first to avoid transient inconsistent states
        self.remove_child(leaf)
        composite = Composite(leaf.get_name())
        composite.add_child(leaf)
        self.add_child(composite)
        return composite

    @override
    def get_tree(self, prefix: str = "", is_last: bool = True) -> str:
        lines = [prefix + ("└── " if is_last else "├── ") + self.get_name()]
        children = list(self.get_children())
        for i, child in enumerate(children):
            is_child_last = (i == len(children) - 1)
            new_prefix = prefix + ("    " if is_last else "│   ")
            lines.append(child.get_tree(new_prefix, is_child_last))
        return "\n".join(lines)

    @override
    def get_graphviz(self, dot=None, parent_name: str | None = None) -> Digraph:
        if dot is None:
            dot = Digraph(comment=f"Composite Tree ({self.get_name()})")
        dot.node(self.get_name())
        if parent_name:
            dot.edge(parent_name, self.get_name())
        for child in self.get_children():
            child.get_graphviz(dot, self.get_name())
        return dot

    def get_children(self) -> Tuple[Component, ...]:
        return tuple(self._children)

    def is_leaf(self) -> bool:
        return False

    def get_depth(self) -> int:
        if not self._children:
            return 1
        return 1 + max(child.get_depth() for child in self._children)

    def get_size(self) -> int:
        return 1 + sum(child.get_size() for child in self._children)

    def walk(self) -> Iterable[Component]:
        yield self
        for child in self._children:
            yield from child.walk()

    def stringify(self) -> str:
        lines = [self.get_name()]
        for child in self._children:
            for ln in child.stringify().splitlines():
                lines.append("  " + ln)
        return "\n".join(lines)
