from utilityx.data.storage.decorator.single_valued import SingleValued
from utilityx.data.storage.type.file.file import File
from utilityx.data.type.key_value.dic.decorator.uniqueness_checked import UniquenessChecked
from utilityx.data.type.key_value.dic.basic import Basic as BasicDic
from utilityx.data.type.yaml.basic import Basic as BasicYaml
from utilityx.os.path import Path


class TestUniquenessChecked:
    def test_valid_unique_leaves(self):
        valid_inque_leaves_test_str_path = "valid_inque_leaves_test.yaml"
        dic_to_check_uniqueness = SingleValued(File(Path(valid_inque_leaves_test_str_path)), BasicYaml).get_ram()
        unique_checker = UniquenessChecked(BasicDic(dic_to_check_uniqueness))
        #make sure it is valid
        assert unique_checker.validate_unique_items_in_lists()

    def test_invalid_unique_leaves(self):
        invalid_inque_leaves_test_str_path = "invalid_inque_leaves_test.yaml"
        dic_to_check_uniqueness = SingleValued(File(Path(invalid_inque_leaves_test_str_path)), BasicYaml).get_ram()
        unique_checker = UniquenessChecked(BasicDic(dic_to_check_uniqueness))
        #make sure it is not valid
        assert not unique_checker.validate_unique_items_in_lists()



