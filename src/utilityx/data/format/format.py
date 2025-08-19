from abc import abstractmethod, ABC
from typing import Any


class Format(ABC):
    """
    - it can not have storage save option. if saving is needed, it should be done through a storage object
    - It is to do the most general things about the format such as validation
    """
    @abstractmethod
    def validate_value(self, value:Union[str])->bool:
        pass