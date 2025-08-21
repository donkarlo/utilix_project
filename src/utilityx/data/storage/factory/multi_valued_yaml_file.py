from typing import Optional, List
from ruamel.yaml import YAML, CommentedMap

from utilityx.data.format.type.yaml.yaml import Yaml as YamlFormat
from utilityx.data.storage.decorator.multi_valued.formatted import Formatted
from utilityx.data.storage.decorator.multi_valued.multi_valued import MultiValued
from utilityx.data.storage.type.file.file import File
from utilityx.os.path import Path


class MultiValuedYamlFile:
    def __init__(self, file_path: str):
        file_storage = File(Path(file_path))
        self._decorated_storage = Formatted(MultiValued(file_storage, "---"), YamlFormat)
        self._yaml = YAML()
        # affects dumping, harmless for loading
        self._yaml.explicit_start = True

    def load(self) -> List[CommentedMap]:
        """
        Load all YAML documents into memory and cache them.
        - Returns the cached muti on subsequent calls unless force_reload=True.
        """
        with open(self.__get_path(), "r") as stream:
            ram_units = [doc for doc in self._yaml.load_all(stream) if doc is not None]

        # Optionally enforce mapping type if you expect only mappings:
        for i, unit in enumerate(ram_units):
            if not isinstance(unit, CommentedMap):
                raise TypeError(f"Document {i} is not a mapping (got {type(unit).__name__}).")

        self._decorated_storage.set_ram_units(ram_units)

    def save(self) -> None:
        """Persist the cached documents back to disk as a multi-doc YAML."""
        nap = self.__get_path()
        # ruamel.yaml preserves comments/order in CommentedMap by default
        with open(nap, "w") as stream:
            self._yaml.dump_all(self._ram_units, stream)

    def get_ram_unit_at(self, at: int) -> Optional[CommentedMap]:
        """
        Return a single cached document by index (load cache if needed).
        """
        self._decorated_storage.get_ram_units(at)

    def add_ram_unit(self, unit: CommentedMap):
        """Append a new document to the in-memory cache and return its index."""
        self._decorated_storage.add_ram_units(unit)

    def load_slice(self, slc:slice) -> List[CommentedMap]:
        """
        Return a muti of documents selected by a Python slice.

        Rules:
          - If indices are non-negative and step > 0, stream only the requested window
            from disk without loading the whole file.
          - Otherwise (negative start/stop or negative/zero step), load all and slice in memory.

        Args:
            slc: A Python slice object (start, stop, step).

        Returns:
            List[CommentedMap]: Selected YAML documents.
        """
        if not isinstance(slc, slice):
            raise TypeError(f"load_slice expects a slice, got {type(slc).__name__}")

        s_start = 0 if slc.start is None else slc.start
        s_stop = slc.stop  # may be None
        s_step = 1 if slc.step is None else slc.step

        if s_step <= 0:
            raise ValueError("slice step must be > 0")

        out: List[CommentedMap] = []
        with open(self.__get_path(), "r") as stream:
            for index, doc in enumerate(self._yaml.load_all(stream)):
                if doc is None:
                    continue
                if index < s_start:
                    continue
                if s_stop is not None and index >= s_stop:
                    break
                if (index - s_start) % s_step == 0:
                    if not isinstance(doc, CommentedMap):
                        raise TypeError(
                            f"Document {index} is not a mapping (got {type(doc).__name__})."
                        )
                    out.append(doc)
        return out

    def __get_path(self):
        return self._decorated_storage.get_native_absolute_path()

if __name__ == "__main__":
    file_path = "/home/donkarlo/Dropbox/projs/research/data/self-aware-drones/ctumrs/two-drones/normal-scenario/uav1-gps-lidar-uav2-gps-lidar-1001-lines.yaml"
    multi_valued_yaml_file = MultiValuedYamlFile(file_path)
