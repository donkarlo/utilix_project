from utilix.data.kind.tabular.decorator.decorator import Decorator
from utilix.data.kind.tabular.interface import Interface


class Columned(Decorator):
    def __init__(self, inner: Interface, column_names:List[str]):
        Decorator.__init__(self, inner)
        self._column_names = column_names

    def get_column_names(self):
        return self._column_names
