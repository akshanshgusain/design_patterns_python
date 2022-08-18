from abc import ABC, abstractmethod
from behavioral.observer.observer.iObserver import Observer


class Subject(ABC):

    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observer(self):
        pass
