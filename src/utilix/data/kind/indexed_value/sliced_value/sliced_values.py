from collections.abc import MutableSequence
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SlicedValues:
    """
    A slice of values bound to a Python slice object.
    Values are assumed to correspond to indices produced by that slice.
    """

    def __init__(self, slc: slice, values: MutableSequence):
        self._values = values
        self._slice = slc

    def get_slice(self) -> slice:
        return self._slice

    def get_values(self) -> MutableSequence:
        return self._values

    def iter_index_value(self):
        """
        Yield (index, value) pairs according to the stored slice.
        """
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
        if self._values is None:
            self._values = []

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