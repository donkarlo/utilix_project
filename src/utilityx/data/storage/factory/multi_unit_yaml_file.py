from typing import Iterator

from utilityx.data.storage.decorator.multi_unit import MultiUnit
from utilityx.data.storage.decorator.single_data_format import SingleDataFormat
from utilityx.data.storage.type.file import File
from utilityx.os.path import Path
from ruamel.yaml import YAML, CommentedMap


class MultiUnitYamlFile:


    def __init__(self, file_path):
        file_storage = File(Path(file_path))
        self._storage_plan = SingleDataFormat(MultiUnit(file_storage))

        self._yaml = YAML()
        self._yaml.explicit_start = True

    def fetch_next_with_counter(self) -> Iterator[tuple[int, CommentedMap]]:
        with open(self.__file.get_native_absolute_path(), "r") as stream:
            for counter, doc in enumerate(self.__yaml.load_all(stream)):
                yield (counter, doc)

