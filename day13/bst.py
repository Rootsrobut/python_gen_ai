class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, data):
        self.root = self.rinsert(self.root, data)

    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.rinsert(root.left, data)
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root

    # Search
    def search(self, data):
        return self.rsearch(self.root, data)

    def rsearch(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.rsearch(root.left, data)
        else:
            return self.rsearch(root.right, data)

    # Traversals
    def inorder(self):
        result = []
        self.rinorder(self.root, result)
        return result

    def preorder(self):
        result = []
        self.rpreorder(self.root, result)
        return result

    def postorder(self):
        result = []
        self.rpostorder(self.root, result)
        return result

    def rinorder(self, root, result):
        if root is None:
            return
        self.rinorder(root.left, result)
        result.append(root.item)
        self.rinorder(root.right, result)

    def rpreorder(self, root, result):
        if root is None:
            return
        result.append(root.item)
        self.rpreorder(root.left, result)
        self.rpreorder(root.right, result)

    def rpostorder(self, root, result):
        if root is None:
            return
        self.rpostorder(root.left, result)
        self.rpostorder(root.right, result)
        result.append(root.item)

    # Minimum value
    def min_value(self, temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.item

    # Maximum value
    def max_value(self, temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.item

    # Delete node
    def rdelete(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.rdelete(root.left, data)
        elif data > root.item:
            root.right = self.rdelete(root.right, data)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children:
            # Get inorder successor (smallest in the right subtree)
            root.item = self.min_value(root.right)
            # Delete the inorder successor
            root.right = self.rdelete(root.right, root.item)
        return root


# Example usage:
if __name__ == "__main__":
    tree = BST()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(val)

    print("Inorder:", tree.inorder())
    print("Preorder:", tree.preorder())
    print("Postorder:", tree.postorder())

    print("Min value:", tree.min_value(tree.root))
    print("Max value:", tree.max_value(tree.root))

    print("\nDeleting 20...")
    tree.root = tree.rdelete(tree.root, 20)
    print("Inorder after deleting 20:", tree.inorder())

    print("\nDeleting 30...")
    tree.root = tree.rdelete(tree.root, 30)
    print("Inorder after deleting 30:", tree.inorder())

    print("\nDeleting 50...")
    tree.root = tree.rdelete(tree.root, 50)
    print("Inorder after deleting 50:", tree.inorder())




