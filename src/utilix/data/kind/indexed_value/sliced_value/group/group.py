from typing import List, Optional
from utilix.data.kind.indexed_value.sliced_value.sliced_values import SlicedValues
from collections.abc import MutableSequence
from typing import Any


class Group:
    """
    To cache slices of situations such as reading yaml files and storing from 233 to 766
    """

    def __init__(self):
        self._sliced_values_list: List[SlicedValues] = []
        self._combined_values_slice: Optional[SlicedValues] = None
        self._broadest_values_slice: Optional[SlicedValues] = None

    def add_values_slice(self, values_slice: SlicedValues) -> None:
        self._sliced_values_list.append(values_slice)
        self._combined_values_slice = None
        self._broadest_values_slice = None

    def slice_exists(self, slc: slice) -> bool:
        for member in self._sliced_values_list:
            if slc == member.get_slice():
                return True
        return False

    def get_values_by_slice(self, slc: slice) -> Optional[MutableSequence]:
        for vs in self._sliced_values_list:
            if vs.get_slice() == slc:
                return vs.get_values()
        return None

    def get_newest_slice_values(self) -> SlicedValues:
        return self._sliced_values_list[-1]

    def get_the_broadest_one(self) -> SlicedValues:
        """
        Broadest range ignoring step compatibility.
        Step is set to 1.
        """
        if not self._sliced_values_list:
            raise ValueError("No SlicedValues in Finite.")

        min_start = None
        max_stop = None

        for vs in self._sliced_values_list:
            slc = vs.get_slice()
            start = slc.start if slc.start is not None else 0
            stop = slc.stop

            if stop is None:
                # Infer stop from values length and step
                step = slc.step if slc.step is not None else 1
                stop = start + step * len(vs.get_values())

            if min_start is None or start < min_start:
                min_start = start
            if max_stop is None or stop > max_stop:
                max_stop = stop

        self._broadest_values_slice = SlicedValues([], slice(min_start, max_stop, 1))
        return self._broadest_values_slice

    def get_one_steped_combined(self) -> SlicedValues:
        """
        Combine all slices into a single SlicedValues with step=1.
        Later slices overwrite earlier ones on overlaps.
        """
        if not self._sliced_values_list:
            raise ValueError("No SlicedValues in Finite.")

        broadest = self.get_the_broadest_one().get_slice()
        start = broadest.start if broadest.start is not None else 0
        stop = broadest.stop
        if stop is None:
            raise ValueError("Broadest stop could not be inferred.")

        index_to_value: Dict[int, Any] = {}

        for vs in self._sliced_values_list:
            for idx, val in vs.iter_index_value():
                index_to_value[idx] = val  # newest wins

        combined_values: List[Any] = []
        for idx in range(start, stop):
            if idx in index_to_value:
                combined_values.append(index_to_value[idx])
            else:
                combined_values.append(None)

        return SlicedValues(combined_values, slice(start, stop, 1))

    def get_combined(self) -> SlicedValues:
        """
        Try to return a combined SlicedValues that preserves a common step
        only if all steps are equal and aligned. Otherwise fallback to step=1.
        """
        if self._combined_values_slice is not None:
            return self._combined_values_slice

        if not self._sliced_values_list:
            raise ValueError("No SlicedValues in Finite.")

        steps: List[int] = []
        residues: List[int] = []

        min_start = None
        max_stop = None

        for vs in self._sliced_values_list:
            slc = vs.get_slice()
            start = slc.start if slc.start is not None else 0
            step = slc.step if slc.step is not None else 1
            stop = slc.stop

            if stop is None:
                stop = start + step * len(vs.get_values())

            steps.append(step)
            residues.append(start % step)

            if min_start is None or start < min_start:
                min_start = start
            if max_stop is None or stop > max_stop:
                max_stop = stop

        common_step = steps[0]
        all_same_step = True
        for s in steps[1:]:
            if s != common_step:
                all_same_step = False
                break

        aligned = True
        if all_same_step:
            r0 = residues[0]
            for r in residues[1:]:
                if r != r0:
                    aligned = False
                    break
        else:
            aligned = False

        if not all_same_step or not aligned:
            self._combined_values_slice = self.get_one_steped_combined()
            return self._combined_values_slice

        # Safe to preserve common step
        index_to_value: Dict[int, Any] = {}
        for vs in self._sliced_values_list:
            for idx, val in vs.iter_index_value():
                index_to_value[idx] = val

        start = min_start
        stop = max_stop

        combined_values: List[Any] = []
        idx = start
        while idx < stop:
            if idx in index_to_value:
                combined_values.append(index_to_value[idx])
            else:
                combined_values.append(None)
            idx += common_step

        self._combined_values_slice = SlicedValues(combined_values, slice(start, stop, common_step))
        return self._combined_values_slice