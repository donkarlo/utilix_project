from abc import abstractmethod, ABC

from utilityx.data.storage.access import Access


class Storage(ABC):
    """
    An storage is for saving active_memory in a storage such as file and load it into active_memory
    cache can be regarded as active memory. The RAM
    - it is still abstract because we will work with file , DB etc

    """
    def __init__(self, access:Access):
        self._access = access


        # from source to python variable
        self._ram_memory:str = None

    def set_ram_memory(self, content:str):
        self._ram_memory = content

    def save_ram_memory_to_storage(self, clean_ram_memory:bool):
        self._do_save_ram_memory_to_storage()
        if clean_ram_memory == True:
            self._ram_memory = None