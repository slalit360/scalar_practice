class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"[{self.val}]"


class Tree:
    def __init__(self):
        self.root = None
        self.count = 0

    @staticmethod
    def preorder(root: Node) -> list:
        ans = [root.val]
        if root.left:
            ans += Tree.preorder(root.left)
        if root.right:
            ans += Tree.preorder(root.right)
        return ans

    @staticmethod
    def inorder(root: Node) -> list:
        ans = []
        if root.left:
            ans += Tree.inorder(root.left)
        ans.append(root.val)
        if root.right:
            ans += Tree.inorder(root.right)
        return ans

    @staticmethod
    def postorder(root: Node) -> list:
        ans = []
        if root.left:
            ans += Tree.postorder(root.left)
        if root.right:
            ans += Tree.postorder(root.right)
        ans.append(root.val)
        return ans

    def height(self, root: Node) -> int:
        if not root:
            return -1
        return max(self.height(root.left), self.height(root.right)) + 1

    def count_nodes(self, root: Node) -> int:
        if not root:
            return 0
        return self.count_nodes(root.left) + self.count_nodes(root.right) + 1

    def sum_nodes(self, root: Node) -> int:
        if not root:
            return 0
        return self.sum_nodes(root.left) + self.sum_nodes(root.right) + root.val


if __name__ == '__main__':
    e = Node(5)
    e.left = Node(8)

    b = Node(2)
    b.left = Node(4)
    b.right = e

    c = Node(3)
    c.left = Node(6)
    c.right = Node(7)

    a = Node(1)
    a.left = b
    a.right = c

    t = Tree()
    t.root = a

    print(t.preorder(t.root))
    print(t.inorder(t.root))
    print(t.postorder(t.root))

    print(t.height(t.root))
    print(t.count_nodes(t.root))
    print(t.sum_nodes(t.root))
