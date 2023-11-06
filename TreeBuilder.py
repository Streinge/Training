class TreeBuilder:
    def __init__(self, key=None, parent=None):
        self.key = key
        self.parent = parent
        self.descendant = []
        self.cur = self

    def add(self, key):
        print(self)
        global i
        i += 1
        print(i)
        print('self.cur из add', self.cur)
        tmp = self.cur.__class__(key, parent=self)
        print('новый объект', tmp)
        self.cur.descendant.append(tmp)
        print(self.cur.descendant)
        return tmp

    def __enter__(self):
        print("Inside __enter__")
        self.cur = self.descendant[0]
        print('self.descendant ', self.descendant)
        print(self.cur)

    def __exit__(self, exc_type, exc_value, traceback):
        self = self.parent

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

i = 0
tree = TreeBuilder()
print(tree)
print(tree.__dict__)
print(tree.structure)
print(tree.add('1st').__dict__)
print(tree.__dict__)
print(tree.structure)
print(tree.__dict__)
print(tree.cur)
with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
print(tree.structure)