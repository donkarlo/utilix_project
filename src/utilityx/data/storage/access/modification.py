from typing import Iterable

from utilityx.data.storage.security.modification import ModificationSet


class Group:
    def __init__(self, mods: set[ModificationSet]):
        self._mods = mods  # trust the caller

    def add(self, mod: ModificationSet) -> None:
        self._mods.add(mod)

    def remove(self, mod: ModificationSet) -> None:
        self._mods.discard(mod)

    def has(self, mod: ModificationSet) -> bool:
        return mod in self._mods

    def __repr__(self) -> str:
        return f"Group({', '.join(m.name for m in self._mods)})"