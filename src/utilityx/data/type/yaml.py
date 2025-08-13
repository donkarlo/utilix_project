from ruamel.yaml import CommentedMap
from ruamel.yaml import YAML
from ruamel.yaml.parser import ParserError
from ruamel.yaml.scanner import ScannerError
from ruamel.yaml.constructor import ConstructorError
from io import StringIO
from utilityx.data.type import Type
from utilityx.data.type.supporting_format import SupportingFormat


class Yaml(Type):
    """
    This is just to represent single yaml, for multiple a composite zis needed
    """

    def set_string_content_from_commented_map(self, content:CommentedMap)->str:
        yaml = YAML()
        yaml.explicit_start = True  # optional
        yaml.default_flow_style = False  # for multi-line readability
        stream = StringIO()
        yaml.dump(content, stream)
        self._content = stream.getvalue()

    def validate(self, string_content:str)->bool:
        yaml = YAML(typ="safe")
        yaml.allow_duplicate_keys = False
        try:
            docs = list(yaml.load_all(string_content))
        except (ParserError, ScannerError, ConstructorError):
            return False
        return (
                len(docs) == 1 and
                isinstance(docs[0], (dict, list)) and  # only mappings or sequences
                bool(docs[0])  # not empty
        )

