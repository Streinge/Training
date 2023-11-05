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
    
    # @property
    def structure(self, list_full=[]):
        global i
        i += 1 
        print(i)
        if self.key:
            list_full.append(self)
            print('список ', list_full)
        if self.descendant:
            for x in self.descendant:
                print('x.key ', x.key)
                x.structure(list_full)
        print('дошло до конца')
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
print(tree.structure())
