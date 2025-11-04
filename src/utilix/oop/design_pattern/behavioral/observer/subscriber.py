from typing import Protocol

from utilix.oop.design_pattern.behavioral.observer.subject import Subject


class Subscriber(Protocol):
    def do_something_with_new_published_subject(self, published_subject:Subject)-> None: ...