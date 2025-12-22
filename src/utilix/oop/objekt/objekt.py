from typing import Any, Optional, Set

from utilix.data.kind.dic.dic import Dic


class Objekt:
    """
    Wraps an input object and builds a nested Dic representation
    of its attributes.
    """

    def __init__(self, input_object: Any) -> None:
        self._input_object = input_object

    def _build_deep_dic(self, obj: Any, depth: int, visited: Set[int]) -> Any:
        """
        Recursive helper that walks the object graph and builds
        a nested Dic / repr structure.
        """
        # cycle protection
        if id(obj) in visited:
            return "<visited>"

        visited.add(id(obj))

        # unwrap Dic so we traverse the underlying dict, not Dic internals
        if isinstance(obj, Dic):
            obj = obj.get_raw_dict()

        # case 1: plain dict → traverse its items
        if isinstance(obj, dict):
            result = {}
            for key, value in Dic(obj).get_keys_values():
                if depth < 5:
                    result[key] = self._build_deep_dic(value, depth + 1, visited)
                else:
                    result[key] = repr(value)
            return Dic(result)

        # case 2: object without __dict__ → leaf
        if not hasattr(obj, "__dict__"):
            return repr(obj)

        # case 3: generic object with __dict__
        result = {}
        for key, value in Dic(obj.__dict__).get_keys_values():
            if depth < 5:
                result[key] = self._build_deep_dic(value, depth + 1, visited)
            else:
                result[key] = repr(value)

        return Dic(result)

    def get_deep_dic(self, depth: int = 0, visited: Optional[Set[int]] = None) -> Dic:
        """
        Public entry point: returns a Dic representing the nested attribute structure of the wrapped input object.
        """
        if visited is None:
            visited = set()

        result = self._build_deep_dic(self._input_object, depth, visited)

        # ensure return type is always Dic at the top level
        if isinstance(result, Dic):
            return result

        return Dic({"value": result})

    def print(self)->None:
        self.get_deep_dic().print()
