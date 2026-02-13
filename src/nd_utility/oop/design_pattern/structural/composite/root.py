from nd_utility.oop.design_pattern.structural.composite.component import Component
from nd_utility.oop.design_pattern.structural.composite.composite import Composite


class Root(Composite):
    def __init__(self, composite_root:Composite):
        Composite.__init__(self, "root")
        Composite.add_child(self, composite_root)
        self._composite_root = composite_root

    def add_child(self, child: Component) -> None:
        raise ValueError("Root can have only one child")
