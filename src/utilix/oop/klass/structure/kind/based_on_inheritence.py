from typing import Any, Dict, Set, Optional, Sequence

from utilix.data.kind.dic.dic import Dic
from utilix.oop.klass.structure.structure import Structure
from graphviz import Digraph


class BasedOnInheritence(Structure):
    """
    Builds a Dic tree for a class (or instance) using ONLY inheritance:

    - The root node is the given class (or the type of the given instance).
    - Children of each node are its direct base classes (cls.__bases__),
      recursively.
    - Multiple inheritance is fully supported: if a class has several bases,
      all of them appear as children.

    Notes
    -----
    - No filtering on modules is applied. All classes are included
      (ABC, Protocol, etc.).
    - The 'object' base is skipped for readability. If you want it as well,
      remove the 'if base is object' check.
    """

    def __init__(self, target: Any, filtered: bool = False, max_depth: Optional[int] = None,
                 project_prefixes: Optional[Sequence[str]] = None) -> None:
        if isinstance(target, type):
            klass = target
        else:
            klass = type(target)

        super().__init__(klass, None, None)
        self._klass: type = klass

        # Kept for backward compatibility with older call sites.
        self._filtered: bool = filtered
        self._max_depth: Optional[int] = max_depth
        self._project_prefixes: Optional[Sequence[str]] = project_prefixes

    def get_tree(self) -> Dic:
        """
        Return a Dic representing the inheritance tree going UPWARDS
        from the given class to all its base classes (recursively),
        following cls.__bases__.
        """
        visited: Set[type] = set()

        tree: Dict[str, Any] = {}
        root_key = self._class_key(self._klass)
        tree[root_key] = {}

        self._build_upward_subtree(self._klass, tree[root_key], visited)

        return Dic(tree)

    def draw_tree(self) -> None:
        tree = self.get_tree()
        tree.draw()

    def _build_upward_subtree(self, cls: type, subtree: Dict[str, Any], visited: Set[type]) -> None:
        """
        Recursively fill 'subtree' with all base classes of 'cls'
        using cls.__bases__, handling multiple inheritance and avoiding cycles.
        """
        if cls in visited:
            return

        visited.add(cls)

        try:
            bases = cls.__bases__
        except AttributeError:
            return

        for base in bases:
            # Skip 'object' for a cleaner graph. Remove this check
            # if you want 'object' to appear as well.
            if base is object:
                continue

            base_key = self._class_key(base)
            if base_key not in subtree:
                subtree[base_key] = {}

            self._build_upward_subtree(base, subtree[base_key], visited)

    def _class_key(self, cls: type) -> str:
        module_name = getattr(cls, "__module__", "")
        qualname = getattr(cls, "__qualname__", cls.__name__)
        if module_name == "" or module_name == "__main__":
            return qualname
        return f"{module_name}.{qualname}"

    def draw_graph(self) -> None:
        dot = Digraph(
            name="Inheritance",
            format="png",
            graph_attr={
                "rankdir": "BT",  # Bottom -> Top: root class at the bottom
            },
            edge_attr={
                "arrowhead": "empty",  # hollow arrow heads
            },
        )

        visited: Set[type] = set()
        self._add_class_to_graph(self._klass, dot, visited)

        dot.view(cleanup=True)

    def _add_class_to_graph(self, cls: type, dot: Digraph, visited: Set[type]) -> None:
        if cls in visited:
            return
        visited.add(cls)

        cls_key = self._class_key(cls)

        # Highlight the root class with a light orange fill
        if cls is self._klass:
            dot.node(cls_key, label=cls_key, style="filled", fillcolor="lightgoldenrod1")
        else:
            dot.node(cls_key, label=cls_key)

        try:
            bases = cls.__bases__
        except AttributeError:
            return

        for base in bases:
            if base is object:
                continue

            base_key = self._class_key(base)
            dot.node(base_key, label=base_key)

            # Child -> Base, with rankdir=BT => arrows visually go upward
            dot.edge(cls_key, base_key)

            self._add_class_to_graph(base, dot, visited)


