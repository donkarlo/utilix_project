from abc import ABC, abstractmethod


class Project(ABC):
    @abstractmethod
    def run(self):
        pass