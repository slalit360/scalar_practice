from DSA.Tree.BT import Node, Tree


class BinarySearchTree(Tree):

    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if root.val == data:
                return root
            elif data < root.val:
                root.left = self.insert(root.left, data)
            elif data > root.val:
                root.right = self.insert(root.right, data)
        return root

    def search(self, root,  k):
        if root is None:
            return False
        if root.val == k:
            return True
        elif k <= root.val:
            self.search(root.left, k)
        else:
            self.search(root.right, k)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.root = bst.insert(bst.root, 5)
    bst.root = bst.insert(bst.root, 7)
    bst.root = bst.insert(bst.root, 1)
    print(bst.inorder(bst.root))
    print(bst.search(bst.root, 7))
