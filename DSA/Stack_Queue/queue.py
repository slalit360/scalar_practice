from abc import ABC, abstractmethod


class IQueue(ABC):

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def get_front(self):
        pass

    @abstractmethod
    def get_rear(self):
        pass


class Queue(IQueue):
    def __init__(self):
        self.container = []

    def insert(self, data):
        self.container.append(data)

    def delete(self):
        if self.container:
            return self.container.pop(0)

    def get_front(self):
        if self.container:
            return self.container[0]

    def get_rear(self):
        if self.container:
            return self.container[-1]

    def __str__(self):
        return f"{self.container}"


if __name__ == '__main__':
    q = Queue()
    q.insert(1)
    q.insert(2)
    q.insert(3)
    print(q)
    q.delete()
    print(q)
    q.insert(5)
    print(q)

    print(q.get_front())
    print(q.get_rear())
