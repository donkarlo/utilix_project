from utilix.data.storage.factory.uniformated_multi_valued_yaml_file import UniformatedMultiValuedYamlFile
from utilix.os.path.path import Path


class TestUniformatedMultiValuedYamlFile:
    def test_get_values_by_slice(self) -> None:
        file_path = "test_uniformted_multi_yaml_file.yaml"
        path = Path(file_path)
        mvf = UniformatedMultiValuedYamlFile(path)
        slc = slice(2, 5, 1)
        yaml_docs = mvf.get_values_by_slice(slc)
        assert len(yaml_docs) == 3