from typing import Dict
from utilityx.data.storage.type.file.format.format import Format
from utilityx.os.path import Path
import yaml


class Yaml(Format):
    def get_formatted_value(self, path:Path)->Dict:
        return yaml.load(path.get_native_absolute_path())



