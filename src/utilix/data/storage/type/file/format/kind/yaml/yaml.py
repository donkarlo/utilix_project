from typing import Dict
from utilix.data.storage.type.file.format.format import Format
from utilix.os.path.path import Path
import yaml


class Yaml(Format):
    def get_formatted_value(self, path:Path)->Dict:
        return yaml.load(path.get_native_absolute_path())



