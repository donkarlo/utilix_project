from collections.abc import Iterable
from typing import List
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class SlicedValues(Iterable):
    def __init__(self, slc: slice, values: Optional[List]) -> None:
        if values is None:
            self._values = []
        else:
            self._values = values
        self._slice = slc

    def get_slice(self) -> slice:
        return self._slice

    def get_values(self) -> List:
        return self._values

    def iter_index_value(self):
        start = self._slice.start
        stop = self._slice.stop
        step = self._slice.step

        if start is None:
            start = 0
        if step is None:
            step = 1
        if stop is None:
            stop = start + step * len(self._values)

        idx = start
        i = 0
        while idx < stop and i < len(self._values):
            yield idx, self._values[i]
            idx += step
            i += 1

    def add_value(self, value: Any) -> None:
        self._values.append(value)

        start = self._slice.start
        stop = self._slice.stop
        step = self._slice.step

        if start is None:
            start = 0
        if step is None:
            step = 1
        if stop is None:
            stop = start + step * (len(self._values) - 1)
        else:
            stop = stop + step

        self._slice = slice(start, stop, step)

    def __getitem__(self, item):
        return self._values[item]

    def __iter__(self):
        return iter(self._values)
