from typing import List, Protocol

from utilix.oop.design_pattern.behavioral.observer.subject import Subject
from utilix.oop.design_pattern.behavioral.observer.subscriber import Subscriber


class Publisher(Protocol):
    _subscribers: List[Subscriber]

    def attach_subscriber(self, subscriber: Subscriber) -> None: ...

    def detach_subscriber(self, subscriber: Subscriber) -> None: ...

    def notify_subscribers(self, subject:Subject) -> None: ...