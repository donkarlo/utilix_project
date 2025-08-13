from typing import Iterator

from utilityx.data.type.supporting_format import SupportingFormat
from utilityx.data.source.interface import SourceDecorator
from utilityx.data.storage.file import File
from utilityx.data.storage.supporting_storage import SupportingStorage
from utilityx.data.storage.decorator import Decorator

from utilityx.data.source import Source
from utilityx.data.storage.decorator import Partial

from utilityx.data.storage.decorator import United
from utilityx.os.path import Path
from ruamel.yaml import YAML, CommentedMap


class MultiDocYamlFile:


    def __init__(self, inner:Source):
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