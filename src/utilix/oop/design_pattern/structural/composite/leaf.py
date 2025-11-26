# in leaf.py
from typing import override, Optional
from utilix.oop.design_pattern.structural.composite.component import Component
from utilix.oop.inheritance.overriding.override_from import override_from


class Leaf(Component):
    """Leaf node with no children."""
    def __init__(self, name:Optional[str]):
        Component.__init__(self, name)

    @override_from(Component)
    def stringify(self) -> str:
        return self.get_name()

    @override_from(Component)
    def get_tree(self, prefix: str = "", is_last: bool = True) -> str:
        return prefix + ("└── " if is_last else "├── ") + self.get_name()
