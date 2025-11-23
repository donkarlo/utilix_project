from collections.abc import MutableSequence
from typing import Any

class ValuesSlice():
    def __init__(self, values:MutableSequence, slc:slice):
        self._values:MutableSequence = values
        self._slice = slc

    def get_slice(self):
        return self._slice

    def get_values(self):
        return self._values

    def add_value(self, value:Any)->None:
        self._values.append(value)
        self._slice.stop += self._slice.step