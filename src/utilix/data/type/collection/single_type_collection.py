from typing import List,Generic,TypeVar

from utilix.data.type.collection.collection import Colection as BaseCollection
T=TypeVar('T')
class SingleTypeCollection(BaseCollection, Generic[T]):
    def __init__(self, members:List[T])->None:
        super(BaseCollection, self).__init__(members)

    def get_members(self)->List[T]:
        return self._members

    def add_member(self, member: T)->None:
        self._members.append(member)

    def remove_member(self, member: T)->None:
        self._members.remove(member)
