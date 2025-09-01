from typing import Protocol


class Format(Protocol):
    """
    - format is specific to file, it is not a data type
    - it can not have storage save option. if saving is needed, it should be done through a storage object
    - It is to do the most general things about the format such as validation
    """
    def validate_value(self, value:str)->bool:
        ...