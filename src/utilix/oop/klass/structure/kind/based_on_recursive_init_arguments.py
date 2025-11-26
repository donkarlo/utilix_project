from typing import Any, Dict, List, Set, get_type_hints, get_origin, get_args

from utilix.data.kind.dic.dic import Dic
from utilix.oop.klass.structure.structure import Structure


class BasedOnRecursiveInitArguments(Structure):
    """
    Builds a Dic tree for a class (or instance) with:
    - An inheritance chain from the top-most base (excluding object) down to the class.
    - Downward edges from the given class based on:
        * __init__ type hints (parameter types).
        * Protected attributes of the root instance (if an instance is provided),
          scanned recursively to discover nested classes (e.g. inner, formatted_data, etc.).
    """

    def __init__(self, target: Any) -> None:
        if isinstance(target, type):
            klass = target
            instance = None
        else:
            klass = type(target)
            instance = target

        super().__init__(klass)
        self._klass: type = klass
        self._instance: Any = instance

    def get_tree(self) -> Dic:
        visited_down: Set[type] = set()

        # 1) Build inheritance chain: top-most base -> ... -> klass
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

        # 2) From klass node, go down through related classes
        self._add_related_subtree(self._klass, klass_node, visited_down)

        return Dic(tree)

    def _add_related_subtree(self, cls: type, subtree: Dict[str, Any], visited: Set[type]) -> None:
        if cls in visited:
            return

        visited.add(cls)

        # 1) Related classes from __init__ type hints
        related_classes: List[type] = self._get_related_from_init(cls)

        # 2) Additional classes from the root instance (runtime graph)
        if self._instance is not None and cls is self._klass:
            visited_instances: Set[int] = set()
            self._scan_instance_for_classes(self._instance, related_classes, visited_instances)

        for child_cls in related_classes:
            child_key = self._class_key(child_cls)
            if child_key not in subtree:
                subtree[child_key] = {}
            self._add_related_subtree(child_cls, subtree[child_key], visited)

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

    def _scan_instance_for_classes(self, obj: Any, collector: List[type], visited_instances: Set[int]) -> None:
        obj_id = id(obj)
        if obj_id in visited_instances:
            return

        visited_instances.add(obj_id)

        obj_type = type(obj)
        if self._is_relevant_class(obj_type):
            if obj_type is not self._klass or obj is not self._instance:
                if obj_type not in collector:
                    collector.append(obj_type)

        try:
            attrs = vars(obj)
        except TypeError:
            return

        for attr_name, value in attrs.items():
            if not isinstance(attr_name, str):
                continue
            if not attr_name.startswith("_"):
                continue
            if value is None:
                continue
            self._scan_instance_for_classes(value, collector, visited_instances)

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
                if self._is_relevant_class(arg):
                    result.append(arg)
            else:
                nested = self._iter_relevant_types(arg)
                if len(nested) > 0:
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

        return True

    def _class_key(self, cls: type) -> str:
        module_name = getattr(cls, "__module__", "")
        qualname = getattr(cls, "__qualname__", cls.__name__)
        if module_name == "" or module_name == "__main__":
            return qualname
        return f"{module_name}.{qualname}"
