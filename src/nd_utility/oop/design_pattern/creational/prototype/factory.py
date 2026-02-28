from copy import deepcopy
from typing import Generic, TypeVar
T = TypeVar("T")

class Factory(Generic[T]):
    def __init__(self, sample_object:T):
        self._sample_object = sample_object

    def get_clone(self) -> T:
        return deepcopy(self._sample_object)