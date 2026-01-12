from abc import ABC, abstractmethod
from typing import Any

from utilix.data.kind.core.kinds import Kinds


class Kind(ABC):
    def __init__(self, kinds_item:Kinds):
        self._kinds_item = kinds_item

    @abstractmethod
    def is_of_my_kind(self, value:Any)->bool: ...