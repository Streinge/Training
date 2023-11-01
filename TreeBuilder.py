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
    def structure(self, list=[]):
        if self.descendant:
            for x in self.descendant:
                list.append(x.key)
                print(list)
                print(self.descendant)
                x.structure(list)
        return list



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
tree.structure