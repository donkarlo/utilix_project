from utilix.oop.design_pattern.structural.composite.component import Component
from typing import override


class Leaf(Component):
    """Leaf node with no children."""

    @override(Component)
    def stringify(self) -> str:
        return self.name