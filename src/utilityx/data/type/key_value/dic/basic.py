from typing import Dict, override

import overrides

from utilityx.data.type.key_value.dic.interface import Interface as DicInterface


class Basic(DicInterface):
    def __init__(self, raw_dict:Dict):
        self._raw_dict:Dict = raw_dict

    @override
    def get_raw_dict(self)->Dict:
        return self._raw_dict

    def __repr__(self):
        return f"{self.__class__.__name__}({self._raw_dict})"