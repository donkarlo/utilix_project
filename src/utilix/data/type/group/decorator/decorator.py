from utilix.data.type.group.interface import Interface as GroupInterface
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator


class Decorator(BaseDecorator, GroupInterface):
    def __init__(self, inner: GroupInterface):
        super(BaseDecorator, self).__init__(inner)