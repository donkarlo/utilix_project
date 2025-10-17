import yaml
from utilix.data.type.type import Type as DataType
from utilix.data.type.dic.dic import Dic as BasicDict


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

