class MultiKeyDict:
    def __init__(self, **kwargs):
        self.dict = {}
        for key, values in kwargs.items():
            list_value = []
            list_value.append(values)
            self.dict[key] = list_value

    def __getitem__(self, key):
        return self.dict[key][0]

    def __setitem__(self, key, value):
        self.dict[key][0] = value

    def alias(self, **kwargs):
        for nickname in list(kwargs.keys()):
            original = kwargs[nickname]
            self.dict[nickname] = self.dict[original]


mkd = MultiKeyDict(x=100, y=[10, 20])
mkd.alias(z='x')  # 'z' теперь означает то же, что и 'x'
print(mkd['z'])
mkd['z'] += 1
print(mkd['x'])
mkd.alias(z='y')
mkd['z'] += [30]
print(mkd['y'])
mkd = MultiKeyDict(a=1, b='foo')
print(mkd.__dict__)
print(mkd['a'])  # 1
print(mkd['b'])  # 'foo'
mkd.alias(aa='a', bb='b')
print(mkd.__dict__)
print(mkd['aa'])  # 1
print(mkd['bb'])  # 'foo'
