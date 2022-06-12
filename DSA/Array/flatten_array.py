class NestedIterator:
    def __init__(self, nestedList):
        self.data = []
        self.flatten(nestedList)

    def flatten(self, lst):
        for el in lst:
            if type(el) is int:
                self.data.append(el)
            else:
                self.flatten(el)

    def hasNext(self) -> int:
        return len(self.data)

    def next(self) -> int:
        return self.data.pop(0)


if __name__ == '__main__':
    i, v = NestedIterator([[1, [11, 10, 9]], 2, [1, 1]]), []
    while i.hasNext():
        v.append(i.next())
    print(v)
