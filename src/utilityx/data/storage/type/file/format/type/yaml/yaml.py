from ruamel.yaml import YAML
from ruamel.yaml.parser import ParserError
from ruamel.yaml.scanner import ScannerError
from ruamel.yaml.constructor import ConstructorError
from utilityx.data.storage.type.file.format.format import Format


class Yaml(Format):
    """
    This is just to represent single yaml, for multiple a composite zis needed
    """

    def validate(self, value:str)->bool:
        """
        
        Args:
            value: 

        Returns:

        """
        yaml = YAML(typ="safe")
        yaml.allow_duplicate_keys = False
        try:
            docs = list(yaml.load_all(value))
        except (ParserError, ScannerError, ConstructorError):
            return False
        return (
                len(docs) == 1 and
                isinstance(docs[0], (dict, list)) and  # only mappings or sequences
                bool(docs[0])  # not empty
        )

