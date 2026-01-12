from utilix.data.storage.decorator.protected.modificationed.role.core.kinds import Kinds


class Kind:
    def __init__(self, role_set: set[Kinds]):
        """
        The minimum Permitted rule is read. other than that permission is not necessary
        Args:
            role_set:
        """
        self._role_set = role_set  # trust the caller

    def add(self, role: Kinds) -> None:
        self._role_set.add(role)

    def remove(self, role: Kinds) -> None:
        self._role_set.discard(role)

    def has(self, role: Kinds) -> bool:
        return role in self._role_set

    def __str__(self) -> str:
        return f"Group({', '.join(m.name for m in self._role_set)})"