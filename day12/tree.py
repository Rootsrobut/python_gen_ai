class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)
def print_level_order(root):
    if not root:
        return
    # Queue stores (node, level)
    queue = [(root, 0)]
    current_level = 0
    print(f"Level {current_level}:", end=" ")
    while queue:
        node, level = queue.pop(0)
        # If we moved to a new level
        if level != current_level:
            current_level = level
            print(f"\nLevel {current_level}:", end=" ")
        print(node.data, end=" ")
        for child in node.children:
            queue.append((child, level + 1))


# Example usage
n = Node(5)
p = Node(6)
q = Node(7)
r = Node(8)
s = Node(9)

n.add_child(p)
n.add_child(q)
p.add_child(r)
q.add_child(s)

print_level_order(n)
