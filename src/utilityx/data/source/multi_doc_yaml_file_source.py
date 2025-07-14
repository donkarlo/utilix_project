from utilityx.data.format.supporting_format import SupportingFormat
from utilityx.data.source.source import Source
from utilityx.data.type.file import File
from utilityx.data.type.supporting_type import SupportingType
from utilityx.osx.filesys.os_path import OsPath
from ruamel.yaml import YAML

class MultiDocYamlFile(Source):
    def __init__(self, os_path: OsPath):
        self.__file = File(os_path)
        self.__yaml = YAML()
        self.__yaml.explicit_start = True
        super().__init__(SupportingType.FILE, SupportingFormat.YAML, None)

    def fetch_one_with_counter(self) -> tuple[int, dict]:
        with open(self.__file.get_abs_os_path(), "r") as stream:
            for counter, doc in enumerate(self.__yaml.load_all(stream)):
                yield (counter, doc)
