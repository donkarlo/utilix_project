from typing import List, Any
from typing import override


# --- Fast YAML str_path: try C extensions, fall back to safe Python loaders ---
import yaml

from utilix.data.kind.yaml.yaml import Yaml
from utilix.data.storage.decorator.multi_valued.observer.add_to_ram_values_publisher import AddToRamValuesPublisher
from utilix.data.storage.decorator.multi_valued.observer.add_to_ram_values_subscriber import AddToRamValuesSubscriber
from utilix.data.storage.decorator.multi_valued.observer.group_ram_values_addition_finished_publisher import \
    GroupRamValuesAdditionFinishedPublisher
from utilix.data.storage.decorator.multi_valued.observer.group_ram_values_addition_finished_subscriber import \
    GroupRamValuesAdditionFinishedSubscriber
from utilix.oop.inheritance.overriding.override_from import override_from

try:
    from yaml import CLoader as YamlCLoader, CDumper as YamlCDumper  # fastest
except Exception:
    from yaml import SafeLoader as YamlCLoader, SafeDumper as YamlCDumper  # fallback

from utilix.data.storage.decorator.multi_valued.uni_kinded import UniKinded
from utilix.data.storage.decorator.multi_valued.multi_valued import MultiValued
from utilix.data.storage.kind.file.file import File as FileStorage
from utilix.data.kind.sliced_value.values_slice import ValuesSlice
from utilix.data.storage.decorator.multi_valued.interface import Interface as MultiValueInterface
from itertools import islice
import io
from utilix.data.kind.dic.dic import Dic
from utilix.os.file_system.file.file import File as OsFile
from utilix.os.file_system.path.file import File as FilePath

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

    def __init__(self, str_path, create_if_not_exist:bool):
        # Keep your existing UniFormat/MultiValued decorator and the '---' separator
        yaml_data_kind = Yaml()
        file_storage = FileStorage(OsFile.init_from_path(FilePath(str_path)), create_if_not_exist)
        self._storage = UniKinded(MultiValued(file_storage, "---"), yaml_data_kind, False)

    @override_from(AddToRamValuesPublisher)
    def attach_add_to_ram_values_subscriber(self, add_value_subscriber: AddToRamValuesSubscriber) ->None:
        self._storage.attach_add_to_ram_values_subscriber(add_value_subscriber)

    @override_from(AddToRamValuesPublisher)
    def dettach_add_to_ram_values_subscriber(self, add_value_subscriber: AddToRamValuesSubscriber) ->None:
        self._storage.dettach_add_to_ram_values_subscriber(add_value_subscriber)

    @override_from(GroupRamValuesAdditionFinishedPublisher)
    def attach_group_ram_values_addition_finished_subscriber(self, add_values_finished_subscriber: GroupRamValuesAdditionFinishedSubscriber)->None:
        self._storage.attach_group_ram_values_addition_finished_subscriber(add_values_finished_subscriber)

    @override
    def load(self) -> None:
        """
        Load all YAML documents into memory and cache them.
        """
        with open(self.get_native_absolute_string_path(), "r", encoding="utf-8") as stream:
            ram_units: List[dict[str, Any]] = [
                doc for doc in yaml.load_all(stream, Loader=YamlCLoader) if doc is not None
            ]
        self._storage.set_ram_units(ram_units)

    @override
    def save(self) -> None:
        """Persist the cached documents back to disk as a sliced_value-doc YAML."""
        values = self._storage.get_ram_values()
        # Ensure explicit_start to emit '---' before each document for multi-doc files
        with open(self.get_native_absolute_string_path(), "w", encoding="utf-8") as stream:
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

        if slc is None:
            start = 0
            stop = None
            step = 1

        if slc.start is None:
            start = 0
        else:
            start = slc.start

        # if stop is None then until the end is loded
        stop = slc.stop

        if slc.step is None:
            step = 1
        else:
            step = slc.step

        selected_docs: List[dict[str, Any]] = []
        with open(self.get_native_absolute_string_path(), "rb", buffering=1024 * 1024) as f_raw:
            stream = io.BufferedReader(f_raw, buffer_size=8 * 1024 * 1024)
            dict_docs = yaml.load_all(stream, Loader=YamlCLoader)
            for dict_doc in islice(dict_docs, start, stop, step):
                if dict_doc is not None:
                    dic_doc = Dic(dict_doc)
                    selected_docs.append(dic_doc)

        self._storage.add_to_ram_values_slices(ValuesSlice(selected_docs, slc))

    @override
    def get_values_by_slice(self, slc: slice) -> List[dict[str, Any]]:
        """Return a slice view; stream from disk if not cached."""
        if self._storage.get_ram_values_slices().slice_exists(slc):
            return self._storage.get_ram_values_from_values_slices_by_slice(slc)
        self.load_slice(slc)
        return self._storage.get_ram_values_from_values_slices_by_slice(slc)

    def get_native_absolute_string_path(self) -> str:
        return self._storage.get_native_absolute_string_path()

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
