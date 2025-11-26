from typing import Any

class IndexedValue:
    def __init__(self, index:int, value:Any):
        self._index = index
        self._value = value


    def get_value(self)->Any:
        return self._value

    def get_index(self)->Any:
        return self._index