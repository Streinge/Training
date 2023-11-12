class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        x = self.__class__.__name__
        return f"{x}({self.key!r}, {self.left}, {self.right})"

    def search(self, key, target=None):
        print(key)
        if self.key == key:
            print('значение нашлось')
            target = self
            print('target ', target)
            return self
        else:
            if self.left is not None:
                print('заходил влево')
                print('self.left.key ', self.left.key)
                print('target ', target)
                self.left.search(key, target)
            if self.right is not None:
                print('заходил вправо')
                print('self.right.key ', self.right.key)
                print('target ', target)
                self.right.search(key, target)
        return target


node5 = Node(5)
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
print(tree.search(6))