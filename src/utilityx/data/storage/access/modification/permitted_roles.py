from utilityx.data.storage import Storage
from utilityx.data.storage.access.modification.role_set import RoleSet


class PermittedRoles:
    def __init__(self, role_set: set[RoleSet]):
        """
        The minimum Permitted rule is read. other than that permission is not necessary
        Args:
            role_set:
        """
        self._role_set = role_set  # trust the caller

    def add(self, role: RoleSet) -> None:
        self._role_set.add(role)

    def remove(self, role: RoleSet) -> None:
        self._role_set.discard(role)

    def has(self, role: RoleSet) -> bool:
        return role in self._role_set

    def __str__(self) -> str:
        return f"Group({', '.join(m.name for m in self._role_set)})"