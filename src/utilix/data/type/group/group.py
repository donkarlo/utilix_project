from typing import List, Any

from utilix.data.type.group.decorator.interface import Interface


class Group(Interface):
    def __init__(self, members: List) -> None:
        self.__init(members)

    def __init(self, members:List) -> None:
        self._members = members


    def get_members(self) -> List:
        return self._members

    def add_member(self, member:Any) -> None:
        self._members.append(member)

    def remove_member(self, member:Any) -> None:
        self._members.remove(member)

    def reset_members(self, members:List) -> None:
        self.__init(members)
