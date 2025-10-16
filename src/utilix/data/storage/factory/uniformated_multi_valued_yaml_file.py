from typing import List, Any
from typing import override


# --- Fast YAML path: try C extensions, fall back to safe Python loaders ---
import yaml

try:
    from yaml import CLoader as YamlCLoader, CDumper as YamlCDumper  # fastest
except Exception:
    from yaml import SafeLoader as YamlCLoader, SafeDumper as YamlCDumper  # fallback

from utilix.data.storage.type.file.format.type.yaml.yaml import Yaml as YamlFormat
from utilix.data.storage.decorator.multi_valued.uniformated import UniFormated
from utilix.data.storage.decorator.multi_valued.multi_valued import MultiValued
from utilix.data.storage.type.file.file import File
from utilix.os.path import Path
from utilix.data.type.sliced_value.values_slice import ValuesSlice
from utilix.data.storage.decorator.multi_valued.interface import Interface as MultiValueInterface
from itertools import islice
import io


class UniformatedMultiValuedYamlFile(MultiValueInterface):
    """
    High-throughput multi-document YAML file using PyYAML (+CLoader/CDumper if available).
    - load(): loads all docs into RAM
    - save(): dumps RAM docs back to disk (with '---' separators)
    - get_values_by_slice(): streams only the requested doc window
    Notes:
      * PyYAML does not preserve comments/order like ruamel.yaml's round-trip mode.
      * Uses explicit_start='---' for multi-doc formatting.
    """

    def __init__(self, str_path):
        # Keep your existing UniFormat/MultiValued stack and the '---' separator
        self._storage = UniFormated(MultiValued(File(Path(str_path)), "---"), YamlFormat)

    @override
    def load(self) -> None:
        """Load all YAML documents into memory and cache them."""
        with open(self.__get_path(), "r", encoding="utf-8") as stream:
            ram_units: List[dict[str, Any]] = [
                doc for doc in yaml.load_all(stream, Loader=YamlCLoader) if doc is not None
            ]
        self._storage.set_ram_units(ram_units)

    @override
    def save(self) -> None:
        """Persist the cached documents back to disk as a sliced_value-doc YAML."""
        values = self._storage.get_ram_values()
        # Ensure explicit_start to emit '---' before each document for multi-doc files
        with open(self.__get_path(), "w", encoding="utf-8") as stream:
            yaml.dump_all(
                values,
                stream,
                Dumper=YamlCDumper,
                explicit_start=True,
                allow_unicode=True,
                default_flow_style=False,
                sort_keys=False,  # keep user insertion order where possible
            )

    def load_slice(self, slc: slice) -> None:
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
        with open(self.__get_path(), "rb", buffering=1024 * 1024) as f_raw:
            stream = io.BufferedReader(f_raw, buffer_size=8 * 1024 * 1024)
            docs = yaml.load_all(stream, Loader=YamlCLoader)
            for dict_doc in islice(docs, start, stop, step):
                if dict_doc is not None:
                    selected_docs.append(dict_doc)

        self._storage.add_to_ram_values_slices(ValuesSlice(selected_docs, slc))

    @override  # keep if your project uses it; otherwise remove
    def get_values_by_slice(self, slc: slice) -> List[dict[str, Any]]:
        """Return a slice view; stream from disk if not cached."""
        if self._storage.get_ram_values_slices().slice_exists(slc):
            return self._storage.get_ram_values_from_values_slices_by_slice(slc)
        self.load_slice(slc)
        return self._storage.get_ram_values_from_values_slices_by_slice(slc)

    def __get_path(self) -> str:
        return self._storage.get_native_absolute_path()

    # Unimplemented interface methods (fill as needed)
    @override
    def earase_storage(self) -> None:
        pass

    @override
    def delete_storage(self) -> None:
        pass

    @override
    def earase_ram(self) -> None:
        pass

    @override
    def set_ram(self, ram: Any) -> None:
        pass
