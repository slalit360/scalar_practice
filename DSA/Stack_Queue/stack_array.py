from DSA.Stack_Queue.istack import IStack


class Stack(IStack):
    def __init__(self):
        self.container = []
        self.size = 0
        self.top = -1

    def push(self, data):
        self.top += 1
        if self.top < len(self.container):
            self.container[self.top] = data
        else:
            self.container.append(data)

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.container[self.top]
        else:
            return "Stack is empty"

    def get_top(self):
        return self.container[-1]

    def is_empty(self):
        return self.top == -1

    def __str__(self):
        return f"{self.container}"


if __name__ == '__main__':
    stk = Stack()
    stk.push(1)
    stk.push(2)
    print(stk)
    print(stk.get_top())
    print(stk.pop())
    print(stk.pop())
    print(stk.pop())
