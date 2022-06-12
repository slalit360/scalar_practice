from abc import ABC, abstractmethod


class IStack(ABC):

    @abstractmethod
    def push(self, data):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def get_top(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass