class MultiKeyDict:
    def __init__(self, **kwargs):
        self.dict = kwargs

    def __getitem__(self, value):
        print('getitem  ', self.dict[value])
        return self.dict[value][0]

    def __setitem__(self, x_new, y_new):
        print('x_new, y_new ', x_new, y_new)
        list_new = []
        list_new.append(y_new)
        print('list_new ', list_new)
        self.dict[x_new] = list_new

    def alias(self, **kwargs):
        # получение значения псеводнима
        nickname = list(kwargs.keys())[0]
        print(nickname)
        # получение значения оригинала
        original = kwargs[nickname]
        print(original)
        # запись значения по ключу оригинала в список
        list_original = []
        list_original.append(self.dict[original])
        # перевод значения по ключу в список
        self.__setitem__(original, list_original)
        # добавление пары псевдоним-оригинал в исходный список
        self.__setitem__(nickname, list_original)


mkd = MultiKeyDict(x=100, y=[10, 20])
print(mkd.__dict__)

mkd.alias(z='x')  # 'z' теперь означает то же, что и 'x'
print('после z=x ', mkd.__dict__)
print('mkd[x] ', mkd['x'])
print('mkd[y] ', mkd['y'])
print('mkd[z] ', mkd['z'])
print(mkd.__dict__)
mkd['z'] += 1
print(mkd.__dict__)