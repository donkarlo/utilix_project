from typing import Protocol
from utilix.data.type.dic.dic import Dic

class Dictable(Protocol):
    _raw_dict:Dic
    def build_dic(self)->Dic: ...
    def init_from_dic(self)->Dic: ...
