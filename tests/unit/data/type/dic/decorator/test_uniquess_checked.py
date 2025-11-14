from utilix.data.storage.decorator.single_valued import SingleValued
from utilix.data.storage.type.file.file import File
from utilix.data.type.dic.decorator.uniqueness_checked import UniquenessChecked
from utilix.data.type.dic.dic import Dic as BasicDic
from utilix.data.type.yaml import Yaml as BasicYaml
from utilix.os.file_system.path.path import Path
import yaml


class TestUniquenessChecked:
    def test_valid_unique_leaves(self)->None:
        valid_unique_leaves_test_str_path = "valid_inque_leaves_test.yaml"
        dic_to_check_uniqueness = yaml.safe_load(SingleValued(File(Path(valid_unique_leaves_test_str_path)), BasicYaml).get_ram())
        unique_checker = UniquenessChecked(BasicDic(dic_to_check_uniqueness))
        #make sure it is valid
        assert unique_checker.validate_unique_items_in_lists()[0] == True

    def test_invalid_unique_leaves(self)->None:
        invalid_unique_leaves_test_str_path = "invalid_inque_leaves_test.yaml"
        dic_to_check_uniqueness = yaml.safe_load(SingleValued(File(Path(invalid_unique_leaves_test_str_path)), BasicYaml).get_ram())
        unique_checker = UniquenessChecked(BasicDic(dic_to_check_uniqueness))
        #make sure it is not valid
        print(unique_checker.validate_unique_items_in_lists())
        assert unique_checker.validate_unique_items_in_lists()[0] == False

