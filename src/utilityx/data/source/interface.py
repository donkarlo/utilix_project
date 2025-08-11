from abc import abstractmethod

from utilityx.data.format.supporting_format import SupportingFormat
from utilityx.data.storage.supporting_type import SupportingType


class interface(ABC):
    """
    This class is an interface. Dont add anything other than abstract methods. if you need to add concrete properties and
    """
    @abstractmethod
    def load_content(self)->str:
        """to set self._memory_content"""
        pass

    @abstractmethod
    def save_content(self)->bool:
        """
        saves self._memory_content
        No validity check will be performed here. Just the given string will be added
        Returns: success
        """
        pass



