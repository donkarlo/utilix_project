from typing import List

from nd_utility.data.kind.stack.layer.layer import Layer


class Stack:
    def __init__(self, layers:List[Layer]):
        self._layers = layers

    def get_layers(self) -> List[Layer]:
        return self._layers