from typing import Any, Union, Sequence, Dict
from collections import defaultdict,Hashable

class Basic(Interface):
    def __init__(self, raw_dict:Dict):
        self._raw_dict:Dict = raw_dict




