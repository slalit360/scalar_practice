class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"[{self.data}]"


class SinglyLinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        self.size = 0

    @staticmethod
    def get_node(data):
        return Node(data)

    # insert operation
    def insert_at_head(self, data):
        node = self.get_node(data)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
        self.size += 1

    def insert_at_end(self, data):
        node = self.get_node(data)
        if self.head:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = node
        else:
            self.head = node
        self.size += 1

    def insert_at_pos(self, data, index):
        if index == 0:
            self.insert_at_head(data)
        elif index == self.size:
            self.insert_at_end(data)
        elif index > self.size:
            pass
        else:
            node = self.get_node(data)
            counter = 0
            tmp = self.head
            while tmp and counter < index - 1:
                tmp = tmp.next
                counter += 1
            node.next = tmp.next
            tmp.next = node
            self.size += 1

    # delete operation
    def delete_at_head(self):
        if self.head:
            tmp = self.head
            self.head = self.head.next
            self.size -= 1
            val = tmp.data
            del tmp
            return val
        else:
            print("Empty list cannot delete!")

    def delete_at_end(self):
        if self.head:
            if self.head.next is None:
                tmp = self.head
                self.head = None
                del tmp
                self.size -= 1
            else:
                tmp = self.head
                while tmp.next.next is not None:
                    tmp = tmp.next
                del tmp.next
                tmp.next = None
                self.size -= 1
        else:
            print("Empty list cannot delete!")

    def delete_by_value(self, data):
        if not self.head:
            return None

        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1

        tmp = self.head

        while tmp:
            if tmp.next and tmp.next.data == data:
                tmp.next = tmp.next.next
                self.size -= 1
            else:
                tmp = tmp.next

        self.head = tmp

    def delete_duplicates(self):
        head = self.head
        s = Node(0, self.head)
        p = s

        tmp = self.head
        while tmp:
            if tmp.next and tmp.data == tmp.next.data:
                while tmp.next and tmp.data == tmp.next.data:
                    tmp = tmp.next
                p.next = tmp.next
            else:
                p = p.next
            tmp = tmp.next

        self.head = s.next

    def get_all_unique(self):
        head = self.head
        if not head:
            return head
        tmp = head
        while tmp:
            if tmp.next and tmp.data == tmp.next.data:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        self.head = head

    def delete_at_idx(self, index):
        if index == 0:
            self.delete_at_head()
        elif index == self.size - 1:
            self.delete_at_end()
        elif index > self.size:
            print("Index is not valid so, cannot delete!")
        else:
            count = 0
            tmp = self.head
            while count < index - 1:
                tmp = tmp.next
                count += 1
            tmp.next = tmp.next.next
            del tmp
            self.size -= 1

    # search in list
    def search(self, data):
        tmp = self.head
        while tmp:
            if tmp.data == data:
                return True
            tmp = tmp.next
        return False

    def __str__(self):
        op = ""
        tmp = self.head
        while tmp:
            op += str(tmp) + " -> "
            tmp = tmp.next
        op += "None"
        return op


if __name__ == '__main__':
    llist = SinglyLinkedList()
    llist.insert_at_end(10)
    llist.insert_at_head(5)
    llist.insert_at_head(1)
    llist.insert_at_end(11)
    print(llist)
    llist.insert_at_end(9)
    llist.insert_at_end(8)
    llist.insert_at_pos(data=7, index=6)
    print(llist)
    # llist.delete_at_head()
    # print(llist)
    # llist.delete_at_end()
    llist.delete_by_value(60)
    print(llist)


