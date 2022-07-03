import math


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
        self.counter = 0

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

    def node_count(self, node, maxx):
        # count nodes which is greater than all of its ancestor
        if node is None:
            return
        else:
            if node.val > maxx:
                self.counter += 1
            # Left traversal
            self.node_count(node.left, max(maxx, node.val))
            # Right traversal
            self.node_count(node.right, max(maxx, node.val))

    def search_k(self, node: Node, k):
        if node is None:
            return False
        if node.val == k:
            return True
        return self.search_k(node.left, k) or self.search_k(node.right, k)

    def is_identical(self, root1, root2):
        if (not root1 and root2) or (root1 and not root2):
            return False
        elif not root1 and not root2:
            return True
        return root1.val == root2.val and self.is_identical(root1.left, root2.left) and self.is_identical(root1.right,
                                                                                                          root2.right)

    def is_mirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 and root2 and root1.val == root2.val:
            return self.is_mirror(root1.left, root2.right) and self.is_mirror(root1.right, root2.left)

        return False


if __name__ == '__main__':
    e = Node(5)
    e.left = Node(8)

    b = Node(2)
    b.left = Node(4)
    b.right = e

    c = Node(3)
    c.left = Node(4)
    c.left.right = Node(5)
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

    t.node_count(t.root, -math.inf)
    print(t.counter)

    print(t.search_k(t.root, 5))
    print(t.search_k(t.root, 15))

    print(t.is_identical(t.root, t.root))

    # t = Tree()
    # t.root = Node(1)
    # t.root.left = Node(2)
    # t.root.left.left = Node(3)
    # t.root.right = Node(2)
    # t.root.right.right = Node(3)
    # print(t.is_mirror(t.root, t.root))
