# in composition.py
from typing import Iterable, Tuple, override, Optional

from graphviz import Digraph

from nd_utility.data.kind.group.group import Group
from nd_utility.data.kind.group.kind.UniKind import UniKind as UniKindGroup
from nd_utility.oop.design_pattern.structural.composition.component import Component
from nd_utility.oop.design_pattern.structural.composition.leaf import Leaf


class Composite(Component):
    """
    Composite node that can hold other Components.
    """

    def __init__(self):
        """
        This name is useful, it can be used as path parts
        Args:
            name:
        """
        Component.__init__(self)
        self._children = Group()

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
        self._children.add_member(child)

    def remove_child(self, child: Component) -> None:
        self._children.remove_member(child)

    def has_direct_child(self, child: Component) -> bool:
        for current_child in self._children:
            # is for verifying if the two child refer to teh same RAM address
            if current_child is child:
                return True
        return False

    def get_child_by_path_parts(self, path_parts: list[str]) -> Component:
        """
        Traverse the composition hierarchy following the given path_parts.
        Example:
            path_parts = ["A", "B", "C"]
            returns the component named C under A/B/C
        """
        if not path_parts:
            raise ValueError("Path parts list cannot be empty.")
        current: Component = self
        for part in path_parts:
            found = None
            for child in current.get_child_group_members():
                if child.get_name() == part:
                    found = child
                    break
            if found is None:
                raise ValueError(f"Path segment '{part}' not found under '{current.get_name()}'.")
            current = found
        return current

    def get_child_by_name(self, name: str) -> Component:
        """
        Searches ALL descendants recursively.
        Raises ValueError if no match or more than one match is found.
        """

        matches: list[Component] = []

        for node in self.walk():  # walk() already yields full subtree including self
            if node is self:
                continue
            if node.get_name() == name:
                matches.append(node)

        if len(matches) == 0:
            raise ValueError(f"No descendant named '{name}' found under '{self.get_name()}'.")

        if len(matches) > 1:
            raise ValueError(
                f"Multiple descendants named '{name}' found under '{self.get_name()}'."
            )

        return matches[0]

    def convert_leaf_to_composite(self, leaf: Leaf) -> "Composite":
        """Promote a direct child Leaf into a Composite with the same name, keeping its position."""
        # Ensure the argument is a direct child of self
        if leaf not in self._children:
            raise ValueError("Given leaf is not a direct child of this composition.")
        # Remove first to avoid transient inconsistent states
        self.remove_child(leaf)
        composite = Composite()
        composite.add_child(leaf)
        self.add_child(composite)
        return composite

    @override
    def get_tree(self, prefix: str = "", is_last: bool = True) -> str:
        lines = [prefix + ("└── " if is_last else "├── ") + self.get_name()]
        children = list(self.get_child_group_members())
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
        for child in self.get_child_group_members():
            child.get_graphviz(dot, self.get_name())
        return dot

    def get_child_group_members(self) -> Tuple[Component, ...]:
        return tuple(self._children)

    def get_children(self)-> UniKindGroup[Leaf]:
        return self._children

    def is_leaf(self) -> bool:
        return False

    def get_depth(self) -> int:
        if not self._children:
            return 1
        return 1 + max(child.get_depth() for child in self._children)

    def get_size(self) -> int:
        """
        Recursive children count from here down
        Returns:

        """
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
