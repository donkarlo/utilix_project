import time

from utilix.data.storage.factory.uniformated_multi_valued_yaml_file import UniformatedMultiValuedYamlFile
from utilix.os.file_system.path.path import Path


class TestUniformatedMultiValuedYamlFile:
    def test_get_values_by_slice_speed(self) -> None:
        start = time.monotonic()
        dir_path = "/home/donkarlo/Dropbox/projs/research/data/self-aware-drones/ctumrs/two-drones/normal-scenario/"
        file_path = dir_path+"/"+"uav1-gps-lidar-uav2-gps-lidar.yaml"
        path = Path(file_path)
        mvf = UniformatedMultiValuedYamlFile(path)
        slc = slice(2, 10000, 1)
        yaml_docs = mvf.get_values_by_slice(slc)
        elapsed = time.monotonic() - start
        assert elapsed < 20, f"Sequence took {elapsed:.2f}s which exceeds 20s"