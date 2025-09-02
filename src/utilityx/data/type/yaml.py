from typing import Any
import yaml
from utilityx.data.type.type import Type as DataType
from utilityx.data.type.key_value.dic.basic import Basic as BasicDict


class Yaml(DataType):
    """
    This is just to represent single yaml, for multiple a composite zis needed
    """

    def validate(self, value: str) -> bool:
        """

        Args:
            value:

        Returns:

        """
        try:
            yaml.safe_load(value)
            return True
        except yaml.YAMLError:
            return False


    def get_special_object(self, value: str) -> BasicDict:
        return BasicDict(yaml.safe_load(value))

