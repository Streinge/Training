class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        x = self.__class__.__name__
        return f"{x}({self.key!r}, {self.left}, {self.right})"

    def search(self, key):
        if self.key == key:
            return self
        else:
            if key < self.key:
                if self.left is not None:
                    return self.left.search(key)
            if key >= self.key:
                if self.right is not None:
                    return self.right.search(key)
                



""" node5 = Node(5)
node22 = Node(22, left=Node(20))
tree = Node(
    9,
    Node(
        4,
        Node(3),
        Node(
            6,
            node5,
            Node(7),
        ),
    ),
    Node(
        17,
        right=node22,
    ),
)

print(tree)
print(tree.search(6).key)
print(tree.search(6).right.key)
print(tree.search(5) is node5)
print(tree.left.left.key)
single_node = Node(1)
print(single_node.key)
print(single_node.left)
print(single_node.right) """
node5 = Node(5)
node22 = Node(22, right=Node(20))
tree = Node(
    9,
    left=Node(
        4,
        left=Node(
            6,
            left=Node(5),
            right=Node(7),
        ),
        right=Node(3),
    ),
    right=Node(
        17,
        right=Node(22),
    ),
)
print(tree.search(5) is None)
print(tree.search(7) is None)
print(tree.search(6) is None)
print(tree.search(4).key == 4)
print(tree.search(22).key == 22)
