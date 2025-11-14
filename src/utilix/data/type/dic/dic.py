from typing import Any, Dict, List, Tuple, Union, Sequence
from utilix.data.type.dic.interface import Interface as DicInterface

Key = Union[str, int]
KeySeq = Sequence[Key]


class Dic(DicInterface):
    def __init__(self, raw_dict: Dict):
        if not isinstance(raw_dict, dict):
            raise TypeError(f"Dic expects dict, got {type(raw_dict).__name__}")
        self._raw_dict = raw_dict

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._raw_dict})"

    def get_raw_dict(self) -> Dict:
        return self._raw_dict

    def get_keys_values(self) -> List[Tuple[str, Any]]:
        return list(self._raw_dict.items())

    def has_nested_keys(self, keys: List[str]) -> bool:
        current: Any = self._raw_dict
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return False
        return True

    def __getitem__(self, key_or_keys: Union[Key, KeySeq]) -> Any:
        if isinstance(key_or_keys, (str, int)):
            keys: Tuple[Key, ...] = (key_or_keys,)
        elif isinstance(key_or_keys, (list, tuple)):
            keys = tuple(key_or_keys)
        else:
            raise TypeError("Key must be str/int or a list/tuple of them.")

        current: Any = self._raw_dict
        for k in keys:
            if isinstance(current, Dic):  # <-- unwrap Dic during traversal
                current = current._raw_dict

            if isinstance(current, dict):
                if isinstance(k, str):
                    if k in current:
                        current = current[k]
                    else:
                        raise KeyError(f"Key path {keys} not found.")
                elif isinstance(k, int):
                    vals = list(current.values())  # allow dict[int] as i-th value
                    try:
                        current = vals[k]
                    except IndexError:
                        raise KeyError(f"Dict index {k} out of range.")
                else:
                    raise TypeError("Dict key must be str or int.")
            elif isinstance(current, list):
                if not isinstance(k, int):
                    raise TypeError("List indices must be integers.")
                try:
                    current = current[k]
                except IndexError:
                    raise KeyError(f"List index {k} out of range.")
            else:
                raise TypeError(f"Cannot index into {type(current).__name__}.")

        if isinstance(current, Dic):  # final unwrap if needed
            current = current._raw_dict
        return Dic(current) if isinstance(current, dict) else current

    def add_key_value(self, key: Union[int, str], value: Any, create_if_key_not_exists: bool) -> None:
        if create_if_key_not_exists or key in self._raw_dict:
            self._raw_dict[key] = value
        else:
            raise KeyError("the key doesn't exist")

    def add_values_to_key(self, values:List[Any], create_if_key_not_exists: bool ) -> None:
        if key in self._raw_dict:
            if self._raw_dict[key] == None:
                self._raw_dict[key] = []
            elif not isinstance(self._raw_dict[key], list):
                self._raw_dict[key] = [self._raw_dict[key]]
            self._raw_dict[key].append(values)


    def get_keys_and_values(self) -> List[Tuple[str, Any]]:
        return self._raw_dict.items()

    def get_keys(self)->List[Tuple[str, Any]]:
        return self._raw_dict.keys()

    def get_values(self)->List[Any]:
        return self._raw_dict.values()

