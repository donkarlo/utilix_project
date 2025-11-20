from typing import Any

from utilix.data.kind.stack.layer.interface import Interface


class Layer(Interface):
    def __init__(self, data:Any):
        self._data = data

    def get_data(self)->Any:
        return self._data