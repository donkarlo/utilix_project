from typing import Type, Any, TypeVar, Generic, override

from utilix.data.type.group.decorator.decorator import Decorator as GroupDecorator
from utilix.data.type.group.decorator.interface import Interface

T = TypeVar("T")

class SingleTyped(GroupDecorator, Generic[T]):
    def __init__(self, inner: Interface, type_hint:Type[T], validate_type:bool)->None:
        super().__init__(inner)
        self._type_hint = type_hint
        self._validate_type = validate_type
        if validate_type == True:
            for member in self._inner.get_members():
                if not isinstance(member, self._type_hint):
                    raise TypeError(f"type {type(member)} is not a {self._type_hint.__name__}")

    def get_type_hint(self) -> Type[T]:
        return self._type_hint
    def get_validate_type(self) -> bool:
        return self._validate_type

    @override(GroupDecorator)
    def add_member(self, member:T, validate_type:bool) ->None:
        if validate_type == True:
            if not isinstance(member, self._type_hint):
                raise TypeError(f"type {type(member)} is not a {self._type_hint.__name__}")
        self._inner.add_member(member)