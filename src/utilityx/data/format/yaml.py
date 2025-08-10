from ruamel.yaml import CommentedMap
from ruamel.yaml import YAML
from io import StringIO
from utilityx.data.format import Format
from utilityx.data.format.supporting_format import SupportingFormat


class Yaml(Format):
    def __init__(self, content:[CommentedMap]):
        content = self._get_str_content(content)
        super().__init__(SupportingFormat.YAML, content)

    def _get_str_content(self, content:CommentedMap)->str:
        yaml = YAML()
        yaml.explicit_start = True  # optional
        yaml.default_flow_style = False  # for multi-line readability
        stream = StringIO()
        yaml.dump(content, stream)
        content = stream.getvalue()
        return content

    def get_modeled(self, content:str):
        """
        Probably here we dont need a Model object because CommentedMap does already the job
        Args:
            content:

        Returns:

        """
        pass

