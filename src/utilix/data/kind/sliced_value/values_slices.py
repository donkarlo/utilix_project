from typing import List, Optional
from utilix.data.kind.sliced_value.values_slice import ValuesSlice

class ValuesSlices:
    """
    To cache slices of situations such as reading yaml files and storing from 233 to 766
    """
    def __init__(self):
        self._values_slices_list:List[ValuesSlice] = []

    def add_values_slice(self, values_slice:ValuesSlice):
        """
        Later
        """
        self._values_slices_list.append(values_slice)

    def get_values_by_slice(self, slc:slice)->ValuesSlice:
        for values_slice in self._values_slices_list:
            if slc == values_slice.get_slice():
                return values_slice[slc]


    def slice_exists(self, slc:slice)->bool:
        """
        Does the slice exist?
        Args:
            slc:

        Returns:

        """
        for values_slice_memeber in self._values_slices_list:
            if slc == values_slice_memeber.get_slice():
                return True
        return False

    def get_values_by_slice(self, slc:slice)->Optional:
        for vs in self._values_slices_list:
            if vs.get_slice() == slc:
                return vs.get_values()
        return None

