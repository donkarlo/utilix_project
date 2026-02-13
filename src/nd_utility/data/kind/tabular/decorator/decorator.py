import Interface
from nd_utility.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator


class Decorator(BaseDecorator, Interface):
    """
    """

    def __init__(self, inner: Interface, var: Type):
        super(BaseDecorator, self).__init__(inner)
