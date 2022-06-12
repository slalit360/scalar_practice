class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        if not self.min_stk:
            self.min_stk.append(val)
        elif self.min_stk[-1] >= val:
            self.min_stk.append(val)
        self.stk.append(val)

    def pop(self) -> None:
        if self.stk and self.min_stk:
            if self.stk[-1] == self.min_stk[-1]:
                self.min_stk.pop()
            return self.stk.pop()

    def top(self) -> int:
        if self.stk:
            return self.stk[-1]

    def getMin(self) -> int:
        if self.min_stk:
            return self.min_stk[-1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())   # return -3
    print(minStack.pop())
    print(minStack.top())  #  return 0
    print(minStack.getMin())   # return -2