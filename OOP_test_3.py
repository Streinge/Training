class TreeBuilder:
    def __init__(self, value=None, node=None):
        self.value = value
        self.parent = None
        self.child = None
        self.node = node
    def add(self, value):
           if self.value is None:
                self.value = value
           else:
               self.node = self.__class__(value)
               return self.node
    def add_next(self, value):
        self.data.append([value])
    @property
    def structure(self, list=[]):
        if self is None:
            list.append(self.value)
            if self.node is not None:
                list.append(self.node.value)
                self.node.structure()
        return list
    # это заготовка сеттера
    """@structure.setter
    def strucrure(self, list):
        self.list = list"""


tree = TreeBuilder()
tree.add('1st')
tree.add('2nd')
print(tree.__dict__)
print(tree.node.__dict__)
#tree.structure()

# print(tree.__dict__)
# print(tree.structure)
""" tree.add_next('2nd')
print(tree.structure)
tree.add_next('3nd')
print(tree.structure)"""