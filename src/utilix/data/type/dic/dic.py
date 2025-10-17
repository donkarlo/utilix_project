from typing import Dict

from utilix.data.type.dic.interface import Interface as DicInterface


class Dic(DicInterface):
    def __init__(self, raw_dict:Dict):
        self._raw_dict:Dict = raw_dict

    def has_nested_keys(self, keys: list[str]) -> bool:
        current = self._raw_dict
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return False
        return True


    @override
    def get_raw_dict(self)->Dict:
        return self._raw_dict

    def __repr__(self):
        return f"{self.__class__.__name__}({self._raw_dict})"