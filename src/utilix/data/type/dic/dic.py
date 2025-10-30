from typing import Dict,List,Any, Tuple, override, Union

from utilix.data.type.dic.interface import Interface as DicInterface


class Dic(DicInterface):
    def __init__(self, raw_dict:Dict):
        self._raw_dict:Dict = raw_dict

    def has_nested_keys(self, keys: List[str]) -> bool:
        current = self._raw_dict
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return False
        return True

    def get_keys_values(self)->List[Tuple[str,Any]]:
        return self._raw_dict.items()


    @override
    def get_raw_dict(self)->Dict:
        return self._raw_dict

    def __repr__(self):
        return f"{self.__class__.__name__}({self._raw_dict})"

    def __getitem__(self, key_or_keys: Union[str, tuple[str, ...]])->"Dic":
        """
        raw = {"a": {"b": {"c": 42}}}
        d = Dic(raw)

        print(d["a"])  # Dic({'b': {'c': 42}})
        print(d["a"]["b"])  # Dic({'c': 42})
        print(d["a", "b", "c"])  # 42
        Args:
            key_or_keys:

        Returns:

        """


        # Normalize input
        if isinstance(key_or_keys, str):
            keys = (key_or_keys,)
        else:
            keys = key_or_keys
        current = self._raw_dict
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                raise KeyError(f"Key path {keys} not found in dictionary.")

        if isinstance(current, dict):
            return_obj = Dic(current)
        else:
            return_obj = current
        return return_obj

    def add_key_value(self, key:Union[int, str], value:Any, create_if_key_not_exists:bool)->None:
        if self.has_nested_keys(key) or create_if_key_not_exists== True:
            self._raw_dict[key] = value
        else:
            raise KeyError(f"the key doesn exist")

