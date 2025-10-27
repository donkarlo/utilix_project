class Component:
    """Base interface for both leaf and composite objects."""

    def render(self, indent=0):
        raise NotImplementedError


class Leaf(Component):
    """Leaf node that holds a simple value."""

    def __init__(self, value):
        self.value = value

    def render(self, indent=0):
        print(" " * indent + str(self.value))


class Composite(Component):
    """Composite node that can contain children."""

    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, child: Component):
        self.children.append(child)

    def render(self, indent=0):
        print(" " * indent + self.name + " {")
        for child in self.children:
            child.render(indent + 2)
        print(" " * indent + "}")