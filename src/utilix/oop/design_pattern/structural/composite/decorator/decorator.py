from utilix.oop.design_pattern.structural.composite.example import Component
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator


class Decorator(BaseDecorator, Component):
    def __init__(self, inner:Component):
        BaseDecorator.__init__(self, inner)