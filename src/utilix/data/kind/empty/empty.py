from typing import Sequence,List, Set, Dict, Union
import numpy as np
from utilix.data.kind.dic.dic import Dic

EMPTY_VERIFIABLE_TYPES = Union[Sequence, List, Set, Dict, str, Dic, Dict, None ]

class Empty:
    def __init__(self, value: EMPTY_VERIFIABLE_TYPES):
        self._value = value

    def is_empty(self)->bool:

        result = False
        if self._value is None:
            result = True
        elif isinstance(self._value, list):
            if self._value == []:
                result = True
        elif isinstance(self._value, np.ndarray):
            if self._value.size == 0:
                result = True
        elif isinstance(self._value, str):
            if self._value == "":
                result = True
        elif isinstance(self._value, dict):
            if self._value == {}:
                result = True
        elif isinstance(self._value, Dic):
            if self._value.get_raw_dict() == {}:
                result = True
        return result

