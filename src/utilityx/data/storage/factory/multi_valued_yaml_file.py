from typing import List, Any
from ruamel.yaml import YAML  # no CommentedMap

from utilityx.data.format.type.yaml.yaml import Yaml as YamlFormat
from utilityx.data.storage.decorator.multi_valued.uniformat import UniFormat
from utilityx.data.storage.decorator.multi_valued.multi_value import MultiValue
from utilityx.data.storage.type.file.file import File
from utilityx.os.path import Path
from utilityx.data.type.sliced_values.values_slice import VeluesSlice
from utilityx.data.storage.decorator.multi_valued.interface import Interface as MultiValueInterface

class MultiValuedYamlFile(MultiValueInterface):
    def __init__(self, file_storage: File):
        self._storage = UniFormat(MultiValue(file_storage, "---"), YamlFormat)
        self._yaml = YAML(typ="safe")  # plain Python types
        self._yaml.explicit_start = True

    def load(self) -> None:
        """Load all YAML documents into memory and cache them."""
        with open(self.__get_path(), "r") as stream:
            ram_units: List[dict[str, Any]] = [doc for doc in self._yaml.load_all(stream) if doc is not None]
        self._storage.set_ram_units(ram_units)

    def save(self) -> None:
        """Persist the cached documents back to disk as a sliced_values-doc YAML."""
        with open(self.__get_path(), "w") as stream:
            self._yaml.dump_all(self._storage.get_ram_values(), stream)

    def __load_slice(self, slc: slice) -> None:
        """Stream only the requested window from disk and cache it as a slice. Returns nothing."""
        if self._storage.get_ram_values_slices().slice_exists(slc):
            return

        multi_yaml_docs_list: List[dict[str, Any]] = []
        with open(self.__get_path(), "r") as stream:
            for index, single_yaml_doc in enumerate(self._yaml.load_all(stream)):
                if single_yaml_doc is None:
                    continue
                if index < slc.start:
                    continue
                if slc.stop is not None and index >= slc.stop:
                    break
                if (index - slc.start) % slc.step == 0:
                    multi_yaml_docs_list.append(single_yaml_doc)
        self._storage.add_to_ram_values_slices(VeluesSlice(multi_yaml_docs_list, slc))

    # @overrides  # keep if your project uses it; otherwise remove
    def get_values_by_slice(self, slc: slice) -> List[dict[str, Any]]:
        if self._storage.get_ram_values_slices().slice_exists(slc):
            return self.storage.get_ram_values_by_slice(slc)
        self.__load_slice(slc)
        return self._storage.get_ram_values_from_values_slices_by_slice(slc)

    def __get_path(self) -> str:
        return self._storage.get_native_absolute_path()


if __name__ == "__main__":
    file_path = "/home/donkarlo/Dropbox/projs/research/data/self-aware-drones/ctumrs/two-drones/normal-scenario/uav1-gps-lidar-uav2-gps-lidar.yaml"
    file_storage = File(Path(file_path))
    mvf = MultiValuedYamlFile(file_storage)
    slc = slice(0, 40000, 1)
    values = mvf.get_values_by_slice(slc)
    print(values)
