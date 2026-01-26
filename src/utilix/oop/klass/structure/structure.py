from abc import ABC, abstractmethod
from typing import List


class Structure(ABC):
    """
    Utility to generate a stable unique name for a class
    based on its module, qualname and __init__ signature
    (including type hints).
    """

    def __init__(self, klass:type, include_structures:List[type], exclude_structures:List[type]):
        """

        Args:
            klass:
            exclude_structures: for example explude [utilix.group.storage, ...]
        """
        self._klass = klass

    def get_klass(self)->type:
        return self._klass

    def get_inheritence_structure(self)->"Structure":
        pass

    def get_attribute_inheritence_structure(self)->"Structure":
        pass

    def get_inheritence_and_decorated_and_composited_structure(self)->"Structure":
        pass





