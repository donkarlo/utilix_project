from nd_utility.data.storage.decorator.single_valued import SingleValued
from nd_utility.data.storage.type.file.file import File
from nd_utility.data.kind.dic.dic import Dic as BasicDict
from nd_utility.os.file_system.path.path import Path
from nd_utility.data.kind.yaml import Yaml as YamlType


class TestSingleValuedYamlFile:
    def setup_method(self) -> None:
        self._yaml_path:Path = Path("single_value.yaml")

    def test_load(self) -> None:
        dic_to_check_uniqueness = SingleValued(File(self._yaml_path), YamlType()).get_special_ram_object()
        assert dic_to_check_uniqueness is not None
        assert isinstance(dic_to_check_uniqueness, BasicDict)