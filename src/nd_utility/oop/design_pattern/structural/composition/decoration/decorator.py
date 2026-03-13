from nd_utility.oop.design_pattern.structural.composition.example import Component
from nd_utility.oop.design_pattern.structural.decoration.decorator import Decorator as BaseDecorator


class Decorator(BaseDecorator, Component):
    def __init__(self, innerr_composite:Component):
        BaseDecorator.__init__(self, innerr_composite)

    def stringify(self)->str:
        pass