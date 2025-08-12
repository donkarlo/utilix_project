from abc import ABC, abstractmethod


class interface(ABC):
    """
    This class is an interface. Dont add anything other than abstract methods. if you need to add concrete properties and
    """

    @abstractmethod
    def load_cache(self) -> str:
        """to set self._cache"""
        pass

    @abstractmethod
    def save_cache(self) -> bool:
        """
        saves self._cache
        No validity check will be performed here. Just the given string will be added
        Returns: success
        """
        pass
