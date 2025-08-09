from typing import Iterator

from utilityx.data.format.supporting_format import SupportingFormat
from utilityx.data.source.interface import SourceDecorator
from utilityx.data.storage.file import File
from utilityx.data.storage.supporting_storage import SupportingStorage
from utilityx.data.source.decorator import Decorator

from utilityx.data.source import Source
from utilityx.data.source.decorator.partial import Partial

from utilityx.data.source.decorator.united import United
from utilityx.os.filesys.os_path import OsPath
from ruamel.yaml import YAML, CommentedMap


class MultiDocYamlFile(Decorator):


    def __init__(self, inner:Source, file:File):
        super().__init__(inner)
        self._file = file
        self._yaml = YAML()
        self._yaml.explicit_start = True
        self._object = United(Partial(self))

    def fetch_next_with_counter(self) -> Iterator[tuple[int, CommentedMap]]:
        with open(self.__file.get_abs_os_path(), "r") as stream:
            for counter, doc in enumerate(self.__yaml.load_all(stream)):
                yield (counter, doc)

    def add_doc(self, doc:str)->bool:
        #@TODO: check if doc is a valid yaml sytring for an independent document
        pass

if __name__ == "__main__":
    file = File(OsPath("/home/donkarlo/Dropbox/projs/research/data/self-aware-drones/ctumrs/two-drones/normal-scenario/uav1-gps-lidar-uav2-gps-lidar.yaml"))
    path = MultiDocYamlFile(file)
    tpl = next(path.fetch_next_with_counter())

    source = Source()
    print(type(tpl[1]))