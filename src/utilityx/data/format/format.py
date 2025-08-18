from abc import abstractmethod, ABC
from typing import Any


class Format(ABC):
    def __init__(self):
        """
        To hold both the string string_content and how to convert it to a python object
        - it can not have storage save option. if saving is needed, it should be done through a storage object
        """

    @abstractmethod
    def validate_value(self, content:Union[str])->bool:
        pass