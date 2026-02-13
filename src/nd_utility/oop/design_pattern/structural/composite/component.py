# in component.py
from abc import ABC, abstractmethod
from typing import Iterable, Tuple, Optional


class Component(ABC):
    """Base class for Composite pattern."""

    def __init__(self, name: Optional[str]) -> None:
        self._name = name

    @abstractmethod
    def stringify(self) -> str:
        ...

    # Leaf-like defaults
    def add_child(self, child: "Component") -> None:
        raise NotImplementedError

    def remove_child(self, child: "Component") -> None:
        raise NotImplementedError

    def get_children(self) -> Tuple["Component", ...]:
        return ()

    def is_leaf(self) -> bool:
        return True

    def get_depth(self) -> int:
        return 1

    def get_size(self) -> int:
        return 1

    def walk(self) -> Iterable["Component"]:
        yield self

    def get_name(self) -> str:
        return self._name

    def get_tree(self, prefix: str = "", is_last: bool = True) -> str:
        """Default leaf drawing (ASCII)."""
        return prefix + ("└── " if is_last else "├── ") + self.get_name()

    def get_graphviz(self, dot=None, parent_name: str | None = None):
        """Build a Graphviz graph in-memory only (no files)."""
        from graphviz import Digraph
        if dot is None:
            # 'name' is in-memory identifier; does not force file creation.
            dot = Digraph(comment=f"Tree ({self.get_name()})", name="in_memory_graph")
            # Keep format unconstrained here; draw() decides the output format.
        dot.node(self.get_name())
        if parent_name:
            dot.edge(parent_name, self.get_name())
        return dot

    def draw(self, fmt: str = "svg"):
        """Show Graphviz graph in PyCharm SciView without creating files."""

        import io
        import matplotlib.pyplot as plt

        dot = self.get_graphviz()
        png_bytes = dot.pipe(format="png")  # in-memory render, no files

        # Display in PyCharm's SciView
        img = plt.imread(io.BytesIO(png_bytes), format="png")
        plt.figure(figsize=(8, 8))
        plt.imshow(img)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def draw_tree(self) -> None:
        print(self.get_tree())
