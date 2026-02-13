from typing import Any

from nd_utility.data.kind.stack.layer.interface import Interface


class Layer(Interface):
    def __init__(self, data:Any):
        self._data = data

    def get_data(self)->Any:
        return self._data