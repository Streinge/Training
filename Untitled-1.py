class MyClass(object):
    def __init__(self):
        self.level = 0
    def inclev(self):
        self.level += 1
    def declev(self):
        self.level -= 1

    __enter__ = inclev  # For __enter__, just alias inclev, no need for wrapper
    def __exit__(self, exc_type, exc_value, traceback):
        self.declev()


other_instance = MyClass()
print(other_instance.level)
with other_instance:
    print(other_instance.level)
    with other_instance:
        print(other_instance.level)
    print(other_instance.level)