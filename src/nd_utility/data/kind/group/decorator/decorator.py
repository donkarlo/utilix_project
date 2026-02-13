from nd_utility.data.kind.group.interface import Interface as GroupInterface
from nd_utility.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator


class Decorator(BaseDecorator, GroupInterface):
    def __init__(self, inner: GroupInterface):
        super(BaseDecorator, self).__init__(inner)