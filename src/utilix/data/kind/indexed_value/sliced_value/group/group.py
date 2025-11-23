from typing import List, Optional
from utilix.data.kind.indexed_value.sliced_value.values_slice import ValuesSlice

class Group:
    """
    To cache slices of situations such as reading yaml files and storing from 233 to 766
    """
    def __init__(self):
        self._values_slices_list:List[ValuesSlice] = []

        # combined aLL and gives GroupIndexValu
        self._combined_values_slice= None
        ## with contain the brodest slice start and end
        self._broadest_values_slice = None

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

    def get_newest_slice_values(self)->ValuesSlice:
        return self._values_slices_list[-1]

    def get_the_brodest_one(self):
        current_lowest_start = None
        current_highest_end = None

        for current_values_slice in self._values_slices_list:
            current_slice = current_values_slice.get_slice()
            if current_lowest_start is None and current_highest_end is None:
                current_lowest_start = current_slice.start
                current_lowest_end = current_slice.end
            else:
                if current_slice.start < current_lowest_start:
                    current_lowest_start = current_slice.start
                if current_slice.end > current_highest_end:
                    current_highest_end = current_slice.end
        return ValuesSlice(current_lowest_start, current_highest_end)

    def combine(self):
        """
        cobine all exsuting values slices
        for every combination you need to convert to indexed values
        Returns:

        """
        pass

    def combine_values_slice(self, values_slice:ValuesSlice):

        pass




