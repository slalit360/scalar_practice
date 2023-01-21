# Python3 program merge two sorted linked
# in third linked list using recursive.

# Node class


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'[{self.data}]'


# Constructor to initialize the node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Method to print linked list
    def printList(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    # Function to add of node at the end.
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head

        while last.next:
            last = last.next
        last.next = new_node


# Function to merge two sorted linked list.
def mergeLists(head1, head2):
    # create a temp node NULL
    temp = None

    # List1 is empty then return List2
    if head1 is None:
        return head2

    # if List2 is empty then return List1
    if head2 is None:
        return head1

    # If List1's data is smaller or
    # equal to List2's data
    if head1.data <= head2.data:

        # assign temp to List1's data
        temp = head1

        # Again check List1's data is smaller or equal List2's
        # data and call mergeLists function.
        temp.next = mergeLists(head1.next, head2)

    else:
        # If List2's data is greater than or equal List1's
        # data assign temp to head2
        temp = head2

        # Again check List2's data is greater or equal List's
        # data and call mergeLists function.
        temp.next = mergeLists(head1, head2.next)

    # return the temp list.
    return temp


# Driver Function
if __name__ == '__main__':
    # Create linked list :
    list1 = LinkedList()
    list1.append(5)
    list1.append(10)
    list1.append(15)

    # Create linked list 2 :
    list2 = LinkedList()
    list2.append(2)
    list2.append(3)
    list2.append(20)
    list1.printList()
    print(' ')
    list2.printList()
    # Create linked list 3
    list3 = LinkedList()

    # Merging linked list 1 and linked list 2
    # in linked list 3
    list3.head = mergeLists(list1.head, list2.head)

    print("Merged Linked List is:")
    list3.printList()

# This code is contributed by 'Shriaknt13'.
