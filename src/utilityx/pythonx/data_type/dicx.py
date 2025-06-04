from typing import Any, Union, Sequence
from collections import defaultdict,Hashable

class Dicx:
    def __init__(self, raw_input:dict):
        self._raw_dict = raw_input

    def get_by_key_if_noexist_empty_dict(self, key:str)->dict:
        return self._raw_dict.get(key, {})

    def get_by_key_covered_by_key_error(self,key)->Any:
        try:
            return self._raw_dict[key]
        except KeyError:
            raise KeyError(f"key {key} not found in dict")

    def __getitem__(self, key:str)->Any:
        try:
            return self._raw_dict[key]
        except KeyError:
            raise KeyError(f"key {key} not found in dict")



