class TreeBuilder:
    def __init__(self, key=None, parent=None):
        self.key = key
        self.descendant = []
        self.current = self
        self.parent = parent

    def add(self, key):
        tmp = self.current.__class__(key, parent=self.current)
        self.current.descendant.append(tmp)
        return tmp

    def __enter__(self):
        print('self.current ', self.current)
        if self.current.descendant[0]:
            self.current = self.current.descendant[0]

    def __exit__(self, exc_type, exc_value, traceback):
        self.current = self.current.parent

    def _structure(self, list_full):
        if self.descendant:
            if self.key is None:
                for x in self.descendant:
                    list_full.append(x.key)
                    x._structure(list_full)
            else:
                list_new = []
                for x in self.descendant:
                    list_new.append(x.key)
                    x._structure(list_new)
                list_full.append(list_new)
        return list_full

    @property
    def structure(self):
        return self._structure([])


tree = TreeBuilder()
print(tree.structure)
tree.add('1st')
print(tree.structure)
with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
    tree.add('4th')
    with tree:
        pass
print(tree.structure)
print(tree.__dict__)
