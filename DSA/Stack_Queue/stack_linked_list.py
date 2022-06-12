from DSA.LinkedList.SLL import SinglyLinkedList
from DSA.Stack_Queue.istack import IStack


class Stack(IStack):
    def __init__(self):
        self.container = SinglyLinkedList()

    def push(self, data):
        self.container.insert_at_head(data)

    def pop(self):
        if self.container.head:
            return self.container.delete_at_head()
        else:
            return "Stack is empty"

    def get_top(self):
        return self.container.head.data

    def is_empty(self):
        return self.container.head is None

    def __str__(self):
        return f"{self.container}"


if __name__ == '__main__':
    stk = Stack()
    stk.push(1)
    stk.push(2)
    print(stk.get_top())
    print(stk)
    print(stk.pop())
    print(stk)
    print(stk.pop())
    print(stk)
    print(stk.pop())
