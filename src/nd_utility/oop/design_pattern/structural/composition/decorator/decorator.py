from nd_utility.oop.design_pattern.structural.composition.example import Component
from nd_utility.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator


class Decorator(BaseDecorator, Component):
    def __init__(self, inner:Component):
        BaseDecorator.__init__(self, inner)