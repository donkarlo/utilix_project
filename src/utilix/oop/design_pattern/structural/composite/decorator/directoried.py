from utilix.oop.design_pattern.structural.composite.component import Component
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator
from utilix.os.file_system.file.file import File


class Directoried(BaseDecorator, Component):
    def __init__(self, inner: Component, file:File):
        BaseDecorator.__init__(self, inner)

    def create_file_system_structure():
        # if component
        pass