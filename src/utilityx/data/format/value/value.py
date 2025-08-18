class Value(ABC):
    """All values must be either a subclass of this or raw string"""
    def __init__(self):
        self._keys_values:dict= None
        self._string_value = None

    @abstractmethod
    def __str__(self) -> str:
        """Return a string representation of the object."""
        pass

    def get_keys_values(self)->dict:
        return self._keys_values