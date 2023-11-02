class Person:
    def __init__(self, name):
        self.name = name
    @property
    def full_name(self):
        return self.name
    @full_name.setter
    def full_name(self, new):
        self.name = new

tom = Person('Thomas')
tom.full_name = tom.full_name + 'hhhhh'
print(tom.full_name)  # 'Thomas Smith'
