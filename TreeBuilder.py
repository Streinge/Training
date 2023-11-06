class TreeBuilder:
    def __init__(self, key=None):
        self.key = key
        self.descendant = []
        self.current = self

    def add(self, key):
        tmp = self.__class__(key)
        self.descendant.append(tmp)
        self.current = tmp
        return tmp

    def __enter__(self):
        print('self.current ', self.current)
        self.current = self.descendant[0]

    def __exit__(self, exc_type, exc_value, traceback):
        return self

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
_1st = tree.add('1st')
print(tree.structure)
"""with tree:
    _2nd = tree.add('2nd')
    with tree:
        _3st = tree.add('3rd')"""
print(tree.structure)
print(tree.__dict__)
"""print(_1st.__dict__)
print(_2nd.__dict__)
print(_3st.__dict__)"""