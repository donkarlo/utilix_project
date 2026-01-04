from typing import List, Any, Optional
from utilix.data.kind.group.interface import Interface
from typing import Any, Iterator, List, Optional
from collections.abc import Iterable, Container, Sized


class Group(Interface, Iterable, Container, Sized):
    def __init__(self, members: Optional[List[Any]]) -> None:
        if members is None:
            members = []
        self.__init(members)

    def __init(self, members:List[Any]) -> None:
        self._members = members


    def get_members(self) -> List[Any]:
        return self._members

    def add_member(self, member:Any) -> None:
        self._members.append(member)

    def remove_member(self, member:Any) -> None:
        self._members.remove(member)

    def reset_members(self, members:List) -> None:
        self.__init(members)

    def __iter__(self) -> Iterator[Any]:
        return iter(self._members)

    def __len__(self) -> int:
        return len(self._members)

    def __contains__(self, item: object) -> bool:
        return item in self._members


