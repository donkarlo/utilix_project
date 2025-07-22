from ruamel.yaml import CommentedMap
from ruamel.yaml import YAML
from io import StringIO
from utilityx.data.format.format import Format
from utilityx.data.format.supporting_format import SupportingFormat


class Yaml(Format):
    def __init__(self, content:[CommentedMap]):
        content = self._get_str_content(content)
        super().__init__(SupportingFormat.YAML, content)

    def _get_str_content(self, content)->str:
        if isinstance(content, CommentedMap):
            yaml = YAML()
            yaml.explicit_start = True  # optional
            yaml.default_flow_style = False  # for multi-line readability
            stream = StringIO()
            yaml.dump(content, stream)
            content = stream.getvalue()
            return content