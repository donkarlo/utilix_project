from abc import abstractmethod

from utilityx.data.storage.access import Access


class Storage:
    """
    Only discess the where the source is and how to unlock it
    """
    def __init__(self, access:Access):
        self._access = access

        # from source to python variable
        self._cache = None

    @abstractmethod
    def load_to_cache(self) -> str:
        pass

    @abstractmethod
    def save_cache(self) -> bool:
        pass

    def get_type(self) -> SupportingType:
        return self._storage

    def get_format(self) -> SupportingFormat:
        return self._format

    def get_access(self) -> Access:
        return self._access

    def add_to_cache(self, additional_cache_content: str) -> bool:
        """
        Adds at the end of content only
        Args:
            additional_cache_content:

        Returns:

        """
        self._cache += additional_cache_content