from typing import Union, Optional, Iterator, TypeVar, Generic

from nd_utility.data.kind.group.group import Group

T = TypeVar("T")


class UniKind(Group, Generic[T]):
    """
    Runtime-typed specialization of Group.

    You must provide member_type at construction time.
    The type is enforced on initial members and on add_member/reset_members.
    """

    def __init__(self, member_type: type, members: Optional[list[T]] = None) -> None:
        self._member_type = member_type
        if members is not None:
            self._ensure_members_type(members)
        super().__init__(members)

    def get_member_type(self) -> type:
        return self._member_type

    def add_member(self, member: T) -> None:
        self._ensure_member_type(member)
        super().add_member(member)

    def reset_members(self, members: Optional[list[T]] = None) -> None:
        if members is not None:
            self._ensure_members_type(members)
        super().reset_members(members)

    def get_members(self) -> list[T]:
        return self._members  # type: ignore[return-value]

    def __iter__(self) -> Iterator[T]:
        return iter(self._members)  # type: ignore[return-value]

    def __getitem__(self, index: Union[int, slice]) -> T:
        return self._members[index]  # type: ignore[return-value]

    def _ensure_member_type(self, member: T) -> None:
        if not isinstance(member, self._member_type):
            raise TypeError(
                f"UniKind expects members of type {self._member_type.__name__}, got {type(member).__name__}")

    def _ensure_members_type(self, members: list[T]) -> None:
        for member in members:
            self._ensure_member_type(member)
