import pickle
from typing import Any, Dict, List, Tuple

class ModulePathRemappingUnpickler(pickle.Unpickler):
    def __init__(self, file_handle, ordered_prefix_remap: List[Tuple[str, str]], qualified_class_remap: Dict[Tuple[str, str], str]):
        super().__init__(file_handle)
        self._ordered_prefix_remap = ordered_prefix_remap
        self._qualified_class_remap = qualified_class_remap

    def _remap_prefix(self, dotted_path: str) -> str:
        for old_prefix, new_prefix in self._ordered_prefix_remap:
            if dotted_path == old_prefix or dotted_path.startswith(old_prefix + "."):
                return new_prefix + dotted_path[len(old_prefix):]
        return dotted_path

    def find_class(self, module: str, name: str) -> Any:
        # A) Normalize rare case: pickle sometimes stores name like "a.b.ClassName"
        if "." in name:
            name_module_part, name_class_part = name.rsplit(".", 1)
            module = module + "." + name_module_part
            name = name_class_part

        # B) Prefix remap first (so qualified remap can match remapped module too)
        remapped_module = self._remap_prefix(module)

        # C) Qualified (module,name) remap: check both original and remapped module
        key_original = (module, name)
        key_remapped = (remapped_module, name)

        if key_original in self._qualified_class_remap:
            new_module = self._qualified_class_remap[key_original]
            return super().find_class(new_module, name)

        if key_remapped in self._qualified_class_remap:
            new_module = self._qualified_class_remap[key_remapped]
            return super().find_class(new_module, name)

        # D) Default
        return super().find_class(remapped_module, name)