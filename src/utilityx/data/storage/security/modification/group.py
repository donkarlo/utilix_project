from typing import Iterable

from utilityx.data.storage.security.modification import Modification


class Group:
    def __init__(self, mods: set[Modification]):
        self._mods = mods  # trust the caller

    def add(self, mod: Modification) -> None:
        self._mods.add(mod)

    def remove(self, mod: Modification) -> None:
        self._mods.discard(mod)

    def has(self, mod: Modification) -> bool:
        return mod in self._mods

    def __repr__(self) -> str:
        return f"Group({', '.join(m.name for m in self._mods)})"