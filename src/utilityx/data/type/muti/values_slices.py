from typing import List

from utilityx.data.type.muti.values_slice import ValuesSlice


class ValuesSlices:
    def __init__(self):
        self._values_slices_list:List[ValuesSlice] = []

    def __add_values_slice(self, values_slice:ValuesSlice):
        self._values_slices_list.append(values_slice)

    def get_by_slice(self, slc:slice)->ValuesSlice:
        for values_slice_memeber in self._values_slices_list:
            if slc == values_slice_memeber.get_slice():
                return values_slice_memeber[slc]
        values_slice  = ValuesSlice(self._values_slices_list[slc], slc)
        self.__add_values_slice(values_slice)
        return self._values_slices_list[slc]

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
