from typing import Type, Any

from utilix.oop.klass.structure.kind.based_on_inheritence import BasedOnInheritence


class Klass:
    def __init__(self, _target_class: type):
        self._target_class = _target_class

    @classmethod
    def init_from_object(cls, obj:Any):
        return cls(obj.__class__)

    def return_klass_map(self) -> type:
        return self._target_class

    def get_module_path(self):
        return self._target_class.__module__+ "."+self._target_class.__qualname__

    def draw_inherited_classes(self):
        BasedOnInheritence(self._target_class).draw_graph()