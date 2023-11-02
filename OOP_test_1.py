class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key=None):
        if self.key == None:
            self.key = key
        else:
            print('key ', key, 'self.key', self.key)
            if key < self.key:
                self.left = Node(key)
                print('self.left ', self.left)
                if self.right:
                   self.key = key 
            else:
                self.right = Node(key)
                print('self.right', self.right)
                if self.left:
                    self.key = key

tree = Node()
tree.insert(9)
tree.insert(17)
tree.insert(4)
"""tree.insert(3)
tree.insert(6)
print(tree.key)  # 9
print(tree.left.key)  # 4"""
print(tree)
print(tree.left.key)
print(tree.right.key)
