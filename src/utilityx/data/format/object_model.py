from abc import ABC


class ObjectModel(ABC):
    """The base yaml to convert string memory_content of the format to a structure"""
    @abstractmethod
