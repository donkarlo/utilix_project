from typing import Iterable, List, Optional, Tuple

from graphviz import Digraph

from nd_utility.data.kind.group.group import Group
from nd_utility.data.kind.group.kind.UniKind import UniKind as UniKindGroup
from nd_utility.oop.design_pattern.structural.composition.component import Component
from nd_utility.oop.design_pattern.structural.composition.leaf import Leaf


class Composite(Component):

    def __init__(self):
        Component.__init__(self)
        self._children = Group()

    def _would_create_cycle(self, child: Component) -> bool:
        for node in child.walk():
            if node is self:
                return True
        return False

    def _has_direct_child_by_identity(self, child: Component) -> bool:
        for existing_child in self._children:
            if existing_child is child:
                return True
        return False

    def _generate_child_auto_name(self, child: Component) -> str:
        """
        Generates an auto name like Mind_1, Mind_2, Body_1, ...
        This is stored internally for debugging and uniqueness in naming.
        The rendered label is still the class name unless the name was explicitly set.
        """
        base_name = child.__class__.__name__

        count = 0
        for existing_child in self.get_child_group_members():
            if existing_child.__class__.__name__ == base_name:
                count += 1

        return base_name + "_" + str(count + 1)

    def add_child(self, child: Component) -> None:

        if child is self:
            raise ValueError("Cannot add node to itself.")

        if self._would_create_cycle(child):
            raise ValueError("Adding this child would create a cycle.")

        if self._has_direct_child_by_identity(child):
            return

        auto_name = self._generate_child_auto_name(child)
        child.set_auto_name_if_missing(auto_name)

        self._children.add_member(child)

    def add_children(self, children: List[Component]) -> None:
        self._children.add_members(children)

    def remove_child(self, child: Component) -> None:
        self._children.remove_member(child)

    def has_direct_child(self, child: Component) -> bool:
        return self._has_direct_child_by_identity(child)

    def get_child_group_members(self) -> Tuple[Component, ...]:
        return tuple(self._children)

    def get_children(self) -> UniKindGroup[Leaf]:
        return self._children

    def is_leaf(self) -> bool:
        return False

    def get_depth(self) -> int:

        if not self._children:
            return 1

        return 1 + max(current_child.get_depth() for current_child in self._children)

    def get_size(self) -> int:
        return 1 + sum(current_child.get_size() for current_child in self._children)

    def walk(self) -> Iterable[Component]:

        yield self

        for current_child in self._children:
            yield from current_child.walk()

    def stringify(self) -> str:

        lines = [self.get_name()]

        for child in self._children:
            child_lines = child.stringify().splitlines()
            for child_line in child_lines:
                lines.append("  " + child_line)

        return "\n".join(lines)

    def get_tree(self, prefix: str = "", is_last: bool = True) -> str:

        branch = "└── "
        if not is_last:
            branch = "├── "

        lines = [prefix + branch + self.get_name()]

        children = list(self.get_child_group_members())

        for index, child in enumerate(children):

            is_child_last = False
            if index == len(children) - 1:
                is_child_last = True

            new_prefix = prefix
            if is_last:
                new_prefix = new_prefix + "    "
            else:
                new_prefix = new_prefix + "│   "

            lines.append(child.get_tree(new_prefix, is_child_last))

        return "\n".join(lines)

    def get_graphviz(self, dot=None, parent_identifier: Optional[str] = None) -> Digraph:
        dot = Component.get_graphviz(self, dot=dot, parent_identifier=parent_identifier)

        current_node_identifier = self.get_graphviz_node_identifier()

        for child in self.get_child_group_members():
            child.get_graphviz(dot=dot, parent_identifier=current_node_identifier)

        return dot