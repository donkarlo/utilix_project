from utilix.data.kind.indexed_value.indexed_value import IndexedValue


class Group:
    def __init__(self, indexes_values:List[IndexedValue]):
        """
        Use to combine values slices, values sluces is a form of this class
        Args:
            indexes_values:
        """
        self._indexes_values = indexes_values
    def get_indexes_values(self)->List[IndexedValue]:
        return self._indexes_values