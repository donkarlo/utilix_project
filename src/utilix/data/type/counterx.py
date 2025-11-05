from typing import Union, Sequence
from collection import Counter

class Counterx:
    def __init__(self, raw_countable:Union[dict,Sequence]):
        self._raw_countable = raw_countable
    def get_counts(self):
        return Counter(self._raw_countable)