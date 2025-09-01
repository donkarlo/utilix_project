from typing import Dict
from utilityx.data.type.key_value.dic.interface import Interface as DicInterface


class Basic(DicInterface):
    def __init__(self, raw_dict:Dict):
        self._raw_dict:Dict = raw_dict