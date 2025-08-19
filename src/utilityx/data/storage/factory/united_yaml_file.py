from typing import Iterator, Tuple, Optional, List
from ruamel.yaml import YAML, CommentedMap

from utilityx.data.format.type.yaml.yaml import Yaml as YamlFormat
from utilityx.data.storage.decorator.multi_unit.formatted import Formatted
from utilityx.data.storage.decorator.multi_unit.multi_united import MultiUnited
from utilityx.data.storage.type.file import File
from utilityx.os.path import Path


class MultiUnitedYamlFile:
    def __init__(self, file_path: str):
        file_storage = File(Path(file_path))
        self._decorated_storage = Formatted(MultiUnited(file_storage, "---"), YamlFormat)
        self._yaml = YAML()
        # affects dumping, harmless for loading
        self._yaml.explicit_start = True

    def load(self) -> List[CommentedMap]:
        """
        Load all YAML documents into memory and cache them.
        - Returns the cached list on subsequent calls unless force_reload=True.
        """
        nap = self.__get_path()
        with open(nap, "r") as stream:
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



    def load_slice(
            self,
            slc: Optional[slice] = None,
            *, # from here only named arguments are accepted
            start: Optional[int] = None,
            stop: Optional[int] = None,
            step: Optional[int] = None,
            force_reload: bool = False,
    ) -> List[CommentedMap]:
        """
        Return a list of documents selected by a Python slice or by (start, stop, step).
        - If indices are non-negative and step>0, stream only the requested window.
        - Otherwise (negative start/stop or negative step), load all then slice in memory.
        - either give it a slice or the start end step
        Args:
            slc:
            start:
            stop:
            step:
            force_reload:

        Returns:

        """

        # Normalize slice input
        if slc is None:
            slc = slice(start, stop, step)
        s_start = 0 if slc.start is None else slc.start
        s_stop = slc.stop  # may be None
        s_step = 1 if slc.step is None else slc.step

        # Decide whether we can stream efficiently
        streaming_ok = (
                (s_start is None or s_start >= 0) and
                (s_stop is None or s_stop >= 0) and
                (s_step is None or s_step > 0)
        )

        if not streaming_ok:
            # Fallback: load all, then slice using Python semantics
            docs = self.load_all(force_reload=force_reload)
            return docs[slc]

        # Stream the requested window without loading the whole file
        out: List[CommentedMap] = []
        cur = 0
        with open(self.__get_path(), "r") as stream:
            for index, doc in enumerate(self._yaml.load_all(stream)):
                if doc is None:
                    continue
                # Skip until start
                if index < s_start:
                    continue
                # Stop when reaching stop
                if s_stop is not None and index >= s_stop:
                    break
                # Respect step
                if (index - s_start) % s_step == 0:
                    out.append(doc)
        return out

    def __get_path(self):
        return self._decorated_storage.get_native_absolute_path()
