from typing import Protocol

from nd_utility.oop.design_pattern.behavioral.observer.subject import Subject


class Subscriber(Protocol):
    def do_something_with_new_published_subject(self, published_subject:Subject)-> None: ...