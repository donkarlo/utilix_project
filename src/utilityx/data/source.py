from utilityx.data.storage.access import Access
from utilityx.data.storage.supporting_type import SupportingType
from utilityx.data.storage.format import SupportingFormat
from utilityx.data.source.interface import Interface

class Source(Interface):
    def __init__(self, storage:SupportingType, format:SupportingFormat):
        self._storage = storage
        self._format = format

        # from source to python variable
        self._memory_content = None

    @abstractmethod
    def load_to_memory_content(self) -> str:
        pass

    def save_memory_content(self) -> bool:
        print("Saving:", self._memory_content)
        return True

    def get_type(self)->SupportingType:
        return self._storage

    def get_format(self)->SupportingFormat:
        return self._format

    def get_access(self)->Access:
        return self._access

    def add_to_memory_content(self, memory_content:str)->bool:
        """
        Adds at the end of content only
        Args:
            memory_content:

        Returns:

        """
        self._memory_content += memory_content

    def add_to_storage_content(self,):
        pass