from typing import Any, Iterator, Optional, TypeVar, Union
from collections.abc import Container, Iterable, Sized, Sequence

from nd_utility.data.kind.group.interface import Interface

T = TypeVar("T")


class Group(Interface, Sequence):
    """
    If group = Group()
    then you can use 'in' operator on group and also do group[index]
    """

    def __init__(self, members: Optional[list[Any]] = None) -> None:
        if members is None:
            self._members: list[Any] = []
        else:
            self._members = list(members)

    def get_members(self) -> list[Any]:
        return self._members

    def add_member(self, member: Any) -> None:
        self._members.append(member)

    def add_members(self, members: list[Any]) -> None:
        for member in members:
            self.add_member(member)

    def remove_member(self, member: Any) -> None:
        self._members.remove(member)

    def reset_members(self, members: Optional[list[Any]] = None) -> None:
        if members is None:
            self._members = []
        else:
            self._members = list(members)

    def __iter__(self) -> Iterator[Any]:
        return iter(self._members)

    def __len__(self) -> int:
        return len(self._members)

    def __contains__(self, item: object) -> bool:
        return item in self._members

    def __getitem__(self, index: Union[int, slice]) -> Any:
        return self._members[index]