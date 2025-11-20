from typing import Any, Dict, List, Set, Optional, Sequence, get_type_hints, get_origin, get_args

from utilix.data.kind.dic.dic import Dic
from utilix.oop.klass.structure.structure import Structure


class BasedOnInheritence(Structure):
    """
    Builds a Dic tree for a class (or instance) with:
    - An inheritance chain from the top-most base (excluding object) down to the class.
    - For each class node, children are classes that appear:
        * In __init__ type hints of that class.
        * In protected attributes (name starts with "_") of any instance of that class
          reachable from the root instance.

    Parameters
    ----------
    target:
        Class or instance to analyze.
    filtered:
        If True, apply depth limiting to the downward graph (related classes).
    max_depth:
        Maximum depth (starting from 0 at the root class) for the downward graph.
        Only used when filtered is True. If None, no depth limit is applied.
    project_prefixes:
        Module prefixes considered as "your projects". By default:
        ("robotix.", "physix.", "mathx.", "utilix.").
        Any class whose __module__ does not start with one of these
        prefixes will be ignored.
    """

    def __init__(self, target: Any, filtered: bool = False, max_depth: Optional[int] = None,
            project_prefixes: Optional[Sequence[str]] = None, ) -> None:
        if isinstance(target, type):
            klass = target
            instance = None
        else:
            klass = type(target)
            instance = target

        super().__init__(klass)
        self._klass: type = klass
        self._root_instance: Any = instance
        self._filtered: bool = filtered
        self._max_depth: Optional[int] = max_depth
        if project_prefixes is None:
            self._project_prefixes: Sequence[str] = ("robotix.", "physix.", "mathx.", "utilix.",)
        else:
            self._project_prefixes = project_prefixes

    def get_tree(self) -> Dic:
        visited_down: Set[type] = set()

        mro_no_object: List[type] = []
        for c in self._klass.__mro__:
            if c is not object:
                mro_no_object.append(c)
        chain: List[type] = list(reversed(mro_no_object))

        tree: Dict[str, Any] = {}
        current: Dict[str, Any] = tree
        klass_node: Dict[str, Any] = {}

        for cls in chain:
            key = self._class_key(cls)
            if key not in current:
                current[key] = {}
            if cls is self._klass:
                klass_node = current[key]
            current = current[key]

        self._add_related_subtree(self._klass, klass_node, visited_down, depth=0)

        return Dic(tree)

    def _add_related_subtree(self, cls: type, subtree: Dict[str, Any], visited: Set[type], depth: int, ) -> None:
        if cls in visited:
            return

        if self._filtered and self._max_depth is not None:
            if depth >= self._max_depth:
                return

        visited.add(cls)

        related_classes: List[type] = self._get_related_from_init(cls)

        if self._root_instance is not None:
            instance = self._find_instance_of(cls, self._root_instance, set())
            if instance is not None:
                self._add_related_from_instance(instance, related_classes)

        for child_cls in related_classes:
            child_key = self._class_key(child_cls)
            if child_key not in subtree:
                subtree[child_key] = {}
            self._add_related_subtree(child_cls, subtree[child_key], visited, depth=depth + 1)

    def _get_related_from_init(self, cls: type) -> List[type]:
        result: List[type] = []

        try:
            init = cls.__init__
        except AttributeError:
            return result

        try:
            hints = get_type_hints(init, include_extras=True)
        except Exception:
            hints = {}

        for param_name, annotation in hints.items():
            if param_name == "self":
                continue
            if param_name == "cls":
                continue
            if param_name == "return":
                continue

            extracted = self._iter_relevant_types(annotation)
            for t in extracted:
                if t not in result:
                    result.append(t)

        return result

    def _add_related_from_instance(self, instance: Any, collector: List[type]) -> None:
        try:
            attrs = vars(instance)
        except TypeError:
            return

        for name, value in attrs.items():
            if not isinstance(name, str):
                continue
            if not name.startswith("_"):
                continue
            if value is None:
                continue

            t = type(value)
            if self._is_relevant_class(t) and t not in collector:
                collector.append(t)

    def _find_instance_of(self, target_cls: type, root: Any, visited_ids: Set[int]) -> Any:
        obj_id = id(root)
        if obj_id in visited_ids:
            return None
        visited_ids.add(obj_id)

        if isinstance(root, target_cls):
            return root

        try:
            attrs = vars(root)
        except TypeError:
            return None

        for value in attrs.values():
            if value is None:
                continue
            found = self._find_instance_of(target_cls, value, visited_ids)
            if found is not None:
                return found

        return None

    def _iter_relevant_types(self, annotation: Any) -> List[type]:
        result: List[type] = []

        origin = get_origin(annotation)
        if origin is None:
            if isinstance(annotation, type):
                if self._is_relevant_class(annotation):
                    result.append(annotation)
            return result

        args = get_args(annotation)
        for arg in args:
            if isinstance(arg, type):
                if self._is_relevant_class(arg) and arg not in result:
                    result.append(arg)
            else:
                nested = self._iter_relevant_types(arg)
                for t in nested:
                    if t not in result:
                        result.append(t)

        return result

    def _is_relevant_class(self, cls: type) -> bool:
        module_name = getattr(cls, "__module__", "")

        if module_name == "builtins":
            return False
        if module_name.startswith("typing"):
            return False
        if module_name.startswith("collections.abc"):
            return False
        if module_name.startswith("numpy"):
            return False
        if module_name.startswith("matplotlib"):
            return False
        if module_name.startswith("graphviz"):
            return False
        if module_name == "abc":
            return False

        if not module_name.startswith(tuple(self._project_prefixes)):
            return False

        return True

    def _class_key(self, cls: type) -> str:
        module_name = getattr(cls, "__module__", "")
        qualname = getattr(cls, "__qualname__", cls.__name__)
        if module_name == "" or module_name == "__main__":
            return qualname
        return f"{module_name}.{qualname}"
