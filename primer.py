class Node:
    def __init__(self, key, left=None, right=None):
        """Create a new tree node."""
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.key!r}, {self.left}, {self.right})"

"""class N(Node):
    def __repr__(self):
        return f"N({self.key!r}, {self.left}, {self.right})"    """


tree2 = Node(3, Node(1), Node(2))
print(tree2) # Node(3, Node(1, None, None), Node(2, None, None))
tree_of_n = N(3, N(1), N(2))
print(repr(tree_of_n)) # N(3, N(1, None, None), N(2, None, None))