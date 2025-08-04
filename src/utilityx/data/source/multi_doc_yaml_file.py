from typing import Iterator

from utilityx.data.format.supporting_format import SupportingFormat
from utilityx.data.source import Source
from utilityx.data.type.file import File
from utilityx.data.type.supporting_type import SupportingType
from utilityx.osx.filesys.os_path import OsPath
from ruamel.yaml import YAML, CommentedMap


class MultiDocYamlFile(United):
    def __init__(self, os_path: OsPath):
        self.__file = File(os_path)
        self.__yaml = YAML()
        self.__yaml.explicit_start = True
        super().__init__(SupportingType.FILE, SupportingFormat.YAML, None)

    def fetch_next_with_counter(self) -> Iterator[tuple[int, CommentedMap]]:
        with open(self.__file.get_abs_os_path(), "r") as stream:
            for counter, doc in enumerate(self.__yaml.load_all(stream)):
                yield (counter, doc)

    def add_doc(self, doc:str)->bool:
        #@TODO: check if doc is a valid yaml sytring for an independent document
        pass


if __name__ == "__main__":
    c = MultiDocYamlFile(OsPath("/home/donkarlo/Dropbox/projs/research/data/self-aware-drones/ctumrs/two-drones/normal-scenario/uav1-gps-lidar-uav2-gps-lidar.yaml"))
    tpl = next(c.fetch_next_with_counter())
    print(type(tpl[1]))