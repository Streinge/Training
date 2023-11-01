import operator

class Node:
    def __init__(self, key, left=None, right=None):
        """Create a new tree node."""
        self.key = key
        self.left = left
        self.right = right

# BEGIN (write your solution here)
    def _list_nodes(self, list_full):
        # список элементов дерева текущего уровня
        list_full.append(self)
        if self.left is not None:
            self.left._list_nodes(list_full)
        if self.right is not None:
            self.right._list_nodes(list_full)
        return list_full

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key!r}, {self.left}, {self.right})"

    def to_list(self):
        list_full =[]
        list_full_new = self._list_nodes(list_full)[:]
        sum_keys = []
        for x in list_full_new:
            sum_keys.append(x.key)
        return sum_keys

    def __len__(self):
        return len(self.to_list())

    def total(self):
        return sum(self.to_list())

    def minimum(self):
        return min(self.to_list())

    def maximum(self):
        return max(self.to_list())

    def every(self, operation):
        list_keys = self.to_list()
        for key in list_keys:
            if operation(key) is False:
                return False
        return True
                

    def some(self, operation):
        list_keys = self.to_list()
        for key in list_keys:
            if operation(key):
                return True
        return False

"""class N(Node):

    def __repr__(self):
        return f"N({self.key!r}, {self.left}, {self.right})" """
 

tree = Node(
    9,
    Node(
        4,
        Node(8),
        Node(
            6,
            Node(3),
            Node(7),
        ),
    ),
    Node(
        17,
        right=Node(
            22,
            Node(20),
        ),
    ),
)

print(len(tree))  # 9
print(tree.total())  # 96
print(tree.to_list())  # [9, 4, 8, 6, 3, 7, 17, 22, 20]
print(tree.minimum())  # 3
print(tree.maximum())  # 22
tree2 = Node(3, Node(1), Node(2))
print(tree2)
print(tree.every(lambda key: key <= 22))  # True
print(tree.some(lambda key: key > 22))  # False
print(tree.every(lambda key: key < 22)) # False
print(tree.some(lambda key: key == 22)) # True
tree_of_n = N(3, N(1), N(2))
print(repr(tree_of_n))