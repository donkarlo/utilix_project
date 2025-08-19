from abc import ABC, abstractmethod


class Interface(ABC):
    """
        This class is an interface. Dont add anything other than abstract methods. if you need to add concrete properties and
        """

    @abstractmethod
    def load(self) -> None:
        """
        Loadsfrom storage to RAM
        Returns:

        """
        pass

    @abstractmethod
    def save(self)->None:
        """saves what is inside ram into the storage"""
        pass

    @abstractmethod
    def earase_storage(self)->None:
        """
        earase the value of the storage and not the storage i.e. not the file or DB etc
        Returns:

        """
        pass

    @abstractmethod
    def earase_ram(self) -> None:
        pass

    @abstractmethod
    def set_ram(self)->None:
        pass

    @abstractmethod
    def add_to_ram(self)->None:
        pass


