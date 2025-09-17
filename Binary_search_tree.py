class Node:
    def __init__(self, val):
        self.left = None
        self.data = val
        self.right = None

class BST:
    def create(self, val):
        return Node(val)

    def insert(self, node, data):
        if node is None:
            return self.create(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


t1 = BST()
n = int(input())
root = t1.create(n)

while True:
    k = int(input())
    if k == -1:
        break
    root = t1.insert(root, k)

print("\nInorder Traversal: ")
t1.inorder(root)

print("\nPreorder Traversal: ")
t1.preorder(root)

print("\nPostorder Traversal: ")
t1.postorder(root)

