from utilix.data.kind.indexed_value.index_value import IndexValue


class Group:
    def __init__(self, indexes_values:List[IndexValue]):
        """
        Use to combine values slices, values sluces is a form of this class
        Args:
            indexes_values:
        """
        self._indexes_values = indexes_values
    def get_indexes_values(self)->List[IndexValue]:
        return self._indexes_values