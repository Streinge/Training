class TreeBuilder:
    def __init__(self, key=None, parent=None):
        self.key = key
        self.parent = parent
        self.descendant = []

    def add(self, key):
        tmp = self.__class__(key, parent=self)
        print('новый объект', tmp)
        self.descendant.append(tmp)
        return tmp
    
    @property
    def structure(self, list_full=[]):
        global i
        i += 1
        # print(i)
        # print('список ', list_full)
        if self.descendant:
            if self.key is None:  
                for x in self.descendant:
                    # print('x.key ', x.key)
                    list_full.append(x.key)
                    # print('список ', list_full)
                    # str = f"self.key:{self.key!r}, x:{x.key}, list_full:{list_full}"
                    # print(str)
                    x.structure(list_full)
                    # print('После вызова')
                    # str = f"self.key:{self.key!r}, x:{x.key}, list_full:{list_full}"
                    # print(str)
            else:
                list_new = []
                for x in self.descendant:
                    # print('x.key ', x.key)
                    list_new.append(x.key)
                    # print('список новый ', list_new)
                    # str = f"self.key:{self.key!r}, x:{x.key}, list_full:{list_full}"
                    # print(str)
                    x.structure(list_new)
                    # print('После вызова')
                    # str = f"self.key:{self.key!r}, x:{x.key}, list_full:{list_full}"
                    # print(str)
                list_full.append(list_new)
        return list_full

i = 0
tree = TreeBuilder()
print(tree)
print(tree.__dict__) 
_1st = tree.add('1st')  
print(tree.__dict__)  
_2st = _1st.add('2st')  
print(_1st.__dict__)
print(_2st.__dict__)
_3st = _2st.add('3st')
print(_1st.__dict__)
print(_2st.__dict__)
_4st = _1st.add('4st')
print(_1st.__dict__)
print(tree.structure)
