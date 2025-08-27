from typing import List, Any

# --- Fast YAML path: try C extensions, fall back to safe Python loaders ---
import yaml

try:
    from yaml import CLoader as YamlLoader, CDumper as YamlDumper  # fastest
except Exception:
    from yaml import SafeLoader as YamlLoader, SafeDumper as YamlDumper  # fallback

from utilityx.data.format.type.yaml.yaml import Yaml as YamlFormat
from utilityx.data.storage.decorator.multi_valued.uniformat import UniFormat
from utilityx.data.storage.decorator.multi_valued.multi_value import MultiValue
from utilityx.data.storage.type.file.file import File
from utilityx.os.path import Path
from utilityx.data.type.sliced_values.values_slice import VeluesSlice
from utilityx.data.storage.decorator.multi_valued.interface import Interface as MultiValueInterface


class MultiValuedYamlFile(MultiValueInterface):
    """
    High-throughput multi-document YAML file using PyYAML (+CLoader/CDumper if available).
    - load(): loads all docs into RAM
    - save(): dumps RAM docs back to disk (with '---' separators)
    - get_values_by_slice(): streams only the requested doc window
    Notes:
      * PyYAML does not preserve comments/order like ruamel.yaml's round-trip mode.
      * Uses explicit_start='---' for multi-doc formatting.
    """

    def __init__(self, file_path: str):
        file_storage = File(Path(file_path))
        # Keep your existing UniFormat/MultiValue stack and the '---' separator
        self._storage = UniFormat(MultiValue(file_storage, "---"), YamlFormat)

    def load(self) -> None:
        """Load all YAML documents into memory and cache them."""
        with open(self.__get_path(), "r", encoding="utf-8") as stream:
            ram_units: List[dict[str, Any]] = [
                doc for doc in yaml.load_all(stream, Loader=YamlLoader) if doc is not None
            ]
        self._storage.set_ram_units(ram_units)

    def save(self) -> None:
        """Persist the cached documents back to disk as a sliced_values-doc YAML."""
        values = self._storage.get_ram_values()
        # Ensure explicit_start to emit '---' before each document for multi-doc files
        with open(self.__get_path(), "w", encoding="utf-8") as stream:
            yaml.dump_all(
                values,
                stream,
                Dumper=YamlDumper,
                explicit_start=True,
                allow_unicode=True,
                default_flow_style=False,
                sort_keys=False,  # keep user insertion order where possible
            )

    def __load_slice(self, slc: slice) -> None:
        """
        Stream only the requested window from disk and cache it as a slice.
        Reads sequentially and stops as soon as the window is complete.
        """
        if self._storage.get_ram_values_slices().slice_exists(slc):
            return

        start = 0 if slc.start is None else slc.start
        stop = slc.stop  # may be None
        step = 1 if slc.step is None else slc.step

        selected_docs: List[dict[str, Any]] = []
        with open(self.__get_path(), "r", encoding="utf-8") as stream:
            for index, single_yaml_doc in enumerate(yaml.load_all(stream, Loader=YamlLoader)):
                if single_yaml_doc is None:
                    continue
                if index < start:
                    continue
                if stop is not None and index >= stop:
                    break
                if (index - start) % step == 0:
                    selected_docs.append(single_yaml_doc)

        self._storage.add_to_ram_values_slices(VeluesSlice(selected_docs, slc))

    # @overrides  # keep if your project uses it; otherwise remove
    def get_values_by_slice(self, slc: slice) -> List[dict[str, Any]]:
        """Return a slice view; stream from disk if not cached."""
        if self._storage.get_ram_values_slices().slice_exists(slc):
            return self._storage.get_ram_values_from_values_slices_by_slice(slc)
        self.__load_slice(slc)
        return self._storage.get_ram_values_from_values_slices_by_slice(slc)

    def __get_path(self) -> str:
        return self._storage.get_native_absolute_path()

    # Unimplemented interface methods (fill as needed)
    def earase_storage(self) -> None:
        pass

    def delete_storage(self) -> None:
        pass

    def earase_ram(self) -> None:
        pass

    def set_ram(self, ram: Any) -> None:
        pass


if __name__ == "__main__":
    file_path = "/home/donkarlo/Dropbox/projs/research/data/self-aware-drones/ctumrs/two-drones/normal-scenario/uav1-gps-lidar-uav2-gps-lidar.yaml"
    mvf = MultiValuedYamlFile(file_path)
    slc = slice(0, 40000, 1)
    values = mvf.get_values_by_slice(slc)
    print(len(values))
