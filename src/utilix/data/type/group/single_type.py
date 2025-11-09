from typing import List,Generic,TypeVar, override

from utilix.data.type.group.group import Group
from utilix.data.type.group.interface import Interface

T=TypeVar('T')

class SingleType(Group, Generic[T], Interface):
    def __init__(self, members:List[T], validate_type:bool)->None:
        super(Group, self).__init__(members)
        self._validate_type = validate_type

    @override(Group)
    def get_members(self)->List[T]:
        return self._members

    @override(Group)
    def add_member(self, member: T)->None:
        if self._validate_type == True:
            self._members.append(member)

    @override(Group)
    def remove_member(self, member: T)->None:
        self._members.remove(member)
