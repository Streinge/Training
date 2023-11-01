class Node:
    """Ссылка на фактический класс это self.__class__
    Не понимаю зачем делать из этого такую тайну. 
    Подскажу больше - self.__class__() - это функция , 
    возвращающая новый экземпляр класса. Не надо никаких 
    self.__init__ и Node(key) - такое не пройдет тест второй"""
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if self.key is None:
            self.key = key
            return
        print('key ', key, 'self.key ', self.key)
        if (key < self.key):
            print('меньше')
            if (self.left is not None):
                self = self.left
                return self.insert(key)
            else:
                self.left = self.__class__(key)
                return self.left
        if (key > self.key):
            print('больше')
            if (self.right is not None):
                self = self.right
                return self.insert(key)
            else:
                self.right = self.__class__(key)
                return self.right


tree = Node()
tree.insert(9)
print('tree', tree)
print('tree_dict__ ', tree.__dict__)
_17_ = tree.insert(17)
print('tree_dict__ ', tree.__dict__)
print('_17_dict ', _17_.__dict__)
_4_ = tree.insert(4)
print('tree_dict__ ', tree.__dict__)
print('_4_dict ', _4_.__dict__)
_3_ = tree.insert(3)
print('_4_dict ', _4_.__dict__)
print('_3_dict ', _3_.__dict__)
_6_ = tree.insert(6)
print('_4_dict ', _4_.__dict__)
print(tree.key)  # 9
print(tree.left.key)  # 4
print(tree.right.key)  # 17
print(tree.left.left.key)  # 3
print(tree.left.right.key)  # 6"""
