from typing import Any, override

from utilix.data.type.group.decorator.decorator import Decorator as GroupDecorator
from utilix.data.type.group.decorator.interface import Interface as GroupInterface


class UniqueNamed(GroupDecorator):
    def __init__(self, inner: GroupInterface, create_modality_if_name_doesnt_exist:bool):
        super().__init__(inner)

    @override(GroupDecorator)
    def add_member(self, name:str, value:Any)->GroupDecorator:
        pass

