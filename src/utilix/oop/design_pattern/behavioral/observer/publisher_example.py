from utilix.oop.design_pattern.behavioral.observer.publisher import Publisher
from utilix.oop.design_pattern.behavioral.observer.subject import Subject
from utilix.oop.design_pattern.behavioral.observer.subscriber import Subscriber


class PublisherExample(Publisher):
    def __init__(self):
        self._subscribers = []
    def attach_subscriber(self, subscriber: Subscriber) -> None:
       self._subscribers.append(subscriber)

    def detach_subscriber(self, subscriber: Subscriber) -> None:
        self._subscribers.remove(subscriber)

    def notify_subscribers(self, subject: Subject) -> None:
        for subscriber in self._subscribers:
            subscriber.do_something_with_new_published_subject(subject)