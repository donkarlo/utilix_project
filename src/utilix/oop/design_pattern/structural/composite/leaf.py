# in leaf.py
from typing import override
from utilix.oop.design_pattern.structural.composite.component import Component


class Leaf(Component):
    """Leaf node with no children."""
    def __init__(self, name:str):
        Component.__init__(self, name)

    @override
    def stringify(self) -> str:
        return self.get_name()
