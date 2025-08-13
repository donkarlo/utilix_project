from abc import ABC, abstractmethod


class interface(ABC):
    """
    This class is an interface. Dont add anything other than abstract methods. if you need to add concrete properties and
    """

    @abstractmethod
    def load_to_ram_memory(self) -> str:
        pass

    @abstractmethod
    def _do_save_ram_memory_to_storage(self):
        pass