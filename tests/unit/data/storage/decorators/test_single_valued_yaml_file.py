from utilix.data.storage.decorator.single_valued import SingleValued
from utilix.data.storage.type.file.file import File
from utilix.data.type.dic.dic import Dic as BasicDict
from utilix.os.path import Path
from utilix.data.type.yaml import Yaml as YamlType


class TestSingleValuedYamlFile:
    def setup_method(self) -> None:
        self._yaml_path:Path = Path("single_value.yaml")

    def test_load(self) -> None:
        dic_to_check_uniqueness = SingleValued(File(self._yaml_path), YamlType()).get_special_ram_object()
        assert dic_to_check_uniqueness is not None
        assert isinstance(dic_to_check_uniqueness, BasicDict)