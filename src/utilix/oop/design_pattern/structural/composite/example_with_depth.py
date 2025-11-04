class Component:
    """Base class for Composite pattern."""

    def __init__(self, name: str):
        self._name = name

    def add(self, child: "Component") -> None:
        raise NotImplementedError

    def remove(self, child: "Component") -> None:
        raise NotImplementedError

    def children(self):
        return ()

    def is_leaf(self) -> bool:
        return True

    def depth(self) -> int:
        """Depth measured as number of levels from this node to the farthest leaf."""
        return 1  # leaf depth = 1

    def size(self) -> int:
        """Total number of nodes in the subtree rooted here."""
        return 1

    def walk(self):
        """Preorder traversal."""
        yield self

    def name(self) -> str:
        return self._name


class Leaf(Component):
    """Leaf node with no children."""
    pass


class Composite(Component):
    """Composite node that can hold other components."""

    def __init__(self, name: str):
        super().__init__(name)
        self._children = []

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


# -------- PublisherExample usage --------
if __name__ == "__main__":
    root = Composite("root")
    a = Composite("a")
    b = Leaf("b")
    a1 = Leaf("a1")
    a2 = Composite("a2")
    a21 = Leaf("a21")

    root.add(a)
    root.add(b)
    a.add(a1)
    a.add(a2)
    a2.add(a21)

    print("Depth:", root.depth())  # -> 4
    print("Size:", root.size())  # -> 6

    print("Preorder walk:")
    for node in root.walk():
        print("-", node.name())