from typing import Any, Union, Sequence
from collections import defaultdict,Hashable

class Dicx:
    def __init__(self, raw_input:dict):
        self._counter = 0
        self._ids: Dict[str, int] = {}
        self._raw_dict = raw_input

    def get_path_ids(self, d: Dict[str, Any], prefix: str = "") -> None:
        for k, v in d.items():
            path = f"{prefix}/{k}" if prefix else k
            if isinstance(v, dict):
                # Recurse into sub-dictionaries
                self.get_path_ids(v, path)
            else:
                # Leaf node: assign unique ID
                self._ids[path] = self._counter
                self._counter += 1
                

    def get_by_key_if_noexist_empty_dict(self, key:str)->dict:
        return self._raw_dict.get(key, {})

    def get_by_key_covered_by_key_error(self,key)->Any:
        try:
            return self._raw_dict[key]
        except KeyError:
            raise KeyError(f"key {key} not found in dict")

    def get_paths(self):


    def __getitem__(self, key:str)->Any:
        try:
            return self._raw_dict[key]
        except KeyError:
            raise KeyError(f"key {key} not found in dict")



