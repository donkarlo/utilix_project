from abc import abstractmethod, ABC


class Value(ABC):
    """
    All values must be either a subclass of this or raw string
    - For example CommentedMap from yaml is a raw_value
    """
    def __init__(self):
        self._keys_values:dict= None
        #everything must be message to a string
        self._string_value = None

    @abstractmethod
    def __str__(self) -> str:
        """Return a string representation of the object."""
        pass

    @abstractmethod
    def __eq__(self, other:Value)->bool:
        pass

    def get_keys_values(self)->dict:
        return self._keys_values