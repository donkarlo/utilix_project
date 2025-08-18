from abc import ABC, abstractmethod


class Interface(ABC):
    """
        This class is an interface. Dont add anything other than abstract methods. if you need to add concrete properties and
        """

    @abstractmethod
    def load(self) -> str:
        """
        Loadsfrom storage to RAM
        Returns:

        """
        pass

    @abstractmethod
    def save(self)->bool:
        """saves what is inside ram into the storage"""
        pass

    @abstractmethod
    def earase(self)->bool:
        """
        earase the value of the storage and not the storage i.e. not the file or DB etc
        Returns:

        """
        pass
