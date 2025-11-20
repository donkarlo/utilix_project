from typing import Type, Any


class Klass:
    def __init__(self, _target_class: type):
        self._target_class = _target_class

    def return_klass_map(self) -> type:
        return self._target_class

    def get_module_path(self):
        return self._target_class.__module__+ "."+self._target_class.__qualname__

