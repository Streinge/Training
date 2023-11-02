class Counter:
    def __init__(self, value=0):
        self.value = value


    def inc(self, delta=1):  
        return Counter(self.value + delta)


    def dec(self, delta=1):
        if self.value - delta < 0:
            self.value = 0
        return Counter(self.value - delta)


c = Counter()
print(c.inc().inc(5).dec(2).value)

# Старый экземпляр не должен изменяться
d = c.inc(100)
print(d.dec().value)  # 99

forty_two = Counter(42)
print(forty_two.value)  # 42